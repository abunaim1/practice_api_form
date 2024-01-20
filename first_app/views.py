from django.shortcuts import render
from .forms import PracticeForm
from . import models
# Create your views here.

def apiForm(request):
    if request.method == 'POST':
        form = PracticeForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PracticeForm
    return render(request, 'api_form.html', {'form' : form})

def djangoModel(request):
    model = models.ExampleModel.objects.all()
    return render(request, 'django_model.html', {'model':model})