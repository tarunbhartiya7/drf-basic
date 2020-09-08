from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# function based view


def employeeView(request):
    # emp = {
    #   'id': 123,
    #   'name': 'John',
    #   'salary': 10000000
    # }

    query_set = Employee.objects.all()
    response = {
        'employees': list(query_set.values('id', 'name', 'salary'))
    }
    return JsonResponse(response)
