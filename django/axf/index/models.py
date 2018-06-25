from django.db import models


# Create your models here.
class Main(models.Model):
    img = models.CharField(max_length=200)  # 图片
    name = models.CharField(max_length=100)  # 名称
    trackid = models.CharField(max_length=15)  # 通用id

    class Meta:
        abstract = True  # 抽象父类


class MainWheel(Main):
    """轮播banner"""
    class Meta:
        db_table = 'axf_wheel'


class MainNav(Main):
    # 导航
    class Meta:
        db_table = 'axf_nav'


class MainHotGoods(Main):
    """热销商品"""
    class Meta:
        db_table = 'axf_hotgoods'


class MainShop(Main):
    class Meta:
        db_table = 'axf_shop'


class MainShow(Main):
    categoryid = models.CharField(max_length=16)
    brandename = models.CharField(max_length=100)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=16, null=True)
    productid1 = models.CharField(max_length=16, null=True)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField(default=0)
    marketprice1 = models.FloatField(default=1)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16, null=True)
    productid2 = models.CharField(max_length=16, null=True)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField(default=0)
    marketprice2 = models.FloatField(default=1)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16, null=True)
    productid3 = models.CharField(max_length=16, null=True)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField(default=0)
    marketprice3 = models.FloatField(default=1)

    class Meta:
        db_table = 'axf_show'


class FoodType(models.Model):
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_foodtype'


class Goods(models.Model):
    productid = models.CharField(max_length=16)  # 商品的id
    productimg = models.CharField(max_length=200)  # 商品的图片
    productname = models.CharField(max_length=100)  # 商品的名称
    productlongname = models.CharField(max_length=200)  # 商品额
    isxf = models.IntegerField(default=1)
    pmdesc = models.CharField(max_length=100)
    specifics = models.CharField(max_length=100)  # 商品的规格
    price = models.FloatField(default=0)  # 折后价格
    marketprice = models.FloatField(default=1)  # 商品的原价
    categoryid = models.CharField(max_length=16)  # 分类id
    childcid = models.CharField(max_length=16)  # 子分类id
    childcidname = models.CharField(max_length=100)  # 子分类id名字
    dealerid = models.CharField(max_length=16)
    storenums = models.CharField(max_length=1)  # 排序
    productnum = models.IntegerField(default=1)  # 销量排序

    class Meta:
        db_table = 'axf_goods'


class UserModel(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256) # 密码
    email = models.CharField(max_length=64, unique=True)
    sex = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='icons')
    is_delete = models.BooleanField(default=False)
    u_ticket = models.CharField(max_length=256, null=True)

    class Meta:
        db_table = 'axf_users'


# 购物车
class CartModel(models.Model):
    user = models.ForeignKey(UserModel, related_name='user_id')  # 关联用户
    goods = models.ForeignKey(Goods, related_name='goods_id')  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品的个数
    is_select = models.BooleanField(default=True)  # 是否选择商品

    class Meta:
        db_table = 'axf_cart'


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    o_num = models.CharField(max_length=64)  # 数量
    # 0 代表已下单， 但是未付款， 1已付款未发货， 2 已付款已发货
    o_status = models.IntegerField(default=0)  # 状态
    o_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'axf_order'


class OderGoodsModel(models.Model):
    goods = models.ForeignKey(Goods)  # 关联的商品
    order = models.ForeignKey(OrderModel)  # 关联的订单
    goods_num = models.IntegerField(default=1)  # 商品的个数

    class Meta:
        db_table = 'axf_order_goods'


class PassUtilsTimes(models.Model):
    p_times = models.IntegerField(max_length=1, default=0)

    class Meta:
        db_table = 'pass_utils_times'