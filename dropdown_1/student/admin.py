from django.contrib import admin
from .models import Student,Country,State,City
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','country','state','city')
admin.site.register(Student,StudentAdmin)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)