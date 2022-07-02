from django.urls import include, path

from . import views
from .feeds import AtomSiteNewsFeed, LatestPostsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("about/", views.About.as_view()),
    path("contact/", views.Contact.as_view()),
    path("policy/", views.Policy.as_view()),
    path("download_policy/", views.download_policy)
]
