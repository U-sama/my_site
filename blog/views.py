from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views import View
from django.views.generic import ListView, DetailView
from datetime import date
from .models import Post
from .forms import CommentForm

# Create your views here.
# Home Page
class Starting_pageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        query =  super().get_queryset()
        return query[:3]
    
# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html",
#     {"posts":latest_posts})

# Posts List Page
class PostsListView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]

# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/all-posts.html", {"all_posts":all_posts})


# Post Detail Page
class PostDetailView(View):

    def is_stored_post(self, request, post_pk):
        stored_posts = request.session.get("stored_posts")
        post_saved_for_later = False

        if stored_posts is not None:
            post_saved_for_later = str(post_pk) in stored_posts

        return post_saved_for_later

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        
        context = {
            "post":post,
            "all_tags":post.tag.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id"),
            "post_saved_for_later": self.is_stored_post(request, post.pk)
        }
        return render(request, "blog/post-detail.html", context )

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug)

        if comment_form.is_valid():
            data = comment_form.save(commit=False)
            data.post = post
            data.save()
            return HttpResponseRedirect(reverse("post-details-page", args=[slug]))

        
        context = {
            "post":post,
            "all_tags":post.tag.all(),
            "comment_form": comment_form,
            "comments":post.comments.all().order_by("-id"),
            "post_saved_for_later": self.is_stored_post(request, post.pk)
        }
        return render(request, "blog/post-detail.html", context )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["all_tags"] = self.object.tag.all()
    #     context["comment_form"] = CommentForm()
    #     return context

# def post_details(request,slug):
#     post = get_object_or_404(Post, slug=slug)
#     #post = next(post for post in all_posts if post['slug'] == slug)
#     return render(request, 'blog/post-detail.html', {"post" : post, "all_tags":post.tag.all()})

# Read later Page
class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["stored_posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(pk__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored_posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        post_pk = request.POST["post_pk"]

        if stored_posts == None:
            stored_posts = []

        if post_pk not in stored_posts:
            stored_posts.append(post_pk)
        else:
            stored_posts.remove(post_pk)
        
        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")
