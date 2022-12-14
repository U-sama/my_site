from django.shortcuts import render
from datetime import date

# Create your views here.
all_posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Osama",
        "date": date(2020, 7, 15),
        "title": "Mountain Hiking",
        "exerpt": "There is nothing loke the views and the montains you see in the forests and I wasn't prepared of what happend!",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?"""

    },

    {
        "slug" : "Coding",
        "image": "coding.png",
        "author": "Osama",
        "date": date(2022, 1, 20),
        "title": "Clean Code",
        "exerpt": "I will show you the best prctice youshould do to have your code clean and ready for real world deployment and be more rubost to changes.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?"""

    },

    {
        "slug" : "walking-in-the-woods",
        "image": "woods.jpg",
        "author": "Osama",
        "date": date(2019, 6, 3),
        "title": "Walking in the Woods",
        "exerpt": "It's awesome to live in a diffrent way and try new things as we will walk thow how I manged to stay in the woods for more than 7 days without Masturbation ",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Minus deleniti quaerat blanditiis repellendus laudantium commodi possimus maiores illum,
                     magni in quod, eaque odit placeat officia aliquam voluptas, autem nam ex?"""

    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",
    {"posts":latest_posts})

def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts":all_posts})

def post_details(request,slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {"post" : post})