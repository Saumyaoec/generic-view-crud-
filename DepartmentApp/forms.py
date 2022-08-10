from django import forms
from .models import *

class OrganizationForm(forms.ModelForm):
   
    class Meta:
        model = Organization
        fields = ['org_name','org_email','org_contact_no','org_address']


class DepartmentForm(forms.ModelForm):

	class Meta:
		model = Department
		fields = ['user','role','org']

		
		
