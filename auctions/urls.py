from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("Create", views.createListing, name="create"),
    path("Categories/<str:category>", views.catContent, name="catContent"),
    path("Listing/<int:id>", views.Listing, name="Listing"),
    path("WatchList", views.displaywatchlist, name="WatchList"),
    path("RemoveWatchListing/<int:id>", views.RemoveWatchListing, name="RemoveWatchListing"),
    path("AddWatchListing/<int:id>", views.AddWatchListing, name="AddWatchListing"),
    path("addComment/<int:id>", views.addComment, name="addComment"),
    path("addbid/<int:id>", views.addbid, name="addbid"),
    path("MyListings", views.MyListings, name="MyListings"),
    path("closeAuction/<int:id>", views.closeAuction, name="closeAuction"),
     

    
]

