from django.conf.urls import url

from App.views import *

urlpatterns = [
	#zhuye
	url(r'^index/', index, name='index'),
	#lunbo
	url(r'^wheeldata/', wheel_data, name='wheel'),
	url(r'^maindata/', main_data, name='main'),
	url(r'^userdata/', user_data, name='user'),
	#user
    url(r'^register/', register, name='register'),
	url(r'^login/', login, name='login'),
	url(r'^logout/', logout, name='logout'),
	#detail
	url(r'^detail/', jump_to_detail, name='detail'),
	#cart
	url(r'^cart/', jump_to_cart, name='cart'),
	#order
	url(r'^order/', jump_to_order, name='order'),
	url(r'^pay/', jump_to_pay, name='pay'),
	url(r'^topay/', topay,name='topay'),
    url(r'^notify/', notify),
    url(r'^result/', result),
]