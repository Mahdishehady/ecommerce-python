from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    Listings = aListing.objects.all()
    categories=Category.objects.all()
    
        
    return render(request, "auctions/index.html",{
        "Listings":Listings,
        "categories":categories
     }
     )


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createListing(request):
    if request.method == "POST":
        user=request.user
        title=request.POST["title"]
        description=request.POST["description"]
        imageUrl=request.POST["imageUrl"]
        price=request.POST["price"]
        category=request.POST["category"]
        startbid=Bid(user=user,bid=price)
        startbid.save()
        getCategory=Category.objects.get(categoryName=category)
        Listing=aListing(
            Title=title,
            Description=description,
            imageUrl=imageUrl,
            Price=startbid,
            Owner=user,
            category=getCategory
        )
        Listing.save()
        return HttpResponseRedirect(reverse(index))
    else:
        categories=Category.objects.all()
        return render(request,"auctions/createListing.html",{
            "categories":categories
        })




def catContent(request,category):
    if(category not in 'All'):
        category1=Category.objects.get(categoryName=category)
        categories=Category.objects.all()
        Listings = aListing.objects.filter(category=category1)
        return render(request, "auctions/categories.html",{
       "Listings":Listings,
       "categories":categories,
       "cat":category
      }
      )
    else:
         Listings = aListing.objects.all()
         categories=Category.objects.all()
    
        
         return render(request, "auctions/categories.html",{
             "Listings":Listings,
             "categories":categories,
             "cat":category
             }
             )
        

def Listing(request,id):
    ListingData=aListing.objects.get(id=id)
    inWatchList= request.user in ListingData.WatchList.all()
    allcomments=Comment.objects.filter(listing=ListingData)
    return render(request,"auctions/Listing.html",{
        "Listing":ListingData,
        "inWatchList":inWatchList,
        "allcomments":allcomments,
        "message":None
    })

def RemoveWatchListing(request,id):
    listingdata=aListing.objects.get(pk=id)
    user=request.user
    listingdata.WatchList.remove(user)
    return HttpResponseRedirect(reverse("Listing",args=(id,)))




def AddWatchListing(request,id):
    listingdata=aListing.objects.get(pk=id)
    user=request.user
    listingdata.WatchList.add(user)
    return HttpResponseRedirect(reverse("Listing",args=(id,)))


def displaywatchlist(request):
    user=request.user
    watchListings=user.WatchList.all()

    return render(request,"auctions/watchlist.html",{
        "Listings":watchListings
     })

def addComment(request,id):
    user=request.user
    listing=aListing.objects.get(pk=id)
    comment=request.POST["newComment"]
    newComment=Comment(
        person=user,
        listing=listing,
        comment=comment
    )
    newComment.save()
    return HttpResponseRedirect(reverse("Listing",args=(id,)))

def addbid(request,id):
    if request.method == "POST":
        user=request.user
        bid=request.POST["newbid"]
        listing=aListing.objects.get(pk=id)
        if(float(bid) > listing.Price.bid):
            newbid=Bid(user=user,bid=float(bid))
            newbid.save()
            numofbids=listing.NumOfBids + 1
            aListing.objects.filter(pk=id).update(NumOfBids=numofbids)
            aListing.objects.filter(pk=id).update(Price=newbid)
            
            ListingData=aListing.objects.get(id=id)
            inWatchList= request.user in ListingData.WatchList.all()
            allcomments=Comment.objects.filter(listing=ListingData)
            return render(request,"auctions/Listing.html",{
                "Listing":ListingData,
                "inWatchList":inWatchList,
                "allcomments":allcomments,
                "message":True
                })
        else:
             ListingData=aListing.objects.get(id=id)
             inWatchList= request.user in ListingData.WatchList.all()
             allcomments=Comment.objects.filter(listing=ListingData)
             return render(request,"auctions/Listing.html",{
                "Listing":ListingData,
                "inWatchList":inWatchList,
                "allcomments":allcomments,
                "message":False
                })
def MyListings(request):
    user=request.user
    
    Listings=aListing.objects.filter(Owner=user)
    return render(request, "auctions/myListing.html",{
        "Listings":Listings
     }
     )

def closeAuction(request,id):
    user=request.user
    listing =aListing.objects.filter(pk=id)
    listing.update(isActive=False)
    return HttpResponseRedirect(reverse("MyListings",))
