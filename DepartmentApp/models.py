from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Organization(models.Model):
	org_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
	org_name = models.CharField(max_length=50)
	org_email = models.EmailField(max_length=60)
	org_contact_no = models.CharField(max_length=13)
	org_address = models.CharField(max_length=200)

class Department(models.Model):
    dept_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)



