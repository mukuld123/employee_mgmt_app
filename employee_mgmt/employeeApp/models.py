from django.db import models

# Create your models here.


# class Salary(models.Model):
#     # salary_id 
#     month_no = models.IntegerField()
#     working_days_count = models.IntegerField()

#     def __str__(self):
#         return self.month_no
    

class Department(models.Model):
    # dept_id
    dept_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.dept_name
    

# class ContactPerson(models.Model):
#     # person_id
#     person_name = models.CharField(max_length=50)
#     person_relation = models.CharField(max_length=50)

#     def __str__(self):
#         return self.person_name
    

class Role(models.Model):
    role_title = models.CharField(max_length=20)
    role_level = models.CharField(max_length=20)
    role_description = models.CharField(max_length=200)

    def __str__(self):
        return self.role_title


class Employee(models.Model):
    emp_id = models.SlugField(max_length=15, null=False)                # id
    emp_fname = models.CharField(max_length=50, null=True)
    emp_lname = models.CharField(max_length=50, null=True)
    # emp_age = models.IntegerField()
    emp_gender = models.CharField(max_length=20, null=True)
    emp_dob = models.DateField(null=True)
    emp_manager = models.CharField(max_length=50, null=True)
    emp_contact = models.IntegerField(null=True)
    emp_city = models.CharField(max_length=50, null=True)
    # salary_id =  models.ForeignKey(Salary, on_delete=models.CASCADE)
    # select_related, prefetch_related,
    acc_no = models.IntegerField(null=True)
    ifsc_code = models.CharField(max_length=20, null=True)
    bank_name = models.CharField(max_length=50, null=True)
    dept_id  = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept_of', null=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_of', null=True)
    contact_person_name = models.CharField(max_length=50, null=True)
    contact_person_relation = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"{self.emp_id}. {self.emp_fname} {self.emp_lname}"


# class Account(models.Model):

#     acc_no = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='account_for')
#     ifsc_code = models.CharField(max_length=20)
#     bank_name = models.CharField(max_length=50)

#     def __str__(self):
#         return str(self.acc_no)
    

class Reimbursement(models.Model):
    # ticket_id
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reimbursement_for')
    ticket_status = models.CharField(max_length=20, null=True, blank=True)
    ticket_amount = models.IntegerField()
    ticket_reason = models.CharField(max_length=200)
    date_raised = models.DateField()
    date_passed = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.emp_id)
    
