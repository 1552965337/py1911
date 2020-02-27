# author sqz
# date 2020/2/26 16:19
# file_name serializers
from rest_framework import serializers
from .models import *

class CategorySerializers(serializers.Serializer):
    """
    序列化类   决定了模型序列化细节
    """
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=10,min_length=3,error_messages={
        "max_length":"最多10个字",
        "min_length": "最少3个字"
    })

    def create(self, validated_data):
        #通过重写create方法  来定义模型创建方式
        print("重写创建方法",validated_data)
        instace=Category.objects.create(**validated_data)
        print("创建模型实例",instace)
        return instace
    def update(self, instance, validated_data):
        """
        通过重写update  来定义模型的更新方法
        :param instance: 改之前的实例
        :param validated_data: 更改参数
        :return: 返回的新实例
        """
        print("重写更新方法",validated_data,instance.name)
        instance.name=validated_data.get("name",instance.name)
        print(instance.name)
        instance.save()
        return instance


class CoodImgsSerializers(serializers.Serializer):
    img=serializers.ImageField()
    good=serializers.CharField(source='good.name')

    # def validate_good(self, data):
    #     try:
    #         g=Good.objects.get(name=data['name'])
    #         return g
    #     except:
    #         raise serializers.ValidationError("输入的商品不存在")
    #     return data

    def validate(self, attrs):
        try:
            g=Good.objects.get(name=attrs['good']['name'])
            attrs['good']=g
        except:
            raise serializers.ValidationError('商品不存在')
        return attrs

    def create(self, validated_data):
        instance=GoodImgs.objects.create(**validated_data)
        return instance



class GoodSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最多20个字",
        "min_length": "最少2个字"
    })
    category=CategorySerializers(label="分类")
    imgs=CoodImgsSerializers(label="图片",many=True,read_only=True)

    def validate_category(self,category):
        """
        处理category
        :param category: 处理的原始值
        :return:返回新值
        """
        try:
            Category.objects.get(name=category["name"])
        except:
            raise serializers.ValidationError("输入的分类名不存在")
        return category

    def validate(self, attrs):
        print("收到的数据为",attrs)
        try:
            c=Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name=attrs["category"]["name"])

        attrs["category"]=c
        return attrs

    def create(self,validated_data):
        print("创建good参数",validated_data)
        instace=Good.objects.create(**validated_data)
        return instace

    def update(self,instance,validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.category=validated_data.get("category",instance.category)
        instance.save()
        return instance

class GoodSerializers1(serializers.ModelSerializer):

    #在序列化时指定字段  在多方  使用source=模型名.字段名
    # read_only=True表示不能更改(get显示  update不显示)
    #write_only=True标识只能更改(get不显示  update显示)
    category=serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('id','name','desc','category')


class CustomSerializers(serializers.RelatedField):
    """
    自定义序列化类
    """
    def to_representation(self, value):
        """
        重写对象的输出格式
        :param value: 需要序列化的对象
        :return: 显示的格式
        """
        return str(value.id)+"--"+value.name+'--'+value.desc





class CategorySerializers1(serializers.ModelSerializer):
    """
    编写针对Category 的序列化类
    本类指明了Category的序列化细节
    需要继承ModelSerializer 才可以针对模型进行序列化
    在Meta类中  model指明序列化的模型  fields指明序列化的字段
    """
    #goods 一定要和related_name的值一至
    #StringRelatedField可以显示关联模型中的__str__返回值  many=True代表多个对象  read_only=True代表只读
    # goods=serializers.StringRelatedField(many=True)

    #PrimaryKeyRelatedField显示主键值
    # goods=serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    #显示资源RestFulAPI
    # goods=serializers.HyperlinkedRelatedField(view_name='good-detail',read_only=True,many=True)

    #自定义序列化类
    goods=CustomSerializers(many=True,read_only=True)

    # goods=GoodSerializers(many=True,read_only=True)

    class Meta:
        model = Category
        #__all__ 代表模型中的所有字段
        # fields = "__all__"
        fields = ('id','name','goods')


