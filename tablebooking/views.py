from django.shortcuts import render, redirect
from .models import *
from .forms import Customerform, Resturantform, Booktableform, Orderdishform, CreateUserform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *


# Create your views here
@login_required(login_url='login')
def home(request):
    return render(request, 'admindash/home.html')

@login_required(login_url='login')
def UserPage(request):
    context = {}
    return render(request, 'admindash/user.html', context)


@login_required(login_url='login')
@admin_only
def dash(request):
    tcust = Customer.objects.all()
    trest = Restaurant.objects.all()
    ttord = BookTable.objects.all()
    tpord = OrdersDish.objects.all()

    cust = tcust.count()
    rest = trest.count()
    tord = ttord.count()
    pord = tpord.count()
    context = {'cust': cust, 'rest': rest, 'tord': tord, 'pord': pord}
    return render(request, 'admindash/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def show_cust(request):
    cust = Customer.objects.all()
    return render(request, 'admindash/show_cust.html', {'cust': cust})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def show_rest(request):
    rest = Restaurant.objects.all()
    return render(request, 'admindash/show_rest.html', {'rest': rest})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def show_torder(request):
    tord = BookTable.objects.all()
    return render(request, 'admindash/show_torder.html', {'tord': tord})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def show_porder(request):
    pord = OrdersDish.objects.all()
    return render(request, 'admindash/show_porder.html', {'pord': pord})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_cust(request):
    add_form = Customerform()
    if request.method == 'POST':
        add_form = Customerform(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('/admindash')
    context = {'add_form': add_form}
    return render(request, 'admindash/add_cust.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_rest(request):
    add_form = Resturantform()
    if request.method == 'POST':
        add_form = Resturantform(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('/admindash')

    context = {'add_form': add_form}
    return render(request, 'admindash/add_rest.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_torder(request):
    add_form = Booktableform()
    if request.method == 'POST':
        add_form = Booktableform(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('/admindash')

    context = {'add_form': add_form}
    return render(request, 'admindash/add_torder.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_porder(request):
    add_form = Orderdishform()
    if request.method == 'POST':
        add_form = Orderdishform(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('/admindash')

    context = {'add_form': add_form}
    return render(request, 'admindash/add_porder.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def view_cust(request, pk):
    customers = Customer.objects.get(id=pk)
    torders = (customers.booktable_set.all())
    porders = (customers.ordersdish_set.all())

    context = {'customers': customers, 'torders': torders, 'porders': porders}
    return render(request, 'admindash/view_cust.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def view_rest(request, pk):
    resturant = Restaurant.objects.get(id=pk)
    torders = (resturant.booktable_set.all())
    porders = (resturant.ordersdish_set.all())

    context = {'resturant': resturant, 'torders': torders, 'porders': porders}
    return render(request, 'admindash/view_rest.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def view_torder(request):
    return render(request, 'admindash/view_torder.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def view_porder(request):
    return render(request, 'admindash/view_porder.html')


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            messages.info(request, 'USERNAME or PASSWORD is Incorrect')
    context = {}
    return render(request, 'admindash/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def register(request):
    form = CreateUserform()
    if request.method == 'POST':
        form = CreateUserform(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account was Created for ' + str(username))
            return redirect('login')

    context = {'form': form}
    return render(request, 'admindash/register.html', context)
