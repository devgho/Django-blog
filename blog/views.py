from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown
from comments.form import CommentForm
from datetime import datetime
# Create your views here.


def index(request):
    post_list = Post.objects.all()
    return render(request, "blog/index.html", {
        'post_list': post_list,
    })


def detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc'
                                 ])
    comment_list = post.comment_set.all()
    form = CommentForm()
    return render(request,"blog/detail.html",{
        'post': post,
        'comment_list': comment_list,
        'form': form
    })


def archive(request,year,month):
    # return HttpResponse(date)
    post_list = Post.objects.filter(created_time__year=year,created_time__month=month)
    return render(request,'blog/index.html',{
        'post_list': post_list,
})


def category(request,ct):
    post_list = Post.objects.filter(category=ct)
    return render(request,'blog/index.html',{
        'post_list': post_list
    })


def author(request,name):
    post_list = Post.objects.filter(author=name)
    return render(request,'blog/index.html',{
        'post_list': post_list
    })