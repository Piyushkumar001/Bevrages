from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

@login_required(login_url='/login')
def products(request):
	prod = Products.objects.all()
	return render(request, 'products.html', {'prod':prod})

def store(request):
	return render(request, 'store.html', {})

def registerUser(request):
	frm = UserCreationForm()
	if request.method == 'POST':
		frm = UserCreationForm(request.POST)
		if frm.is_valid():
			frm.save()
			return redirect("login")
	return render(request, 'register.html', {'frm':frm})

def loginUser(request):
	if request.user.is_authenticated:
		return redirect('login')
	if request.method == 'POST':
		username = request.POST.get('username')
		pwd = request.POST.get('passwd')
		user = authenticate(request, username = username, password = pwd)
		if user is not None:
			login(request, user)
			return redirect('products')
	return render(request, 'login.html', {})


def logoutUser(request):
	logout(request)
	return redirect('login')
	
def OrderDetails(request):
    frm=OrderdetailForm()
    return render(request, 'cart.html', {'frm':frm})

def visit_us_today(request):
	return render(request, 'register.html', {})


