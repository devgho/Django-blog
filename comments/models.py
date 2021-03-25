from django.db import models
# from blog.models import Post
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=20,verbose_name="姓名")
    email = models.EmailField(verbose_name="邮箱")
    url = models.CharField(max_length=100,null=True,blank=True,verbose_name="网址")
    content = models.TextField(verbose_name="内容")
    # post = models.ForeignKey(Post,null=True,on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post',null=True,on_delete=models.CASCADE)
    # add_time = models.DateTimeField(default=timezone.now(),verbose_name="添加时间")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-add_time','name']

    def __str__(self):
        return self.content[:20]
