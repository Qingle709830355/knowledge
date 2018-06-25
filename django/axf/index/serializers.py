from rest_framework import serializers
from index.models import CartModel, Goods, UserModel


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = ('id', 'c_num', 'is_select', 'goods', 'user')

    # def create(self, validated_data):
    #     cart = CartModel(
    #         goods_id=validated_data['goods_id'],
    #         user_id=validated_data['user_id']
    #     )
    #     cart.save()
    #     return cart

