from DjangoUeditor.models import UEditorField
from django.db import models

# Create your models here.


class ArticleCategory(models.Model):
    name = models.CharField(max_length=20,default='',unique=True,verbose_name='文章分类名称')
    parent_category = models.ForeignKey('self',null=True,blank=True,related_name='sub_cate', verbose_name='父级分类ID')
    code = models.CharField(default="", max_length=30,unique=True, verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")

    class Meta:
        verbose_name= '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200,verbose_name='文章标题')
    summary = models.TextField(max_length=400,verbose_name='文章摘要')
    content = UEditorField(verbose_name='文章详情', width=1000, height=300, toolbars="full", imagePath="article/ueditor/",
                          filePath="article/ueditor/", upload_settings={"imageMaxSize": 1204000,"imageUrlPrefix": "xxxxxxxxxxx"}, default='')
    category = models.ForeignKey(ArticleCategory)
    hit_num = models.IntegerField(verbose_name='文章点击量',default=0)
    image = models.ImageField(max_length=300,upload_to="article/images/",default="",verbose_name='文章图片')
    is_hot = models.BooleanField(default=False,verbose_name='是否是热门文章')

    add_time = models.DateTimeField(auto_now_add=True,verbose_name='文章新建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='文章最后更新时间')

    class Meta:
        verbose_name='文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title