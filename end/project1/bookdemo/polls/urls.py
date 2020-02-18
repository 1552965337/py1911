

from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    #函数视图
    url(r'^$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^result/(\d+)/$',views.result,name='result'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regist/$',views.regist,name='regist'),
    url(r'^logout/$',views.logout,name='logout'),



    #类视图
    # url(r'^$',views.IndexView.as_view(),name='index'),
    # url(r'^detail/(?P<qid>\d+)/$',views.DetailView.as_view(),name='detail'),
    # url(r'^result/(\d+)/$',views.ResultView.as_view(),name='result')
]