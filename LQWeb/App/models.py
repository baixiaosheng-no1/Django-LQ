from datetime import datetime

from django.db import models

#user
class User(models.Model):
	name = models.CharField(max_length=10,unique=True)
	psd = models.CharField(max_length=100)
	is_delete = models.BooleanField(default=False)
	class Meta:
		db_table = 'lq_user'

#lunbo
class WheelModel(models.Model):
	id = models.AutoField(primary_key=True)
	img = models.CharField(max_length=255)
	class Meta:
		db_table = 'lq_wheel'

#产品模型
#其他产品模型
class OtherPro(models.Model):
	id = models.AutoField(primary_key=True)
	img = models.CharField(max_length=255)
	price = models.FloatField()
	concent = models.CharField(max_length=100)
	class Meta:
		db_table = 'lq_Other'
	
#详情产品模型
class ProModel(models.Model):
	id = models.AutoField(primary_key=True)
	img = models.CharField(max_length=255)
	img1 = models.CharField(max_length=255)
	img2 = models.CharField(max_length=255)
	img3 = models.CharField(max_length=255)
	img4 = models.CharField(max_length=255)
	img5 = models.CharField(max_length=255)
	img6 = models.CharField(max_length=255)
	price = models.FloatField()
	concent = models.CharField(max_length=100)
	concent1 = models.CharField(max_length=100)
	concent2 = models.CharField(max_length=100)
	concent3 = models.CharField(max_length=100)
	concent4 = models.CharField(max_length=100)
	concent5 = models.CharField(max_length=100)
	
	class Meta:
		db_table = 'lq_pro'



#中间表cart
#cart-user（多对一）
#cart-product(一对多)
class Cart(models.Model):
	user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)  # 用户
	goods = models.ForeignKey(ProModel,on_delete=models.SET_NULL,null=True)  # 商品
	ber = models.IntegerField(default=1)  # 商品数量
	is_select = models.BooleanField(default=True)
	class Meta:
		db_table = 'lq_cart'
		
		
class Cart2(models.Model):
	img = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	ber = models.IntegerField(default=1)
	price = models.FloatField()
	sp = models.FloatField()
	
	class Meta:
		db_table = 'lq_cart2'

class OrderModel(models.Model):
	#下单时间
	order_time = models.CharField(max_length=100)
	#订单号
	order_num = models.CharField(max_length=300)
	#收件人
	get_user = models.CharField(max_length=100)
	#发送地址
	send_address = models.CharField(max_length=200)
	order_pay = models.CharField(max_length=10,default=0)
	class Meta:
		db_table = 'lq_order'