# author sqz
# date 2020/2/26 16:19
# file_name serializers
from rest_framework import serializers
from .models import *

class CoodImgsSerializers(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')


    def validate(self, attrs):
        try:
            g = Good.objects.get(name=attrs['good']['name'])
            attrs['good'] = g
        except:
            raise serializers.ValidationError('商品不存在')
        return attrs

    def create(self, validated_data):
        instance = GoodImgs.objects.create(**validated_data)
        return instance


class GoodSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最多20个字",
        "min_length": "最少2个字"
    })
    desc=serializers.CharField()
    price=serializers.FloatField()
    historyprice=serializers.FloatField()
    num=serializers.IntegerField()
    imgs = CoodImgsSerializers(label="图片", many=True, read_only=True)
    def validate_category(self, category):
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
        print("收到的数据为", attrs)
        try:
            c = Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name=attrs["category"]["name"])

        attrs["category"] = c
        return attrs

    def create(self, validated_data):
        print("创建good参数", validated_data)
        instace = Good.objects.create(**validated_data)
        return instace

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance



class CategorySerializers(serializers.Serializer):
    """
    序列化类   决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=3, error_messages={
        "max_length": "最多10个字",
        "min_length": "最少3个字"
    })
    goods=GoodSerializers(many=True,read_only=True)

    def create(self, validated_data):
        # 通过重写create方法  来定义模型创建方式
        print("重写创建方法", validated_data)
        instace = Category.objects.create(**validated_data)
        print("创建模型实例", instace)
        return instace

    def update(self, instance, validated_data):
        """
        通过重写update  来定义模型的更新方法
        :param instance: 改之前的实例
        :param validated_data: 更改参数
        :return: 返回的新实例
        """
        print("重写更新方法", validated_data, instance.name)
        instance.name = validated_data.get("name", instance.name)
        print(instance.name)
        instance.save()
        return instance





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
        return str(value.id) + "--" + value.name + '--' + value.desc




class UserSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ["user_permissions", "groups"]

    def validate(self, attrs):
        print("原生创建",attrs)
        from django.contrib.auth import hashers
        if attrs.get("password"):
            attrs["password"] = hashers.make_password(attrs["password"])
        return attrs


class UserRegistSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10, min_length=3, error_messages={
        "required": "用户名必填"
    })
    password = serializers.CharField(max_length=10, min_length=3, write_only=True)
    password2 = serializers.CharField(max_length=10, min_length=3, write_only=True)

    def validate_password2(self, data):
        if data != self.initial_data["password"]:
            raise serializers.ValidationError("密码不一致")
        else:
            return data

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data.get('username'), email=validated_data.get('email'),
                                        password=validated_data.get('password'))


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class AdsSerializers(serializers.ModelSerializer):
    img = serializers.ImageField()

    def create(self, validated_data):
        instance =Ads.objects.create(**validated_data)
        return instance
    class Meta:
        model = Ads
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    img = serializers.ImageField()
    def create(self, validated_data):
        instance =Product.objects.create(**validated_data)
        return instance
    class Meta:
        model = Product
        fields = '__all__'


class RecommendSerializers(serializers.ModelSerializer):
    img = serializers.ImageField()

    def create(self, validated_data):
        instance =Recommend.objects.create(**validated_data)
        return instance
    class Meta:
        model = Recommend
        fields = '__all__'