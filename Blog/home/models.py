from django.db import models
from users.models import User
# Create your models here.
from django.utils import timezone


class ArticleCategory(models.Model):
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_category'
        verbose_name = '类别管理'
        verbose_name_plural = verbose_name


class Article(models.Model):
    """
    文章
    """
    # 定义文章作者。 author 通过 models.ForeignKey 外键与内建的 User 模型关联在一起
    # 参数 on_delete 用于指定数据删除的方式，避免两个关联表的数据不一致。
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章标题
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)

    category = models.ForeignKey(
        ArticleCategory,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )
    # 标签
    tags = models.CharField(max_length=20, blank=True)
    # 标题
    title = models.CharField(max_length=100, null=False, blank=False)
    # 概要
    sumary = models.CharField(max_length=200, null=False, blank=False)
    # 正文
    content = models.TextField()
    # 浏览量,文章评论数
    total_views = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    # 创建,更新 时间
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        db_table = 'tb_article'
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    # 评论内容
    content = models.TextField()
    # 评论的文章
    article = models.ForeignKey(Article,
                                on_delete=models.SET_NULL,
                                null=True)
    # 发表评论的用户
    user = models.ForeignKey('users.User',
                             on_delete=models.SET_NULL,
                             null=True)
    # 评论发布时间
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.title

    class Meta:
        db_table = 'tb_comment'
        verbose_name = '评论管理'
        verbose_name_plural = verbose_name
