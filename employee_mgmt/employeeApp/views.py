import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Employee, Department, Role, Reimbursement
from employee_mgmt.serializers import EmployeeSerializer, DepartmentSerializer,  RoleSerializer, ReimbursementSerializer
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.


def HomePage(request):
    return JsonResponse({'hello':'hello'})


# class EmployeeListCreate(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeReadUpdateDelete(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

class EmployeeAPI(APIView):
    def get(self, request, id=None, format=None):
        # id = pk
        if id is not None:
            emp = Employee.objects.get(emp_id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request, id=None, format=None):
        if id is not None:
            id = id
            # print(id)
            form_data = request.data
            # print(form_data['role_id'])
            role_obj = Role.objects.get(role_title=form_data['role_id'])
            form_data['role_id'] = role_obj.id
            dept_obj = Department.objects.get(dept_name=form_data['dept_id'])
            form_data['dept_id'] = dept_obj.id

            emp = Employee.objects.get(emp_id = id)
            serializer = EmployeeSerializer(emp, data=form_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data updated'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        form_data = request.data
        # print(form_data['role_id'])
        role_obj = Role.objects.get(role_title=form_data['role_id'])
        form_data['role_id'] = role_obj.id
        dept_obj = Department.objects.get(dept_name=form_data['dept_id'])
        form_data['dept_id'] = dept_obj.id
        
        serializer = EmployeeSerializer(data = form_data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return HttpResponse({'msg':'data created'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        id = id
        # print(id)
        form_data = request.data
        # print(form_data['role_id'])
        role_obj = Role.objects.get(role_title=form_data['role_id'])
        form_data['role_id'] = role_obj.id
        dept_obj = Department.objects.get(dept_name=form_data['dept_id'])
        form_data['dept_id'] = dept_obj.id

        emp = Employee.objects.get(emp_id = id)
        serializer = EmployeeSerializer(emp, data=form_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class AccountListCreate(ListCreateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer

# class AccountReadUpdateDelete(RetrieveUpdateDestroyAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer


class DepartmentListCreate(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer




class RoleListCreate(ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# class ReimbursementListCreate(ListCreateAPIView):
#     queryset = Reimbursement.objects.all()
#     serializer_class = ReimbursementSerializer

# class ReimbursementReadUpdateDelete(RetrieveUpdateDestroyAPIView):
#     queryset = Reimbursement.objects.all()
#     serializer_class = ReimbursementSerializer

class ReimbursementAPI(APIView):
    def get(self, request, id=None, format=None):
        # id = pk
        real_id = Employee.objects.get(emp_id=id)
        if id is not None:
            rmb = Reimbursement.objects.filter(emp_id=real_id)
            serializer = ReimbursementSerializer(rmb,many=True)
            return Response(serializer.data)
        
        rmb = Reimbursement.objects.all()
        serializer = ReimbursementSerializer(rmb, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        form_data = request.data
        # print(form_data['role_id'])
        rmb_obj = Employee.objects.get(emp_id=form_data['emp_id'])
        form_data['emp_id'] = rmb_obj.id
        
        serializer = ReimbursementSerializer(data = form_data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return HttpResponse({'msg':'data created'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

