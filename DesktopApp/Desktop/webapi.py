import requests
import os
import conf
import dashboard
import init_sql

get_id = 1

WEB_URL = f"https://icafeorder.pythonanywhere.com/menu/{get_id}/"
def start_user(user):

	pass

def api_info():
	global WEB_URL

	url=conf.WEB_API_URL+"info/"
	headers = {
		"Authorization":f"token {init_sql.get_token()}"
	}
	res = requests.get(url,headers=headers)
	data = res.json()
	WEB_URL = f"https://icafeorder.pythonanywhere.com/menu/{data['cafe']['id']}/"
	print(data)
	conf.BOT_TOKEN = data['cafe']['bot_token']
	dashboard.count_order.value = data['count_order']
	dashboard.total_sum.value = data['total_sum']
	dashboard.count_user.value = data['count_user']
	dashboard.count_product.value = data['count_product']
	dashboard.dashboard.update()

def api_categorys_get():
	url=conf.WEB_API_URL+"category/"
	headers = {
		"Authorization":f"token {init_sql.get_token()}"
	}
	res = requests.get(url,headers=headers)
	data = res.json()
	return data

def api_categorys_edit(id,name):
	url=conf.WEB_API_URL+f"category/{id}/"
	headers = {
		"Authorization":f"token {init_sql.get_token()}"
	}
	res = requests.patch(url,{"name":name},headers=headers)

def api_categorys_delete(id):
	url=conf.WEB_API_URL+f"category/{id}/"
	headers = {
		"Authorization":f"token {init_sql.get_token()}"
	}
	res = requests.delete(url,headers=headers)

def api_categorys_add(name):
	url=conf.WEB_API_URL+f"category/"
	headers = {
		"Authorization":f"token {init_sql.get_token()}"
	}
	res = requests.post(url,json={"name":name,"user":1},headers=headers)
	print(res.text)


def api_products_get():
	url=conf.WEB_API_URL+"product/"
	headers = {
		"Authorization":f"token {init_sql.get_token()}"
	}
	res = requests.get(url,headers=headers)
	data = res.json()
	return data

def api_products_add(name,image,category,price,about):
	url=conf.WEB_API_URL+f"product/"
	headers = {
		"Authorization":f"token {init_sql.get_token()}"
	}
	with open(image,'rb') as f:
		res = requests.post(url,files={'image':f},data={"name":name,"category":str(category),"price":price,"about":about},headers=headers)
		print(res.text)

def api_products_edit(id,name,image,category,price,about):
	print(image)
	url=conf.WEB_API_URL+f"product/{id}/"
	headers = {
		"Authorization":f"token {init_sql.get_token()}"
	}
	if image != None:
		with open(image,'rb') as f:
			res = requests.patch(url,files={'image':f},data={"name":name,"category":str(category),"price":price,"about":about},headers=headers)
	else:
		res = requests.patch(url,data={"name":name,"category":str(category),"price":price,"about":about},headers=headers)

	print(res.text)

def api_products_delete(id):
	url=conf.WEB_API_URL+f"product/{id}/"
	headers = {
		"Authorization":f"token {init_sql.get_token()}"
	}
	res = requests.delete(url,headers=headers)
