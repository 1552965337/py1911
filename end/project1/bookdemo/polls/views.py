from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
# Create your views here.
from  django.views.generic import View,TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView
#View 是所有视图响应类的父类
from django.contrib.auth import authenticate,login as lin,logout as lot


def index(request):
    questions = Question.objects.all()
    return render(request,'polls/index.html',{"questions":questions})
    # return HttpResponse("首页")

#基于CBV的形式实现首页
class IndexView(ListView):
    # 方法二、继承ListView
    # template_name指明使用的模板
    template_name = "polls/index.html"
    # queryset 指明返回的结果列表
    queryset = Question.objects.all()
    # context_object_name 指明返回字典参数的健
    context_object_name = "questions"

    # 方法一、继承的TemplateView
    # template_name = "polls/index.html"
    # def get_context_data(self, **kwargs):
    #     return {"questions":Question.objects.all()}



def detail(request,qid):
    print(qid,"++")
    if request.method == "GET":
        print("当前用户：",request.user.username)
        if request.user and request.user.username !="":
            #已经登录过了
            # print("++",request.user.questions,type(request.user.questions.all()))
            try:
                question = Question.objects.get(id=qid)
                if question in request.user.questions.all():
                    print("已经投过票了")
                    url = reverse("polls:result",args=(qid))
                    return redirect(to=url)
                else:
                    try:
                        # question = Question.objects.get(id=qid)
                        print(question,"--")
                        #使用render发起一起请求
                        return render(request, 'polls/detail.html', {"question": question})

                    except Exception as e:
                        print(e)
                        return HttpResponse("问题不合法")
            except Exception as e:
                print(e,"----")
        else:
            # url =reverse('polls:login')+'?next=/polls/detail/'+qid+"/"
            url = reverse('polls:login') + '?next='+reverse('polls:detail',args=(qid,))
            return redirect(to=url)
    elif request.method == "POST":
        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes+=1
            choice.save()
            request.user.questions.add(Question.objects.get(id=qid))
            # 返回当前投票问题的投票结果页
            url = reverse("polls:result",args=(qid,))
            # 投票成功 返回投票结果
            return redirect(to=url)

        except:
            return HttpResponse("选项不合法")

    # return HttpResponse("详情页"+qid)

class DetailView(View):
    def get(self,request,qid):
        try:
            question = Question.objects.get(id=qid)
            print(question, "--")
            return render(request, 'polls/detail.html', {"question": question})

        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")
    def post(self,request,qid):
        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes += 1
            choice.save()
            # 返回当前投票问题的投票结果页
            url = reverse("polls:result", args=(qid,))
            # 投票成功 返回投票结果
            return redirect(to=url)

        except:
            return HttpResponse("选项不合法")

def result(request,qid):

    try:
        question = Question.objects.get(id=qid)
        return render(request,'polls/result.html',{"question":question})
    except Exception as e:
        print(e)
        return HttpResponse("问题不合法")

class ResultView(View):
    def get(self,request,qid):
        try:
            question = Question.objects.get(id=qid)
            return render(request, 'polls/result.html', {"question": question})
        except Exception as e:
            print(e)
            return HttpResponse("问题不合法")


def login(request):
    if request.method == "GET":
        return render(request, 'polls/login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 可以使用Django自带的用户认证系统
        user = authenticate(username=username, password=password)
        if user:
            lin(request, user)
            next= request.GET.get("next")
            print("取得next的参数为",next)
            if next:
                url=next
            else:
                url = reverse("polls:index")
            return redirect(to=url)
        else:
            url = reverse("polls:login")
            return redirect(to=url)
    # return HttpResponse("登录")

def regist(request):
    if request.method == "GET":
        return render(request, 'polls/regist.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if User.objects.filter(username=username).count() > 0:
            return HttpResponse("用户名已存在")
        else:
            if password == password2:
                User.objects.create_user(username=username, password=password)
                url = reverse("polls:login")
                return redirect(to=url)

            else:
                return HttpResponse("密码不一致")
    # return HttpResponse("注册")

def logout(request):
    # 调用Django的登出方法 目的是删除cookie
    lot(request)
    url = reverse("polls:index")
    return redirect(to=url)
    # return HttpResponse("退出")