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
from .pagination import Mypagrnation
# 引入django过滤类
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(["GET"])
def getuserinfo(request):
    user=JWTAuthentication().authenticate(request)
    seria=UserSerializers(instance=user[0])
    return Response(seria.data,status=status.HTTP_200_OK)


# 升级版
class CategoryListView2(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetailView2(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.delete(request, pk)


# 基于类
class CategoryListView1(APIView):
    """
    继承Django本身自带的View类需要重写对应的Http方法
    继承DRF自带的APIView类即可完成请求响应的封装  APIView继承封装了Django的View
    """

    def get(self, request):
        # instance从数据库中取
        seria = CategorySerializers(instance=Category.objects.all(), many=True)
        return Response(seria.data, status=status.HTTP_200_OK)

    def post(self, request):
        # data从请求中取
        seria = CategorySerializers(data=request.data)
        # 第一种写法
        # if seria.is_valid():
        #     seria.save()
        #     return Response(seria.data)
        # else:
        #     return Response(seria.data)
        # 第二种写法
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)


class CategoryDetailView1(APIView):
    def get(self, request, cid):
        seria = CategorySerializers(instance=get_object_or_404(Category, pk=cid))
        return Response(seria.data, status=status.HTTP_200_OK)

    def put(self, request, cid):
        seria = CategorySerializers(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_200_OK)

    def patch(self, request, cid):
        seria = CategorySerializers(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_200_OK)

    def delete(self, request, cid):
        get_object_or_404(Category, pk=cid).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 基于函数
@api_view(["GET", "POST"])
def categoryList(request):
    print(request, type(request))
    if request.method == "GET":
        # queryset=Category.objects.all()
        # instance为需要序列化的对象   来源于数据库
        seria = CategorySerializers(instance=Category.objects.all(), many=True)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # data为序列化对象   来源于请求中提取的数据
        seria = CategorySerializers(data=request.data)
        # 从请求中提取的数据序列化之前需要进行校验
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status.HTTP_201_CREATED)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def categoryDetail(request, cid):
    model = get_object_or_404(Category, pk=cid)
    if request.method == "GET":
        seria = CategorySerializers(model)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        # 更新就是从请求中提取数据  替换掉数据库中取出的数据
        seria = CategorySerializers(instance=model, data=request.data)
        # 验证是否合法
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse("当前路由不允许" + request.method + "操作")


# 顶级版
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryViewSets2(viewsets.ModelViewSet):
    """
    如果返回的内容是模型列表  用queryset方便
    如果需要处理  可以使用basename结合get_queryset
    """
    queryset = Category.objects.all()

    # def get_queryset(self):
    #     return Category.objects.all()[:3]

    # serializer_class = CategorySerializers
    def get_serializer_class(self):
        return CategorySerializers

    @action(methods=['GET'], detail=False)
    def getlatestcategory(self, request):
        seria = CategorySerializers(instance=Category.objects.all()[:int(request.query_params.get("num"))], many=True)
        return Response(data=seria.data, status=status.HTTP_200_OK)


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

    # 2.通过方法指明
    # def get_serializer_class(self):
    #     return CategorySerializers

    # 用户为登录不显示 分类列表  优先级别高于全局配置
    # permission_classes = [permissions.IsAdminUser]

    # 超级管理员可以创建分类  普通用户可以查看分类
    def get_permissions(self):
        if self.action == "create" or self.action == "put" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return []

    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    throttle_classes = [MyAnon, MyUser]
    # pagination_class = Mypagrnation

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


class UserViewSets1(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """
    声明用户资源类  获取个人信息  更新个人信息  删除账户
    扩展出action路由  用户操作  创建账户
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers

    # 使用action扩展资源http方法
    @action(methods=["POST"], detail=False)
    def regist(self, request):
        seria = UserRegistSerializer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)


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

    # permission_classes = [permissions.OrderPermissions]

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

# http方法                          混合类关键字                   action关键字
# GET列表                           List                          get
# POST创建对象                       Create                       create
# GET 单个对象                       Retrieve                     retrieve
# PUT 修改对象提供全属性              Update                       update
# PATCH 修改对象提供部分属性          Update                       partial_update
# DELETE 删除对象                    Destroy                      destroy
