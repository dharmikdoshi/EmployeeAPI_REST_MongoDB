from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Employee
from .serializer import EmployeeSerializer
# Create your views here.

@csrf_exempt
def employeeApi(request,id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        emp_serialze = EmployeeSerializer(employees,many=True)
        return JsonResponse(emp_serialze.data,safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        emp_serialize = EmployeeSerializer(data=employee_data)
        if emp_serialize.is_valid():
            emp_serialize.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Error, Failed to add",safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(empid=employee_data['empid'])
        emp_serialize = EmployeeSerializer(employee,data=employee_data)
        if emp_serialize.is_valid():
            emp_serialize.save()
            return JsonResponse("Record Updated",safe =False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee = Employee.objects.get(empid=id)
        employee.delete()
        return JsonResponse("Record Deleted",safe=False)
        
