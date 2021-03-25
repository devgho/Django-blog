from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from .models import Comment
from .form import CommentForm
from django.shortcuts import get_object_or_404
# Create your views here.


def post_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)#因为post有get_absolute_url
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request,'blog/detail.html',context)

# def up(request):
#     c = Comment()
#     c.name = request.POST.get('name','')
#     c.email = request.POST.get('email','')
#     c.content = request.POST.get('content','')
#     c.url = request.POST.get('url','')
#     c.post = get_object_or_404(Post,id=request.POST.get('post_id',''))
#     try:
#         c.save()
#         return HttpResponse("<script type='text/javascript'>alert('评论成功！');"
#                             "window.location.replace(document.referrer);</script>")
#     except:
#         return HttpResponse("<script type='text/javascript'>alert('评论失败,请检查网络！');"
#                             "window.location.replace(document.referrer);</script>")