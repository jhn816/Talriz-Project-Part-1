# myapp/views.py
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import logic
from django.http import HttpResponse
from . import logic
from django.contrib.auth.decorators import login_required
from .forms import ItemForm

@login_required
def my_view(request):
    method = request.method         
    path = request.path            
    headers = request.headers       
    body = request.body            
    cookies = request.COOKIES       

    # Process the request as needed
    return HttpResponse("Request.")
@login_required
def test_page(request):
    response = logic.test_logic(request)
    return response

def login_page(request):
    if request.user.is_authenticated and request.method == 'GET':
        response = redirect('marketplace_page')
        return response
    if request.method == 'POST':
        response = logic.login_logic(request)
        return response
    return render(request, 'login_page.html')
@login_required
def sell_page(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    return render(request, 'sell_page.html')
@login_required
def submit_item(request):
    if not request.user.is_authenticated:
        return redirect('login_page')

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        print(request.user.id)
        print(request.user)
        form.instance.seller = request.user
        print(form.instance.seller)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            print("Item saved successfully")
            return HttpResponseRedirect('/marketplace/')
        else:
            print(form.errors)
            return HttpResponse("Form is not valid")
    else:
        form = ItemForm()
    return render(request, 'submit_item.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        response = logic.create_logic(request)
        return response
    return render(request, 'register_page.html')

## is this catagory logic
@login_required
def category_page(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.method == "POST":
        response = logic.category_logic(request)
        return response
    response = logic.category_logic(request)
    return response


#This is the page that will load all items with no specific look into it
@login_required
def marketplace_page(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.method == 'POST':
        response = logic.Market_logic(request)
        return response
    response = logic.Market_logic(request)
    return response


#This is the page tht will handle loading a specific item and getting the details of it
@login_required
def marketplace_searched_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.method == 'POST':
        response = logic.Market__focused_item_logic(request, item_id)
        return response
    return render(request, 'marketplace_page.html')


# Handle listing a new item to the database that user posted
@login_required
def item_listing(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    if request.method == 'POST':
        response = logic.submit_item(request)
        return response 
    
