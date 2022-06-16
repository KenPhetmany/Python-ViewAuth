from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from core.models import Blog

# Does a query looking for all Blog objects


def listing(request):
    data = {
        "blogs": Blog.object.all()
    }

    return render(request, "listing.html", data)

# Takes a blog_id as a parameter and uses it to look up the Blog object


def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    data = {
        "blog": blog,
    }

    return render(request, "view_blog.html", data)
