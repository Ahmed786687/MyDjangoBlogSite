from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

from django.views.generic import ListView, DetailView
from django.views import View

from blog.models import Post
from blog.forms import CommentForm


def get_date(post):
    return post['date']


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super(StartingPageView, self).get_queryset()
        data = queryset[:3]
        return data


class PostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ["-date"]
    context_object_name = "all_post"


class PostDetailView(View):
    template_name = 'blog/post-detail.html'
    model = Post

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all(),
            "comment_count": post.comments.all().count(),

        }
        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)

        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
        }

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
        }
        return render(request, 'blog/post-detail.html', context)


class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context ={}
        if stored_posts is None or len(stored_posts) ==0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in =stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/read-later.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST['post_id'])
        if post_id in stored_posts:
            stored_posts.append(post_id)
            request.session['stored_posts'] = stored_posts
        return HttpResponseRedirect("/")

    # def get_context_data(self, **kwargs):
    #     context = super(PostDetailView, self).get_context_data()
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context

# Create your views here.

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by('-date')[0:3]
#     # sorted_post = sorted(all_posts, key=get_date)
#     # latest_posts = sorted_post[-3:]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })


#
# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#     return render(request, "blog/all-posts.html", {
#         "all_post": all_posts
#     })


# def post_detail(request, slug):
#     post_identified = Post.objects.get(slug=slug)
#     tags_count = post_identified.tags.all().values_list(flat=True).count()
#     # print(f"Number of Tags ---------------------------------------{tags_count}")
#     try:
#         # post_identified = next(post for post in all_posts if post['slug'] == slug)
#         return render(request, "blog/post-detail.html", {
#             "post": post_identified,
#             "post_tags": post_identified.tags.all(),
#             "tags_count": tags_count,
#         })
#     except:
#         message = render_to_string("404.html")
#         # raise Http404(Exception)
#         return HttpResponseNotFound(message)
