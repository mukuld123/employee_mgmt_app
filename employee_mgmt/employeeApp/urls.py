from django.contrib import admin
from django.urls import path
from employeeApp import views

urlpatterns = [
    path('', views.HomePage),
    # path('employee/',views.EmployeeListCreate.as_view()),
    # path('employee/<int:pk>/',views.EmployeeReadUpdateDelete.as_view()),

    path('employee/', views.EmployeeAPI.as_view()),
    path('employee/<str:id>', views.EmployeeAPI.as_view()),
    # path(''), 

    # path('account/',views.AccountListCreate.as_view()),
    # path('account/<int:pk>/',views.AccountReadUpdateDelete.as_view()),

    path('department/',views.DepartmentListCreate.as_view()),
    path('department/<int:pk>/',views.DepartmentReadUpdateDelete.as_view()),

    path('role/',views.RoleListCreate.as_view()),
    path('role/<int:pk>/',views.RoleReadUpdateDelete.as_view()),

    
    # path('reimbursement/<int:pk>/',views.ReimbursementReadUpdateDelete.as_view()),
    path('reimbursement/', views.ReimbursementAPI.as_view()),
    path('reimbursement/<str:id>', views.ReimbursementAPI.as_view()),

    

]
