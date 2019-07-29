
import random

import time
from django.shortcuts import render, redirect,reverse
from App.alipay import AliPay
from App.models import *
from django.http import JsonResponse, HttpResponse

'''
*******************************
         用户
*******************************
'''
#zhuye
def index(request):
	
	return render(request,'zhuye.html')
	
#register
def register(request):
	if request.method == 'GET':
		return render(request, 'zhuce.html')
	
	if request.method == 'POST':
		# 接收前端提交过来的数据
		# value = request.POST.get(name)
		username = request.POST.get('username')
		psd = request.POST.get('pwd1')
		
		# 检查用户名是否已存在
		is_exist = User.objects.filter(name=username).exists()
		if is_exist:
			#如果存在
			return render(request, 'zhuce.html')
		#如果不存在
		# 注册
		user = User()
		user.name = username
		user.psd = psd
		user.save()
		# 注册成功后，自动登录，并跳转到主页
		request.session['user_id'] = user.id
		return redirect(reverse('App:login'))


#login
def login(request):
	
	return render(request, 'denglu.html')
	
		
#logout
def logout(request):
	del request.session['user_name']
	request.session.flush()
	return redirect(reverse('App:index'))

'''
*******************************
         商品详情页
*******************************
'''
def jump_to_detail(request):
	
	return render(request,'spxq.html')
	

'''
*******************************
    购物车/填写订单/订单详情
*******************************
'''
def jump_to_cart(request):
	
	return render(request,'gouwuche.html')

def jump_to_order(request):
	
	return render(request, 'order.html')

def jump_to_pay(request):
	
	if request.method == 'GET':
		return render(request,'order.html')
	
	if request.method == 'POST':
		print('hello')
		get_user = request.POST.get('get_user')
		send_address = request.POST.get('address')
		order_pay = request.POST.get('total_price')
		
		data = {
				'order_time': ran_date2(),
				'order_num': str(ran_date())+str(random_num()),
				'get_user':get_user,
				'send_address':send_address,
				'order_pay':order_pay
		}
		
		#添加订单
		order = OrderModel()
		order.order_time=ran_date2()
		order.order_num = str(ran_date())+str(random_num())
		order.get_user =get_user
		order.send_address = send_address
		order.order_pay = order_pay
		order.save()
		
		order= OrderModel.objects.filter(order_time=order.order_time).last()
		print(order.id)
		return render(request,'pay.html',data,{'order':order})

'''
*******************************
         返回json数据
*******************************
'''
#lunbo
def wheel_data(request):
	wheels = WheelModel.objects.all().values()
	# print(wheels)
	data = list(wheels)
	print(data)
	return JsonResponse({
		'data': data,
		'msg': '获取图片成功'
	})

#楼层floor
def main_data(request):
	
	res = []
	lis1 = []
	pros = ProModel.objects.all().values()
	prolis = list(pros)
	lis1.append(prolis)
	lis2 = []
	others = OtherPro.objects.all().values()
	otherlis = list(others)
	temp = func(otherlis, 6)
	for i in temp:
		# print(i)
		lis2.append(i)
		lis = lis1 + lis2
	# 	# print(lis) #[[],[],[]]
	temp1 = func(lis, 5)
	for s in temp1:
# 		print(s)  #[[],[],[],[],[]],[[],[],[],[],[]]
		res.append(s)
		# print(res)
		
		# with open('1.json', 'w',encoding='utf8') as wf:
		# 	json.dump(res, wf)
		# 	print('ok')
	return JsonResponse({
		'data': res,
		'msg': '获取图片成功'
	})


#userdata
def user_data(request):
	users = User.objects.all().values()
	data = list(users)
	# print(data)
	return JsonResponse({
		'data': data,
		'msg': '获取用户成功'
	})
	

'''
*******************************
            支付宝
*******************************
'''
# 支付
def topay(request):
	#得到新添加的订单
	order = OrderModel.objects.all().last()
	# print(str(order.order_num))
	alipay= AliPay(
        appid="2016100100640327",  # 设置签约的appid
        app_notify_url="http://127.0.0.1:8000/notify/",  # "http://projectsedus.com/",  # 异步支付通知url
        app_private_key_path=r"App/ying_yong_si_yao.txt",  # 设置应用私钥
        alipay_public_key_path=r"App/zhi_fu_bao_gong_yao.txt",  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=True,  # 默认False,            # 设置是否是沙箱环境，True是沙箱环境
        return_url="http://127.0.0.1:8000/result/",  # "http://47.92.87.172:8000/"  # 同步支付通知url
    )

	# 传递参数执行支付类里的direct_pay方法，返回签名后的支付参数，
	url = alipay.direct_pay(
        subject="购物",  # 订单名称
        # 订单号生成，一般是当前时间(精确到秒)+用户ID+随机数
        out_trade_no=order.order_num,  # 订单号
        total_amount=order.order_pay, # 支付金额
        return_url="http://127.0.0.1:8000/result/"  # 支付成功后，跳转url
    )

	# 将前面后的支付参数，拼接到支付网关
    # 注意：下面支付网关是沙箱环境，最终进行签名后组合成支付宝的url请求
	re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
	# print(re_url)
	data = {'re_url': re_url}
	return JsonResponse(data)
	


# 异步支付通知url (上线后使用)
def notify(request):
	
	print("notify:", dict(request.GET))
	return HttpResponse("支付成功:%s" % (dict(request.GET)))


# 付款成功后跳转的url
def result(request):
	print("result:", dict(request.GET))

	# 支付成功后，将对应订单的状态改为：1 已支付

	return HttpResponse("支付成功:%s" % (dict(request.GET)))
'''
*******************************
            辅助功能
*******************************
'''
#列表均分
def func(listTemp, n):
	for i in range(0, len(listTemp), n):
		yield listTemp[i:i + n]

# # 加密
# def my_md5(s):
# 	m = hashlib.md5()
# 	m.update(s.encode())
# 	return m.hexdigest()

#创建函数后必须被调用才能执行
#如以下函数中的print(num)结果，必须要先调用random_num()函数
def random_num():
	j = 5
	
	num = []
	num = ''.join(str(i) for i in random.sample(range(0,9),j))    # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
	print(num)
	return num

	
def ran_date():
	
	sd = time.localtime()
	st = time.strftime('%Y%m%d', sd)
	# str_st = str(st)
	return st

def ran_date2():
	sdd = datetime.now()
	stt = sdd.strftime('%Y-%m-%d %H:%M:%S %A')
	# print(stt)
	#2019-07-27 15:05:02 Saturday
	return stt
	