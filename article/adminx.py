import xadmin

from .models import Article,ArticleCategory


class ArticleAdmin(object):
    # 显示列表中的字段
    list_display =['title','summary','content']
    # 搜索功能中的字段，时间字段不加到搜索里面
    search_fields =['title','summary','content']
    # 过滤字段 可以加日期
    list_filter =['title','summary','content','add_time']
    style_fields = {"content": "ueditor"}



class ArticleCategoryAdmin(object):
    pass


xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(ArticleCategory,ArticleCategoryAdmin)