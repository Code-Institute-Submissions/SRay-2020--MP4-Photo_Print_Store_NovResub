""" This defines the models used for the Blog app """
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    """ This contains the parameters for the post model on the blog app """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """ This class defines meta behaviour of above class """
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ This returns post_detail to the user """
        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    """ This contains the parameters for the comment model on the blog app """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        """ This class defines meta behaviour of above class """
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
