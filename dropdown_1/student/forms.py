from django import forms
from .models import Student,City,State

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = '__all__'
        exclude = ['name',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset=State.objects.none()
        self.fields['city'].queryset = City.objects.none()

