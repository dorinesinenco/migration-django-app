# ROUTER module
from mini_social.views import *

from django.urls import include, path

from django.contrib import admin

urlpatterns = [
  path("", homePage),
  path("signup", signupPage),

  # post routes
  path("post/create", addPost),
  path("post/save", savePost),

  # HW5:
  #    finish all of these views/urls
  path("get-posts", getPosts),
  path("delete-post", deletePost),
  path("update-post", updatePost),
  path("change-post", changePost),


  # user routes
  path("user/register", registerUser),
  path("user/login", loginUser),
  path("user/logout", logoutUser),
  path("user/preferences/notifications", toggleUserNotification),

  path("user/profile/<int:id>", userProfile),
  path("user/profile/edit/<int:id>", editUserProfile),
  path("user/add/friend/<int:id>", addUserFriend),

  # HW2:
  #     add single post route
  #     /post/<int:id> ---> show this single post on a page

  # development
  path("__debug__/", include("debug_toolbar.urls")),
  
  # admin
  path("admin/", admin.site.urls)
]
