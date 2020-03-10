from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名")

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=20, verbose_name="商品名字")
    desc = models.CharField(max_length=100, null=True, blank=True, verbose_name="商品描述")
    price = models.FloatField(default=99.9, verbose_name="商品价格")
    historyprice = models.FloatField(default=99, verbose_name="商品历史价格")
    num = models.IntegerField(default=66, verbose_name="已售数目")
    # 在序列化关联模型时一定要声明related_name
    # 一找多  related_name  没有定义 c1.good_set.all()   related_name 定义了 c1.good.all()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类", related_name='goods')

    def __str__(self):
        return self.name


class GoodImgs(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name="商品展示图")
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name="商品", related_name='imgs')

    def __str__(self):
        return self.good.name


class User(AbstractUser):
    telephone = models.CharField(max_length=11, verbose_name="手机号")
    address = models.CharField(max_length=50, verbose_name="收货地址")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ManyToManyField(Good, verbose_name="商品")

    def __str__(self):
        return self.user.username + "的订单"


class Ads(models.Model):
    img = models.ImageField(upload_to='ads', verbose_name="轮播图")


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name="商品名字")
    desc = models.CharField(max_length=100, null=True, blank=True, verbose_name="商品描述")
    price = models.FloatField(default=99.9, verbose_name="商品价格")
    historyprice = models.FloatField(default=99, verbose_name="商品历史价格")
    num = models.IntegerField(default=55, verbose_name="已售数目")
    img = models.ImageField(upload_to='product', verbose_name="商品图")


class Recommend(models.Model):
    name = models.CharField(max_length=20, verbose_name="商品名字")
    desc = models.CharField(max_length=100, null=True, blank=True, verbose_name="商品描述")
    price = models.FloatField(default=99.9, verbose_name="商品价格")
    historyprice = models.FloatField(default=99, verbose_name="商品历史价格")
    num = models.IntegerField(default=55, verbose_name="已售数目")
    img = models.ImageField(upload_to='recommend', verbose_name="商品图")
