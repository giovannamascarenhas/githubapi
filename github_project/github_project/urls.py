"""github_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework import routers
from django.conf.urls import include
from github_core.views import GithubtesteViewSet
from github_core.views import GithubrepositoriosViewSet
from github_core.views import GithubViewSet

router = routers.DefaultRouter()
router.register(r'users', GithubtesteViewSet, basename='homeapi')
router.register(r'repos', GithubrepositoriosViewSet, basename='reposapi')
router.register(r'newusers', GithubViewSet, basename='newusers')

urlpatterns = [
    #path("api/", GithubTeste.as_view(), name="teste_api"),
    #path('home/<str:username>', github, name="home"),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
