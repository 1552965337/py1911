from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse

# 通过api_view装饰器可以将基于函数的视图转换成APIVIew基于类的视图
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

#升级版
class CategoryListView2(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
class CategoryDetailView2(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin):
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


#顶级版
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryViewSets2(viewsets.ModelViewSet):
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
    # 2.通过方法指明
    # def get_serializer_class(self):
    #     return CategorySerializers


class CoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializers


class CoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = CoodImgsSerializers
