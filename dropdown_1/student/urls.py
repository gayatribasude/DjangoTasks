from django.urls import path
from .views import CreateStudent,load_state,load_city

urlpatterns=[
    path('',CreateStudent.as_view(),name='create_student'),
    path('ajax_load_state',load_state,name='ajax_load_state'),
    path('ajax_load_city',load_city,name='ajax_load_city'),
]

