from django.shortcuts import render
from .forms import PracticeForm
# Create your views here.

def apiForm(request):
    if request.method == 'POST':
        form = PracticeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PracticeForm
    return render(request, 'api_form.html', {'form' : form})

def djangoModel(request):
    return render(request, 'django_model.html')