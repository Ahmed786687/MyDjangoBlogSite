from datetime import date

from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound
from django.template.loader import render_to_string

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountain_hiking.jpg',
        'author': "Ahmad Iqbal",
        'date': date(2021, 7, 21),
        'title': 'Mountain Hiking',
        'excerpt': 'The flex property in CSS is the combination of flex-grow, flex-shrink,'
                   'and flex-basis property. It is used to set the length of flexible items.',
        'content': """The flex property is much responsive and mobile friendly. It is easy to position child elements and the main container. The margin does not collapse with the content margins. Order of any element can be easily changed without editing the HTML section. The flexbox was added to the CSS standards a few years ago to manage space distribution and element alignment. Basically it is one-dimensional layout syntax.
        The flex property in CSS is the combination of flex-grow, flex-shrink, and flex-basis property. It is used to set the length of flexible items. The flex property is much responsive and mobile friendly. It is easy to position child elements and the main container. The margin does not collapse with the content margins. Order of any element can be easily changed without editing the HTML section. The flexbox was added to the CSS standards a few years ago to manage space distribution and element alignment. Basically it is one-dimensional layout syntax.
        """
    },
    {
        'slug': 'programming-is-fun',
        'image': 'coding.png',
        'author': "Ahmad Iqbal",
        'date': date(2022, 3, 10),
        'title': 'Programming is fun',
        'excerpt': 'The flex property in CSS is the combination of flex-grow, flex-shrink,'
                   'and flex-basis property. It is used to set the length of flexible items.',
        'content': """The flex property is much responsive and mobile friendly. It is easy to position child elements and the main container. The margin does not collapse with the content margins. Order of any element can be easily changed without editing the HTML section. The flexbox was added to the CSS standards a few years ago to manage space distribution and element alignment. Basically it is one-dimensional layout syntax.
        The flex property in CSS is the combination of flex-grow, flex-shrink, and flex-basis property. It is used to set the length of flexible items. The flex property is much responsive and mobile friendly. It is easy to position child elements and the main container. The margin does not collapse with the content margins. Order of any element can be easily changed without editing the HTML section. The flexbox was added to the CSS standards a few years ago to manage space distribution and element alignment. Basically it is one-dimensional layout syntax.
        """
    },
    {
        'slug': 'into-the-woods',
        'image': 'woods.jpg',
        'author': "Ahmad Iqbal",
        'date': date(2020, 8, 5),
        'title': 'Into The Woods',
        'excerpt': 'The flex property in CSS is the combination of flex-grow, flex-shrink,'
                   'and flex-basis property. It is used to set the length of flexible items.',
        'content': """The flex property is much responsive and mobile friendly. It is easy to position child elements and the main container. The margin does not collapse with the content margins. Order of any element can be easily changed without editing the HTML section. The flexbox was added to the CSS standards a few years ago to manage space distribution and element alignment. Basically it is one-dimensional layout syntax.
        The flex property in CSS is the combination of flex-grow, flex-shrink, and flex-basis property. It is used to set the length of flexible items. The flex property is much responsive and mobile friendly. It is easy to position child elements and the main container. The margin does not collapse with the content margins. Order of any element can be easily changed without editing the HTML section. The flexbox was added to the CSS standards a few years ago to manage space distribution and element alignment. Basically it is one-dimensional layout syntax.
        """
    },
]


def get_date(post):
    return post['date']


# Create your views here.

def starting_page(request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_posts = sorted_post[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_post": all_posts
    })


def post_detail(request, slug):
    try:
        post_identified = next(post for post in all_posts if post['slug'] == slug)
        return render(request, "blog/post-detail.html", {
            "post": post_identified
        })
    except:
        message = render_to_string("404.html")
        # raise Http404(Exception)
        return HttpResponseNotFound(message)
