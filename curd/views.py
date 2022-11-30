from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import * 
from email import message
from urllib import response
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def create_emp_details(request):
    """
    url:create_emp_details/
    doc:create employee details.
    """
    if request.method == "POST":
        try:
            employee_serializer = EmployeeSerializer(data = request.data)
            if employee_serializer.is_valid():
                employee_serializer.save()
        except Exception as e:
            return Response({message:e.__str__()},status = 400)
        return Response(employee_serializer.data,status = 200)

@api_view(['GET'])
def get_emp_details(request):
    """
    url:get_emp_details/
    doc:get employee details.
    """
    if request.method == "GET":
        try:
            emp_obj = Employee.objects.all()
        except Exception as e:
            return Response({"error":e.__str__()},status= 400)
        return Response(EmployeeSerializer(emp_obj,many=True).data,status = 200)
    
@api_view(['PUT'])
def edit_emp_details(request):
    """
    url:edit_emp_details/
    doc:edit employee details.
    """
    emp_id = request.data.get("emp_id")
    try:
        emp_obj = Employee.objects.get(emp_id = emp_id)
    except Exception as e:
        return Response({"error":e.__str__()},status= 400)
    if request.method == "PUT":
        emp_obj.first_name = request.data.get('first_name')
        emp_obj.last_name = request.data.get('last_name')
        emp_obj.salary = request.data.get('salary')
        emp_obj.picture = request.data.get('picture')
        emp_obj.mob_no = request.data.get('mob_no')
        emp_obj.address = request.data.get('address')
        emp_obj.save()
        return Response(EmployeeSerializer(emp_obj).data,status=200)
    return Response(EmployeeSerializer(emp_obj).error, status=400)

@api_view(["DELETE"])
def delete_emp_details(request):
    """
    url:delete_emp_details/
    doc:delete employee details.
    """
    if request.method == "DELETE":
        payloadData = JSONParser().parse(request)
        emp_id = payloadData["emp_id"]
        try:
            emp_obj = Employee.objects.filter(emp_id=emp_id)
        except Exception as e:
            return Response({e.__str__()},status= 400)
        if emp_obj.exists():
            emp_obj.delete()
        else:
            return Response({"message":"Already Deleted"})
        return Response({"message":"Deleted Successfully"},status=200)
    
@api_view(["POST"])
def create_project(request):
    if request.method == "POST":
        try:
            emp_id = request.data.get("emp_id")
            project_id = request.data.get("project_id")
            project_name = request.data.get("project_name")
            project_duration = request.data.get("project_duration")
            project_status = request.data.get("project_status")
            emp_obj = Employee.objects.filter(emp_id= emp_id)
            if len(emp_obj) != 0:
                project_data = Projects.objects.create(
                    emp_id_id = emp_id,
                    project_id = project_id,
                    project_name = project_name,
                    project_duration = project_duration,
                    project_status= project_status
                )
            else:
                return Response({"message":"emp_id is not in table"},status = 200)
            project_data.save()
        except Exception as e:
            return Response({"message":e.__str__()},status = 400)
        return Response({"message":"Created successfully"},status = 200)
    
@api_view(["GET"])
def get_project(request):
    if request.method == "GET":
        try:
            project_obj = Projects.objects.all()
        except Exception as e:
            return Response({"message":e.__str__()},status = 400)
        project_seri = ProjectsSerializer(project_obj, many=True).data
        return Response({"response":project_seri},status = 200)