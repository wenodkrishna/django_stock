from django.shortcuts import render,redirect
from .models import stock
from django.contrib import messages
from.forms import stockform


def home(request):
	import requests
	import json
	#pk_edf48937653f40e5949b2c69d841c411


	if request.method == "POST":
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + " /quote?token=pk_edf48937653f40e5949b2c69d841c411")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "error"
		return render(request,'home.html',{"api":api})


	else:
		return render(request,'home.html',{'ticker':"enter a ticker symbol above..."})
	
	


def about(request):
	return render(request,'about.html',{})


def add_stock(request):
	import requests
	import json
	if request.method == "POST":
		form=stockform(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request,("stock has been added successfully"))
			return redirect('add_stock')
	else:
		ticker = stock.objects.all()
		output=[]
		for ticker_item in ticker:
			api_request = requests.get(
				"https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_edf48937653f40e5949b2c69d841c411")

			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "error"

		return render(request,'add_stock.html',{'ticker':ticker,'output':output})

def delete(request,stock_id):
	item =stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request,("stock has been deleted"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker':ticker})





	'''api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_edf48937653f40e5949b2c69d841c411")

	try:
		api = json.loads(api_request.content)


	except Exception as e:
		api = "error"

	return render(request,'home.html',{'api': api})'''
	#api_request = requests.get(
	#			"https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + " /quote?token=pk_edf48937653f40e5949b2c69d841c411")