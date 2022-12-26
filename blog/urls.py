from django.urls import path
from . import views

urlpatterns = [
    path("", views.Starting_pageView.as_view(), name='starting-page'),
    path("posts", views.PostsListView.as_view(), name='posts-page'),
    path("posts/<slug:slug>", views.PostDetailView.as_view(),
         name='post-details-page'),  # posts/my-first-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
