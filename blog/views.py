from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post

# Create your views here.
all_posts = [

       
]

def get_date(post):
    return post['date']

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html",
    {"posts":latest_posts})

def posts(request):
    all_posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {"all_posts":all_posts})

def post_details(request,slug):
    post = get_object_or_404(Post, slug=slug)
    #post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {"post" : post, "all_tags":post.tag.all()})