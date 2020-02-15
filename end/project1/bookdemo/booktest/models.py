from django.db import models


# Create your models here.

# MVT   M 数据模型
# ORM   M 数据模型
# 在此处应用的数据模型类
# 每一张表就是一个模型类
# 有了ORM之后我们就可以定义出表对应的模型类
# 通过操作模型类去操作数据库  不需要写sql语句

# 1.注册mox 在setting.py 中的INSTALLED_APPS 添加应用名
# 2.生产迁移文件  用于与数据库交互 python manage.py makemigrations  会在对应的应用下方生成迁移文件不需要关注
# 3.执行迁移  会在对应的数据库中生产对应的表
# 模型类更改之后需要再次生成迁移文件  执行迁移
class Book(models.Model):
    """
    book 继承了Model类 应为Model类拥有操作数据库的功能
    """
    title = models.CharField(max_length=20, verbose_name="图书名")
    price = models.FloatField(default=0)
    pub_date = models.DateField(default="1983-06-01")
    author = models.CharField(max_length=20, default="sqz")
    desc = models.CharField(max_length=50, null=True, blank=True, db_column='description', help_text="请输入书籍备注信息")

    # telephon = models.CharField(max_length=11,unique=True)

    def __str__(self):
        # 此处必须返回
        return self.title


class Hero(models.Model):
    """
    hero 继承了Model 也可以操作数据库
    """
    name = models.CharField(max_length=22)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    # book 是一对多中的外键 on_delete代表删除数据时如何做
    # 在定义关系字段是使用 related_name="heros"   则一找多  一方对象.heros == 一方对象.小写多方类名_set
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="heros")

    def __str__(self):
        return self.name


# django  orm关联查询
# 多方Hero   一方Book
# 1.多找一， 多方对象.关系字段    exp: h1.book
# 2.一找多， 一方对象.小写多方类名_set.all()    exp: b1.hero_set.all()

class UserManager(models.Manager):
    """
    定义模型管理类   该模型不在具有objects对象
    """

    def deleteByTelePhone(self, tele):
        # django默认的objects 是Manager类型  *.objects.get()
        user = self.get(telephone=tele)
        user.delete()

    def createUser(self, tele):
        # self.model可以获取模型类构造函数
        user = self.model()  # 相当于 user = User()
        user.telephone = tele
        user.save()


class User(models.Model):
    telephone = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号码")
    # 自定义过管理类之后不再有objects
    objects = UserManager()

    def __str__(self):
        return self.telephone

    class Meta:
        # 表名
        db_table = "用户类"
        ordering = ["telephone"]
        # 在admin 页面进入模型类显示的名字
        verbose_name = "用户模型类a"
        # 在admin 页面在应用下方显示的模型名
        verbose_name_plural = "用户模型类s"


class Account(models.Model):
    username = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True, verbose_name="注册日期")


class Concact(models.Model):
    telephone = models.CharField(max_length=11, verbose_name="手机号")
    email = models.EmailField(default="1552965337@qq.com")
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="con")


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    sumary = models.TextField(verbose_name="正文")


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name="标题名")
    articles = models.ManyToManyField(Article, related_name="tags")

# 模型的关联关系
# 一对多   一方Book  实例b  多方Hero  实例h    关系字段定义在多方
# 一找多    b.hero_set.all()    如果定义过related_name='heros' 则使用  b.heros.all()
# 多找一  h.book


# 一对一   一方Account  实例a   一方Concact 实例c   关系字段定义在任意一方
# a 找 c  a.concact
# c 找 a  c.account


# 多对多  多方Article  实例a    多方Tag 实例t   关系字段可以定义在任意一方
# 添加关系   t.articles.add(a)    移除关系  t.articles.remove(a)
# a 找 所有的 t   a.tag_set.all()   如果定义过related_name='tags' 则使用 a.tags.all()
# t 找 所有的 a   t.articles.all()
