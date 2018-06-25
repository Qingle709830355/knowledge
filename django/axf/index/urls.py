from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from index import views

router = SimpleRouter()
router.register('shopcar', views.CartEditor)


urlpatterns = [
    url(r'home/', views.home, name='home'),
    url(r'market/', views.market, name='market'),
    url(r'cart/', views.cart, name='cart'),
    url(r'mine/', views.mine, name='mine'),
    url(r'addcar/', views.add_cart),
    url(r'subcar/', views.sub_car),
    url(r'changecartstatus/', views.change_cart_status),
    url(r'isselectall/', views.is_select_all),
    url(r'createorder/', views.create_order),
    url(r'topay/(\d+)/', views.to_pay, name='topay'),
    url(r'paying/', views.paying),
    url(r'towaitpay/', views.to_wait_pay),
    url(r'payed/', views.payed),
    url(r'surecollect/', views.sure_collect),
    url(r'showareadychoice/', views.show_aready_choice),
    url(r'typeidchoice/', views.typeid_group_goods),
    url(r'childidchoice/', views.childid_choice)
] + router.urls