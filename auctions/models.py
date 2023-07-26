from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Category(models.Model):
    categoryName= models.CharField(max_length=50)
    
    def __str__(self):
        return self.categoryName

class Bid(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name="usr")
    bid=models.FloatField(default=0)
    
    def __str__(self):
        return (f"bid:{self.bid}")
   

class aListing(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=200)
    imageUrl=models.CharField(max_length=1000)
    Price=models.ForeignKey(Bid,on_delete=models.CASCADE,blank=True,related_name="Bid")
    NumOfBids=models.IntegerField(default=0)
    Owner=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name="user")
    isActive= models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True,related_name="category")
    WatchList=models.ManyToManyField(User,blank=True,null=True,related_name="WatchList")
    def __str__(self):
        return self.Title


class Comment(models.Model):
    person=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name="person")
    listing=models.ForeignKey(aListing,on_delete=models.CASCADE,blank=True,related_name="listing")
    comment=models.CharField(max_length=200)

    def __str__(self):
        return (f"{self.person} comment on {self.listing}")