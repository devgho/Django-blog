from django import template
from blog.models import Post,Category
register = template.Library()
#注册自定义简单标签


@register.simple_tag
def addstr_tag():
    return 'Hello,Feng'


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month','DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()