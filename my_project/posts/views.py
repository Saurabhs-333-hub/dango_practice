from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by("date")
    return render(request, "posts/posts_list.html", {"posts": posts})


def post_details(request, slug):
    return HttpResponse(slug)
