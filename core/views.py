from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from core.models import Blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def private_place(request):
    return HttpResponse("Members only!", content_type="text/plain")

# Does a query looking for all Blog objects


def listing(request):
    data = {
        "blogs": Blog.objects.all(),
    }

    return render(request, "listing.html", data)

# Takes a blog_id as a parameter and uses it to look up the Blog object


def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    data = {
        "blog": blog,
    }

    return render(request, "view_blog.html", data)

# Shows the HttpRequest attributes


def see_request(request):
    text = f""" 
        Some attributes of the HttpRequest object:
        
        scheme: {request.scheme}
        path: {request.path}
        method: {request.method}
        GET: {request.GET}
        user: {request.user}    """

    return HttpResponse(text, content_type="text/plain")

# See the attribute information of the current user


def user_info(request):

    text = f""" 

        Selected HttpRequest.user attributes:
        
        username: {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff: {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active: {request.user.is_active}        
        
    """
    return HttpResponse(text, content_type="text/plain")

# Checks if the user is a staff user or superuser.


@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("Employees must wash hands", content_type="text/plain")

# Create asynchronous communication with the user. Used for notifying the user


@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello: {username}")
    messages.add_message(request, messages.WARNING, "SDAOKGJSADFLKJALSK'")

    return HttpResponse("Messages added, go back to root website", content_type="text/plain")
