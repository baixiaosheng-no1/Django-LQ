import json
import codecs

with open('D:\qf\Python\Django\Project\SHOP\App\static\json\loor.json',encoding='utf8') as f:
	json_reader = json.load(f)
	# print(json_reader)
	
str = "\r\n"
# for item in json_reader:
#
# 	print(item) # {}
# 	str = str + "insert into lq_wheel(id,img) values "
# 	str = str + "('%s','%s');\r\n" % (item['id'],item['img'])

for list in json_reader:
	# print(list)
	for list1 in list:
		# print(list1)
		for item in list1:
			print(item)
			# str = str + "insert into lq_other(id,img,price,concent) values "
			# str = str + "('%s','%s','%s','%s');\r\n" %(item['id'],item['img'],item['price'],item['concent'])
			str = str + "insert into lq_goods(id,img,img1,img2,img3,img4,img5,img6,price,concent,concent1,concent2,concent3,concent4,concent5) values "
			str = str + "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');\r\n" %(item['id'],item['img'],item['img1'],item['img2'],item['img3'],item['img4'],item['img5'],item['img6'],item['price'],item['concent'],item['concent1'],item['concent2'],item['concent3'],item['concent4'],item['concent5'])
file_object = codecs.open('goods.sql', 'w', "utf8")
file_object.write(str)
file_object.close()
print("success")



