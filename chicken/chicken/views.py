from django.shortcuts import render


def index(request):
	template='index.html'
	return render(request, template)


def store(request):
	template='store.html'
	return render(request, template)


def products(request):
	template='products.html'
	return render(request, template)

def about(request):
	template='about.html'
	return render(request, template)
