'''
from django.db import models
from django.contrib import admin
# Create your models here.
'''


'''
class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.TextField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null = True)
    
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-date_time']

admin.site.register(Article)
'''
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('分类',max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField('标签', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name


class Entry(models.Model):
    title = models.CharField('文章标题',max_length=128)
    author = models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE)
    img = models.ImageField(upload_to='myblog_img',null=True,blank=True,verbose_name='博客配图')
    abstract = models.TextField('摘要',max_length=256,null=True,blank=True)
    visiting = models.PositiveIntegerField('访问量',default=0)
    category = models.ManyToManyField('Category',verbose_name='博客分类')
    tags = models.ManyToManyField('Tag',verbose_name='标签')
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    modifyed_time = models.DateTimeField('修改时间',auto_now=True)
    body = models.TextField('正文',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        #获取当前博客详情页的url
       # return reverse('myblog:myblog_detail',kwargs={"myblog_id":self.id})     #app名字，详情页url的别名，参数是当前博客的id
        return reverse('myblog:detail',kwargs={'entry_id':self.id})
    def increase_visiting(self):
        #访问量加1
        self.visiting += 1
        self.save(update_fields=['visiting'])   #只保存某个字段

    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客正文'
        verbose_name_plural = verbose_name

class User(models.Model):
    '''用户表'''

    gender = (
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    #img = models.ImageField(upload_to='myblog_img2',null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


