from django import template
from comments.models import Comment
register = template.Library()


@register.simple_tag
def get_comments(post):
    return Comment.objects.filter(post=post)