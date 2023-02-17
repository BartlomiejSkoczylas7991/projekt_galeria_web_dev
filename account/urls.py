from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
#path('login/', views.user_login, name='login_user'),
#path('logout/', views.logout_user, name='logout_user'),
#path('register/', views.register, name='register'),
#path('post/int:pk/', views.post_detail, name='post_detail'),
#path('post/new/', views.post_new, name='post_new'),
#path('post/int:pk/edit/', views.post_edit, name='post_edit'),
#path('post/int:pk/delete/', views.post_delete, name='post_delete'),
#path('post/int:pk/comment/', views.add_comment_to_post, name='add_comment_to_post'),
#path('comment/int:pk/approve/', views.comment_approve, name='comment_approve'),
#path('comment/int:pk/remove/', views.comment_remove, name='comment_remove'),
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]