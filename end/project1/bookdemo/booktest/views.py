from django.shortcuts import render,redirect,reverse
from django.template import loader
from .models import Book, Hero

# Create your views here.


# MVT 中的V视图模块
# 再次接受请求  处理数据  返回响应
from django.http import HttpResponse


# 3.编写对应的视图函数
def index(request):
    # return HttpResponse("这里是首页")
    # 1.获取模板
    # template = loader.get_template('index.html')
    # 2.渲染模板数据
    books = Book.objects.all()
    # context = {'books': books}
    # result = template.render(context)
    # 3.将渲染的结果使用httpresponse返回
    # return HttpResponse(result)

    return render(request, 'index.html', {'books': books})


def detail(request, bookid):
    # return HttpResponse("这里是详情页"+bookid)
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {'book': book}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(request, 'detail.html', {'book': book})


def deletebook(request,bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # 删除一本书之后仍然回到列表页
    # return HttpResponseRedirect(redirect_to='/booktest/'+bookid)
    return redirect(to="/")

def edithere(request,heroid):
    hero=Hero.objects.get(id=heroid)
    #使用get方法进入英雄的编辑页面
    if request.method == "GET":
        return render(request, 'edithere.html',{"hero":hero})
    elif request.method == "POST":
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.save()
        url = reverse("booktest:detail", args=(hero.book.id,))
        return redirect(to=url)
def deletehero(request,heroid):
    #惰性查询 能不操作数据库就不操作数据库  不得已才操作数据库  Hero.objects.get(id=heroid)  并没有操作数据库
    hero=Hero.objects.get(id=heroid)
    #如果访问hero中的对象  不操作数据库得不到数据  此时才真正操作数据库
    #一定先获取在删除
    bookid=hero.book.id
    hero.delete()
    url=reverse("booktest:detail",args=(bookid,))
    return redirect(to=url)

def addhero(request,bookid):
    #视图函数中可以同时存在get与post请求  默认get
    if request.method=="GET":
        return render(request,'addhero.html')
    elif request.method=="POST":
        hero=Hero()
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url=reverse("booktest:detail",args=(bookid,))
        return redirect(to=url)

def addbook(request):
    #视图函数中可以同时存在get与post请求  默认get
    if request.method=="GET":
        return render(request,'addbook.html')
    elif request.method=="POST":
        book=Book()
        book.title = request.POST.get("booktitle")
        book.price = request.POST.get("bookprice")
        book.pub_date = request.POST.get("bookpub_date")
        book.save()
        url=reverse("booktest:index")
        return redirect(to=url)

def editbook(request,bookid):
    book=Book.objects.get(id=bookid)
    #使用get方法进入书籍的编辑页面
    if request.method == "GET":
        return render(request, 'editbook.html',{"book":book})
    elif request.method == "POST":
        book.title = request.POST.get("booktitle")
        book.price = request.POST.get("bookprice")
        book.pub_date = request.POST.get("bookpub_date")
        book.save()
        url = reverse("booktest:index")
        return redirect(to=url)

def about(request):
    return HttpResponse("这里是关于页面")

# 使用django模板
