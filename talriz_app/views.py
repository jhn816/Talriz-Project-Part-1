# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from . import logic
from django.http import HttpResponse
from . import logic

def my_view(request):
    method = request.method         
    path = request.path            
    headers = request.headers       
    body = request.body            
    cookies = request.COOKIES       

    # Process the request as needed
    return HttpResponse("Request.")

def test_page(request):
    response = logic.test_logic(request)
    return response

def login_page(request):
    if request.method == 'POST':
        response = logic.login_logic(request)
        return response
    return render(request, 'talriz/login_page.html')


def register_page(request):
    if request.method == 'POST':
        response = logic.create_logic(request)
        return response
    return render(request, 'talriz/register_page.html')

## is this catagory logic
def filters_page(request):
    response = logic.filters_logic(request)
    return response

def marketplace_page(request):
    if request.method == 'POST':
        response = logic.Market_logic(request)
        return response
    return render(request, 'talriz/marketplace_page.html')

