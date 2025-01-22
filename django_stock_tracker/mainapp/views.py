from django.shortcuts import render
from yahoo_fin.stock_info import *


# Create your views here.
def stock_picker(request):
    stock_picker_tickers = tickers_dow()
    return render(request, "mainapp/stockpicker.html", {"stockpicker": stock_picker_tickers})


def stock_tracker(request):
    return render(request, "mainapp/stocktracker.html")
