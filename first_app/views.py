from django.shortcuts import render
from .forms import PracticeForm
# Create your views here.

def apiForm(request):
    if request.method == 'POST':
        form = PracticeForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PracticeForm
    return render(request, 'api_form.html', {'form' : form})
