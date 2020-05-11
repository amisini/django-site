from django.shortcuts import render
from portfolio.models import Portfolio

def portfolio_index(request):
    portfolio_all = Portfolio.objects.all()
    context = {
        'portfolio_all': portfolio_all
    }
    return render(request, 'portfolio_index.html', context)

def portfolio_detail(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolio_detail.html', context)