from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:movie_pk>/',views.detail,name="detail"),
    path('<int:movie_pk>/comments/', views.comments, name='comments'),
    # path('<int:pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    # path('<int:pk>/<int:comment_pk>/comments/', views.comment_delete, name='comment_delete'),
    # path('<int:pk>/<int:comment_pk>/comments)
    # path('<int:movie_pk>/likes/', views.likes, name='likes'),
    # path('<username>/like_list/', views.like_list, name='like_list'),
]

# 영화 좋아요, 코멘트 좋아요 구현 필요