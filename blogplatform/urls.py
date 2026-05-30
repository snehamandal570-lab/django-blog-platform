from django.contrib import admin
from django.urls import path, include
from posts.views import home, post_detail, create_post, edit_post, delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('create-post/', create_post, name='create_post'),
    path('edit-post/<int:id>/', edit_post, name='edit_post'),
    path('delete-post/<int:id>/', delete_post, name='delete_post'),
    path('accounts/', include('accounts.urls')),
]