from django.urls import path
from blogging.views import stub_view, list_view, detail_view, add_model
from blogging.feeds import LatestEntriesFeed

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('new/', add_model, name="New Post"),
    path('latest/feed/', LatestEntriesFeed()),
]