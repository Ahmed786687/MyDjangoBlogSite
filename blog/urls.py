from . import views
from django.urls import path

from .views import StartingPageView, PostsView, PostDetailView, ReadLaterView

urlpatterns =[
    path("", StartingPageView.as_view(), name= "starting-page"),
    path("posts", PostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", PostDetailView.as_view(), name="post-detail-page"),
    path("read-later", ReadLaterView.as_view(), name="read-later"),
]