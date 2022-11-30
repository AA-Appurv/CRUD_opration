from django.urls import path
from .views import *


urlpatterns = [
    path("create_emp_details/",create_emp_details),
    path("get_emp_details/",get_emp_details),
    path("edit_emp_details/",edit_emp_details),
    path("delete_emp_details/",delete_emp_details),
    path("create_project/",create_project),
    path("create_project/",create_project),
]
