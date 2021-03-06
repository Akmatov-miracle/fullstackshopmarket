from rest_framework import serializers

from Products.models import Products, Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('id', 'title', 'image', 'description', 'category')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.children.exists():
            representation['children'] = CategorySerializer(instance=instance.children.all(), many=True).data
        return representation
