# author sqz
# date 2020/2/26 16:19
# file_name serializers
from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    """
    编写针对Category 的序列化类
    本类指明了Category的序列化细节
    需要继承ModelSerializer 才可以针对模型进行序列化
    在Meta类中  model指明序列化的模型  fields指明序列化的字段
    """
    #goods 一定要和related_name的值一至
    #StringRelatedField可以显示关联模型中的__str__返回值  many=True代表多个对象  read_only=True代表只读
    goods=serializers.StringRelatedField(many=True)
    # goods=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # goods=serializers.HyperlinkedRelatedField(view_name='good-detail',read_only=True,many=True)
    class Meta:
        model = Category
        #__all__ 代表模型中的所有字段
        # fields = "__all__"
        fields = ('name','goods')

class GoodSerializers(serializers.ModelSerializer):

    #在序列化时指定字段  在多方  使用source=模型名.字段名   read_only=True表示不能更改
    category=serializers.CharField(source=('category.name'),read_only=True)
    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('name','desc','category')

