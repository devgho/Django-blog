from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    # path('up',views.up,name="up")
    path('postcomment/<int:pk>',views.post_comment,name="post_comment")
]