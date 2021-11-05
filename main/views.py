from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import SuggestionForm
import json

latest_response = False
name = None
email = None
message = None

def home(request):
    global latest_response
    global name
    global email
    global message

    context = {}

    form = SuggestionForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():

            latest_response = True
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            form.save()
            if request.method == 'POST':
                return redirect('main:success')

    context['form'] = form
    return render(request, 'main/home.html', context)


def success_page(request):
    global latest_response

    if not latest_response:
        return redirect('main:home')
    
    latest_response = False
    
    return render(request, 'main/success.html')


def save_json(request):
    global name
    global email
    global message
    return JsonResponse({'name': name, 'email' : email, 'message' : message})
