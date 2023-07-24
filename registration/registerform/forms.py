# from django import forms
# from django.core.exceptions import ValidationError
# from datetime import date

# class ApplicationForm(forms.Form):
#     name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
#     dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))
#     mobile_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Enter Mobile Number'}))

#     def __init__(self, *args, **kwargs):
#         super(ApplicationForm, self).__init__(*args, **kwargs)

#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if not name.isalpha():
#             raise ValidationError("Name must contain only alphabetic characters.")
#         return name

#     def clean_mobile_number(self):
#         mobile_number = self.cleaned_data['mobile_number']
#         if not mobile_number.isdigit() or len(mobile_number) != 10:
#             raise ValidationError("Mobile number must be a 10-digit numeric value.")
#         return mobile_number

#     def clean_dob(self):
#         dob = self.cleaned_data['dob']
#         today = date.today()
#         age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
#         if age < 18:
#             raise ValidationError("Age must be at least 18 years.")
#         return dob
