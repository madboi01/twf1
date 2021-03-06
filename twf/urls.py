"""twf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="home"),
    path('signup/',views.signup_page,name="signup"),
    path('postsignup/',views.postsignup_page,name="postsignup"),
    path('enter-details/',views.details_page,name="details"),
    path('signin/',views.signin,name="signinpage"),
    path('postlogin/',views.postlogin),
    path('logout/',views.signout,name='signout'),
    path('post_details/',views.post_details,name="post_details"),
    path('details/',views.show_details,name="show_details")
]
