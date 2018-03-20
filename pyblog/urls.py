"""pyblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
import xadmin
from django.views.static import serve

from article.views import ArticleViewSet,ArticleCategoryViewSet
from pyblog.settings import MEDIA_ROOT

router = DefaultRouter()

router.register(r'articles', ArticleViewSet,base_name='articles')
router.register(r'categories', ArticleCategoryViewSet,base_name='categories')

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),# xadmin后台路由
    url(r'^', include(router.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')), #编辑器路由
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}), # 静态文件路由
    url(r'^login/', obtain_jwt_token),  #token 登录路由

]
