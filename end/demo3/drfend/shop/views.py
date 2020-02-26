from rest_framework import viewsets
from .models import *
from .serializers import *

class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 之后拥有GET  POST  PUT PATCH  DELETE等HTTP动词操作
    queryset 指明需要操作的模型列表
    serializer_class 指明序列化类
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializers