from django import forms
from django.core import validators

class PracticeForm(forms.Form):
    name = forms.CharField(label='User Name', widget=forms.TextInput(attrs = { 'placeholder' : 'Enter Your Name' }))
    email = forms.EmailField()
    check = forms.BooleanField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    contact = forms.CharField(initial='01XX')
    COURSE_CHOICE = [('P', 'Python'),('JS', 'JavaScript'), ('C+', 'C++')]
    Courses = forms.ChoiceField(choices=COURSE_CHOICE)
    CoursesRadio = forms.ChoiceField(widget=forms.RadioSelect,choices=COURSE_CHOICE)
    CoursesMultipleChoice = forms.MultipleChoiceField(label='Choice Multiple', widget=forms.CheckboxSelectMultiple, choices=COURSE_CHOICE)
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
