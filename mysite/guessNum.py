#coding:utf-8

# name=input('please input name: ').strip()
# passwd=input('please input password: ').strip()
# email=input('please input email: ').strip()
# while True:
#     if name=="q" or name=="Q":
#         break
#     else:
#         len(name)>20
#         name=name[:20]
#         print("%-40s,%-40s,%-40s" %(name,passwd,email))
#     name=input('please input name: ').strip()
#     passwd=input('please input password: ').strip()
#     email=input('please input email: ').strip()

# while not (name=="q" or name=="Q"):
#     if len(name)>20:
#         name=name[:20]
#     print("%-40s,%-40s,%-40s" %(name,passwd,email))
#     name=input('please input name: ').strip()
#     passwd=input('please input password: ').strip()
#     email=input('please input email: ').strip()

# for i in range(1,4):
# 	name=input("please input name: ").strip()
# 	passwd=input("please input password: ").strip()
# 	if name=='lilei' and passwd=='123456':
# 		break


# with open('/Users/oupeng/Documents/myrecords/py/pythonCourse/diffEncode.txt',encoding='utf-8') as f:
# 	for one in f.readlines():
# 		print(one)


# apple 10 3tee 20 20pear 30 5




#coding:utf8
resList=[]
with open(file='orig.txt',mode='r+',encoding='utf8') as f:
	for one in f.readlines():
		tempDict={}
		name,num,price=one.strip().split(" ")
		tempDict['name']=name
		tempDict['num']=num
		tempDict['price']=price
		resList.append(tempDict)
print(resList)
totalPrice=0
for one in resList:
	totalPrice+=int(one['num'])*int(one['price'])
print(totalPrice)
