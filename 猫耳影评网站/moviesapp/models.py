from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth.hashers import check_password as auth_check_password

"""继承系统自带的USER,也是用自己新建的字段"""
class UserInfo(AbstractUser):
    """用户信息"""
    username = models.CharField(max_length=10,unique=True,verbose_name='用户名')
    tel = models.CharField(max_length=11,verbose_name='手机号')
    avator = models.ImageField(upload_to='avator',default='imgs/default_avator.png',verbose_name='头像')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """分类标签"""
    tag_name = models.CharField(max_length=256,verbose_name='标签名')

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = '分类标签'
        verbose_name_plural = verbose_name


class MoviesInfo(models.Model):
    """电影信息"""
    poster = models.ImageField(upload_to='pics2',default='/media/imgs/404.png',verbose_name='海报')
    name = models.TextField(verbose_name='影名')
    director = models.CharField(max_length=256,verbose_name='导演')
    actor = models.CharField(max_length=256,verbose_name='主演')
    tag_char = models.CharField(max_length=256, verbose_name='分类标签名字')
    tag_for = models.ManyToManyField(Tag,max_length=256, verbose_name='分类标签外键',related_name='moviesinfo_set',blank=True,null=True)
    score = models.CharField(max_length=256, verbose_name='豆瓣评分')
    critics_num = models.IntegerField(blank=True,null=True,default=10,verbose_name='影评数')
    is_notice = models.NullBooleanField(default=False, verbose_name='开启轮播')
    # poster = models.CharField(max_length=128,verbose_name='海报')
    # time = models.DateField(auto_now_add=True, verbose_name='上映时间')
    # score = models.DecimalField(max_digits=2,decimal_places=1,verbose_name='豆瓣评分')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '电影信息'
        verbose_name_plural = verbose_name
        ordering = ['-score']


class Reviews(models.Model):
    """影评信息"""
    auth = models.CharField(max_length=256, verbose_name='作者',blank=True,null=True)
    name = models.CharField(max_length=256, null=True, blank=True, verbose_name='影评名')
    content = RichTextUploadingField(verbose_name='影评内容')
    movie_char = models.CharField(max_length=256, verbose_name='对应电影名称')
    movie_for = models.ForeignKey(MoviesInfo, max_length=128, verbose_name='对应电影外键', related_name='reviews_set',blank=True,null=True)
    visits = models.IntegerField(default=0, verbose_name='浏览量',blank=True,null=True)
    zan = models.IntegerField(default=0, verbose_name='点赞量',blank=True,null=True)
    # auth = models.ForeignKey(UserInfo,verbose_name='作者')
    # time = models.DateField(auto_now_add=True,verbose_name='发表日期')
    # content = models.TextField(verbose_name='影评内容')
    # 使用富文本编辑器


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '影评信息'
        verbose_name_plural = verbose_name
        ordering = ['zan']


