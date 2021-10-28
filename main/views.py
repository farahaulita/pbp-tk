from django.shortcuts import render, redirect
from .forms import SuggestionForm


def home(request):
    context = {}

    form = SuggestionForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        if request.method == 'POST':
            return redirect('main:home')

    context['form'] = form
    return render(request, 'main/home.html', context)
