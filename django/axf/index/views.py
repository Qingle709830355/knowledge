from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import mixins, viewsets
from django.core import serializers
from django.core.urlresolvers import reverse

from index.models import MainWheel, MainNav, MainHotGoods, \
    MainShop, Goods, MainShow, UserModel,FoodType, CartModel, \
    OrderModel, OderGoodsModel
from index.serializers import CartSerializer
from index.filters import CartFilter


# Create your views here.
def home(request):
    if request.method == 'GET':
        wheels = MainWheel.objects.all()
        navs = MainNav.objects.all()
        hotgoods = MainHotGoods.objects.all()
        shops = MainShop.objects.all()
        shows = MainShow.objects.all()
        return render(request, 'home/home.html',
                      {'wheels': wheels,
                       'navs': navs,
                       'hotgoods': hotgoods,
                       # 'shop1': shops[0],
                       # 'shop2to3': shops[1:3],
                       # 'shop4to7': shops[3:7],
                       # 'shop8to11': shops[7:11],
                       'shops': shops,
                       'shows': shows})


def mine(request):
    """我的页面"""
    if request.method == 'GET':
        wait_pay, payed, commit = 0, 0, 0
        ticket = request.COOKIES.get('ticket')
        if ticket:
            users = UserModel.objects.filter(u_ticket=ticket)
            if users:
                orders = users[0].ordermodel_set.all()
                for order in orders:
                    if order.o_status == 0:
                        wait_pay += 1
                    if order.o_status == 1:
                        payed += 1
                    if order.o_status == 2:
                        commit += 1
                data = {
                    'wait': wait_pay,
                    'payed': payed,
                    'commit': commit
                }
                return render(request, 'mine/mine.html', {'users': users[0], 'data': data})
            else:
                return render(request, 'mine/mine.html')
        else:
            return render(request, 'mine/mine.html')


def market(request):
    """闪购"""
    if request.method == 'GET':
        foodtypes = FoodType.objects.all()
        goods = Goods.objects.filter(categoryid=104749).order_by('id')
        start_foodtype = FoodType.objects.get(typeid=104749)
        foodchildnames = start_foodtype.childtypenames
        listnames = change_to_dict(foodchildnames)
        return render(request, 'market/market.html', {'foodtypes': foodtypes,
                                                      'goods': goods,
                                                      'listnames': listnames})


def change_to_dict(foodchildnames):
    """将字符串转化为字典"""
    childnames = foodchildnames.split('#')  # 将字符串转化成列表形式
    listnames = []
    for childname in childnames:
        dictnames = {}
        childname = childname.split(':')
        dictnames['childname'] = childname[0]
        dictnames['id'] = childname[1]
        listnames.append(dictnames)
    return listnames


def typeid_group_goods(request):
    """按照typeid进行分类"""
    if request.method == 'GET':
        data = {
            'msg': '请求成功！',
            'coding': 200,
        }
        listgoods = []
        typeid = request.GET.get('typeid')
        foodchildnames = FoodType.objects.get(typeid=typeid).childtypenames
        listnames = change_to_dict(foodchildnames)
        data['listnames'] = listnames
        goods = Goods.objects.filter(categoryid=typeid)
        for good in goods:
            dict1 = {}
            dict1['id'] = good.id
            dict1['productimg'] = good.productimg
            dict1['productlongname'] = good.productlongname
            dict1['price'] = good.price
            dict1['marketprice'] = good.marketprice
            listgoods.append(dict1)
        data['goods'] = listgoods
        return JsonResponse(data)


def show_aready_choice(request):
    """在闪购页面展示已经选择好的商品个数"""
    if request.method == 'GET':
        data = {
            'msg': '请求成功！',
            'coding': 200,
        }
        cartslist = []
        user = request.user
        if user and user.id:
            carts = CartModel.objects.filter(user_id=user.id)
            for cart in carts:
                dict1 = {}
                dict1['good_id'] = cart.goods.id
                dict1['c_num'] = cart.c_num
                cartslist.append(dict1)

            data['data'] = cartslist

            return JsonResponse(data)


def childid_choice(request):
    if request.method == 'GET':
        data = {
            'message': '请求成功！',
            'coding': 200
        }
        listgoods = []
        childid = request.GET.get('childid')
        typeid = request.GET.get('typeid')
        type = request.GET.get('type')
        if childid == '0':
            goods = Goods.objects.filter(categoryid=int(typeid))
        else:
            goods = Goods.objects.filter(childcid=int(childid))
        foodchildnames = FoodType.objects.get(typeid=int(typeid)).childtypenames
        listnames = change_to_dict(foodchildnames)
        data['listnames'] = listnames

        if type == '1':
            goods = goods.order_by('id')
        if type == '2':
            goods = goods.order_by('productnum')
        if type == '3':
            goods = goods.order_by('price')
        if type == '4':
            goods = goods.order_by('-price')

        for good in goods:
            dict1 = {}
            dict1['id'] = good.id
            dict1['productimg'] = good.productimg
            dict1['productlongname'] = good.productlongname
            dict1['price'] = good.price
            dict1['marketprice'] = good.marketprice
            listgoods.append(dict1)
        data['goods'] = listgoods
        return JsonResponse(data)


def cart(request):
    """购物车"""
    if request.method == 'GET':
        user = request.user
        if user:
            user_id = user.id
            carts, total = calc_total(user_id)
        return render(request, 'cart/cart.html', {'carts': carts, 'total': total})


