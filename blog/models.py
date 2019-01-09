from django.db import models
from django.utils import  timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    #这个ForeignKey是指向另外一个模型的连接
    title = models.CharField(max_length=200)#用有限的字符定义一个变量
    text = models.TextField()#没有限度的长文本
    created_date = models.DateTimeField(default=timezone.now)#日期和时间
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title