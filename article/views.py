from django.shortcuts import render

# Create your views here.
from rest_framework import mixins,viewsets
import django_filters
from rest_framework import viewsets,filters
from rest_framework.response import Response
from .models import Article,ArticleCategory
from .serializers import ArticleSerializer,ArticleCategorySerializer
from .filters import ArticleFilter


class ArticleViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    permission_classes = ()
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = ArticleFilter #过滤类设置
    search_fields = ('title', 'summary', 'content', )  # 搜索字段设置
    ordering_fields = ('title', 'summary', 'content', )   # 排序
    # 点击量 通过重写 retrieve方法来改变，查看详情的时候会调用 retrieve方法

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.hit_num +=1 # 文章点击量
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ArticleCategoryViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    permission_classes = ()
    serializer_class = ArticleCategorySerializer
    queryset =  ArticleCategory.objects.filter(parent_category=None)