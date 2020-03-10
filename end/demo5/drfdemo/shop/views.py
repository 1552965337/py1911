from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse

# 通过api_view装饰器可以将基于函数的视图转换成APIVIew基于类的视图
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from rest_framework import permissions
from . import permissions as mypermissions
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import *
# 引入django过滤类
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(["GET"])
def getuserinfo(request):
    user=JWTAuthentication().authenticate(request)
    seria=UserSerializers(instance=user[0])
    return Response(seria.data,status=status.HTTP_200_OK)




class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers



class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 之后拥有GET  POST  PUT PATCH  DELETE等HTTP动词操作
    queryset 指明需要操作的模型列表
    serializer_class 指明序列化类
    """
    queryset = Category.objects.all()
    # 1.通过属性指明
    serializer_class = CategorySerializers


    # 超级管理员可以创建分类  普通用户可以查看分类
    def get_permissions(self):
        if self.action == "create" or self.action == "put" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return []

    throttle_classes = [MyAnon, MyUser]

    # 局部过滤配置  高于全局过滤配置
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["name"]
    search_fields = ['name']
    ordering_fields = ['id']


class CoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializers
    filterset_fields = ["name"]


class CoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = CoodImgsSerializers



class UserViewSets(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    """
    声明用户资源类  获取个人信息  更新个人信息  删除账户
    扩展出action路由  用户操作  创建账户
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegistSerializer
        return UserSerializers


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


    def get_permissions(self):
        """
        超级管理员只可以展示所有订单
        普通用户  可以创建修改订单  不可以操作其他用户的订单
        :return:
        """
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or self.action == "retrieve" or self.action == "destroy":
            return [mypermissions.OrderPermissions()]
        else:
            return [permissions.IsAdminUser()]


class AdsViewSets(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializers

class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class RecommendViewSets(viewsets.ModelViewSet):
    queryset = Recommend.objects.all()
    serializer_class = RecommendSerializers

