from django import forms
from .models import Reports


class ReportsForm(forms.ModelForm):
	class Meta:
		model = Reports
		fields= ["date","number", "crew", "status", "unit"]