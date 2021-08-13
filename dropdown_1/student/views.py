from django.shortcuts import render
from django.views.generic import CreateView
from .models import Student,State,City
from .forms import StudentForm

# Create your views here.

class CreateStudent(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/create_student.html'

def load_state(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_name_id=country_id)
    return render(request, 'student/state_dropdown.html', {'states': states})

def load_city(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_name_id=state_id)
    return render(request, 'student/city_dropdown.html', {'cities': cities})



