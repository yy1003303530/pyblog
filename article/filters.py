import django_filters
from .models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):
   # is_hot = django_filters.BooleanFilter(name="is_hot")

    class Meta:
        model = Article
        # category__name 是通过名称完全匹配过滤过滤，category是通过分类id过滤
        fields = ['is_hot','category__name','category']