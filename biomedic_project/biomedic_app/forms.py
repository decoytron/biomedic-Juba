# forms.py
# forms.py
from django import forms
from .models import Patient  # Assuming you have a Patient model defined in models.py

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_name', 'age', 'id_number', 'location', 'hiv_status', 'hepatitis_status', 'tb_status']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['patient_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        # Add similar updates for other fields as needed
