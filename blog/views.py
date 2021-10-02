from django.views import generic
from .models import Post
from .forms import CommentForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


class PostList(generic.ListView):
    queryset = Post.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')
    template_name = "blog.html"

# def post_list(request):
#     return render(request, 'blog/blog.html')    



def post_detail(request, slug):
    template_name = "post_detail.html"
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