def calc_total(userid):
    carts = CartModel.objects.filter(user_id=userid)
    total = 0
    for cart in carts:
        if cart.is_select:
            total += (cart.goods.price * cart.c_num)
        total = float('%.2f' % total)
    return carts, total


class CartEditor(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):
    # 查询所有cart
    queryset = CartModel.objects.all()
    # 序列化
    serializer_class = CartSerializer
    # 过滤器
    filter_class = CartFilter


def add_cart(request):
    listdata = []

    data = {
        'msg': '请求成功！',
        'coding': 200,
    }
    if request.method == 'GET':
        carts = CartModel.objects.all()
        for cart in carts:
            dict1 = {}
            dict1['c_num'] = cart.c_num
            dict1['goods_id'] = cart.goods_id
            dict1['user_id'] = cart.user_id
            listdata.append(dict1)
        data['data'] = listdata
        return JsonResponse(data)

    if request.method == 'POST':

        user = request.user
        if user and user.id:
            goodsid = request.POST.get('goods')
            cart = CartModel.objects.filter(goods_id=goodsid, user_id=user.id).first()
            if cart:
                cart.c_num += 1
                cart.save()
            else:
                CartModel.objects.create(
                    goods_id=goodsid,
                    user_id=user.id
                )
            data['c_num'] = CartModel.objects.filter(goods_id=goodsid, user_id=user.id).first().c_num
            data['total'] = calc_total(user.id)[1]
        return JsonResponse(data)


def sub_car(request):
    if request.method == 'POST':
        data = {
            'msg': '请求成功',
            'coding': 200,
        }
        good_id = request.POST.get('goods')
        user = request.user
        if user and user.id:
            cart = CartModel.objects.filter(goods_id=good_id, user_id=user.id).first()
            if cart:
                if cart.c_num > 1:
                    cart.c_num -= 1
                    cart.save()
                    data['c_num'] = cart.c_num
                else:
                    cart.delete()
                    data['c_num'] = 0
                data['total'] = calc_total(user.id)[1]
        return JsonResponse(data)


def change_cart_status(request):
    if request.method == 'POST':
        data = {
            'msg': '请求成功！',
            'coding': 200,
        }
        id = request.POST.get('id')
        l = request.POST.get('l')
        user = request.user
        if user and user.id:
            cart = CartModel.objects.get(id=id)
            is_select = cart.is_select
            cart.is_select = not cart.is_select
            cart.save()
            data['is_select'] = cart.is_select
            carts = CartModel.objects.filter(user_id=user.id)
            if (len(carts) - int(l)) == 1 and not is_select:
                data['is_all'] = True
            else:
                data['is_all'] = False
            data['total'] = calc_total(user.id)[1]
        return JsonResponse(data)


def is_select_all(request):
    if request.method == 'POST':
        data = {
            'msg': '请求成功！',
            'coding': 200,
        }
        user = request.user
        l = request.POST.get('len')
        is_all = request.POST.get('is_all')
        if user and user.id:
            carts = CartModel.objects.filter(user_id=user.id)
            if not is_all:
                if len(carts) == int(l):
                    data['is_all'] = True
                else:
                    data['is_all'] = False

            elif is_all == 'True':
                for cart in carts:
                    cart.is_select = False
                    cart.save()
                    data['is_all'] = False
            else:
                for cart in carts:
                    cart.is_select = True
                    cart.save()
                    data['is_all'] = True

            data['total'] = calc_total(user.id)[1]
        return JsonResponse(data)


def create_order(request):
    """生成一个订单并删除购物车中选择的商品"""
    if request.method == 'GET':
        user = request.user
        if user and user.id:
            carts = CartModel.objects.filter(user_id=user.id, is_select=True)
            if len(carts) <= 0:
                return render(request, 'cart/cart.html', {'message': '您未选择商品！'})
            order = OrderModel.objects.create(
                o_num=len(carts),
                user_id=user.id
            )
            for cart in carts:
                OderGoodsModel.objects.create(
                    goods_id=cart.goods.id, order_id=order.id, goods_num=cart.c_num
                )
                cart.delete()
            return HttpResponseRedirect(reverse('axf:topay', args=(order.id, )))


def to_pay(request, order_id):
    """去付款"""
    ordergoods = OderGoodsModel.objects.filter(order_id=order_id)
    return render(request, 'order/order_info.html', {'ordergoods': ordergoods, 'order_id': order_id})


def paying(request):
    """支付"""
    if request.method == 'GET':
        order_id = request.GET.get('order_id')
        order = OrderModel.objects.get(id=order_id)
        order.o_status = 1
        order.save()
        return HttpResponseRedirect('/axf/mine/')


def to_wait_pay(request):
    """跳转到未付款页面"""
    if request.method == 'GET':
        user = request.user
        if user and user.id:
            orders = OrderModel.objects.filter(user_id=user.id, o_status=0)
            return render(request, 'order/order_list_wait_pay.html', {'orders': orders})


def payed(request):
    """跳转到待收货页面"""
    if request.method == 'GET':
        user = request.user
        if user and user.id:
            orders = OrderModel.objects.filter(user_id=user.id, o_status=1)
            return render(request, 'order/order_list_payed.html', {'orders': orders})


def sure_collect(request):
    """确认收货"""
    if request.method == 'GET':
        order_id = request.GET.get('order_id')
        order = OrderModel.objects.get(id=order_id)
        order.o_status = 2
        order.save()
        return HttpResponseRedirect('/axf/mine/')


