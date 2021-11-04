from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .forms import SuggestionForm

latest_response = None

def home(request):
    global latest_response
    context = {}

    form = SuggestionForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            latest_response = convert_suggestion_to_json(request.POST.get('name'), request.POST.get('email'), request.POST.get('message'))
            form.save()
            if request.method == 'POST':
                return redirect('main:success')

    context['form'] = form
    return render(request, 'main/home.html', context)


def success_page(request):
    global latest_response

    if latest_response == None:
        return redirect('main:home')

    data = json.loads(latest_response.content)
    # Get data from JSON and reset JSON
    response = {
        'name' : data['name'],
        'email' : data['email'],
        'message' : data['message'],
    }
    latest_response = None
    
    return render(request, 'main/success.html', response)


def convert_suggestion_to_json(name, email, message):
    return JsonResponse({'name': name, 'email' : email, 'message' : message})
