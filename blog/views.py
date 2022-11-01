from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

from blog.models import Post


def get_date(post):
    return post['date']


# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[0:3]
    # sorted_post = sorted(all_posts, key=get_date)
    # latest_posts = sorted_post[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, "blog/all-posts.html", {
        "all_post": all_posts
    })


def post_detail(request, slug):
    post_identified = Post.objects.get(slug=slug)
    tags_count = post_identified.tags.all().values_list(flat=True).count()
    # print(f"Number of Tags ---------------------------------------{tags_count}")
    try:
        # post_identified = next(post for post in all_posts if post['slug'] == slug)
        return render(request, "blog/post-detail.html", {
            "post": post_identified,
            "post_tags": post_identified.tags.all(),
            "tags_count": tags_count,
        })
    except:
        message = render_to_string("404.html")
        # raise Http404(Exception)
        return HttpResponseNotFound(message)
