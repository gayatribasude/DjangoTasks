from django.db import models

# Create your models here.
class Country(models.Model):
    country_name=models.CharField(max_length=30)

    def __str__(self):
        return self.country_name

class State(models.Model):
    country_name=models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name=models.CharField(max_length=30)

    def __str__(self):
        return self.state_name

class City(models.Model):
    state_name=models.ForeignKey(State,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=30)

    def __str__(self):
        return self.city_name


class Student(models.Model):
    name=models.CharField(max_length=30)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

