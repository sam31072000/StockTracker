from django.http.response import HttpResponse
from django.shortcuts import render
from yahoo_fin.stock_info import *
# Create your views here.
def stockPicker(request):
    stock_picker = tickers_nifty50()  #to fetch stocks present in nifty
    print(stock_picker)
    return render(request, 'mainapp/stockpicker.html', {'stockpicker':stock_picker}) #sending list of available stocks to frontend

def stockTracker(request):
    is_loginned = await checkAuthenticated(request)
    if not is_loginned:
        return HttpResponse("Login First")
    stockpicker = request.GET.getlist('stockpicker') #to get list of selected stocks
    print(stockpicker)
    data = {}
    available_stocks = tickers_nifty50() #avalable stocks in nifty
    for i in stockpicker:
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Error")
    
    for i in stockpicker:
        result = get_quote_table(i)  #this function used to request data of each stock from yahoo fin library
        data.update({i: result})
    
    print(data)
    return render(request, 'mainapp/stocktracker.html', {'data': data, 'room_name': 'track'})
