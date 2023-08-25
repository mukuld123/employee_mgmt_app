from rest_framework import serializers
from employeeApp.models import Employee, Department, Role, Reimbursement

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_id','emp_fname','emp_lname','emp_gender','emp_dob','emp_manager','emp_contact','emp_city','acc_no','ifsc_code','bank_name','dept_id','role_id','contact_person_name','contact_person_relation']

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = ['acc_no', 'ifsc_code', 'bank_name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['dept_name', 'description']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_title', 'role_level', 'role_description']


class ReimbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimbursement
        fields = ['emp_id', 'ticket_status', 'ticket_amount', 'ticket_reason', 'date_raised', 'date_passed']