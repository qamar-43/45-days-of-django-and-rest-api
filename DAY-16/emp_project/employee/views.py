from django.http import JsonResponse
from django.shortcuts import render
from employee.models import Employee

# Home view
def home(request):
    return render(request, 'employee/home.html')

# List view
def employee_list(request):
    employees = Employee.objects.all()
    context = {
        'employee': employees
    }
    return render(request, 'employee/employee_list.html', context)

# API view
def employee_api(request):
    employees = Employee.objects.all().values('id', 'name', 'age', 'department', 'email')
    return JsonResponse(list(employees), safe=False)
