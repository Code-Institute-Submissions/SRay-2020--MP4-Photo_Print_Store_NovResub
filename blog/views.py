""" This file contains the views displayed in the home app """
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    """ This renders the user a view of a list of the existing posts """
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"


def post_detail(request, slug):
    """ This renders the user a view of the details of a specific
        post and any corresponding comments which exist """
    template_name = "blog/post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
