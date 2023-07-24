from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from registerform.models import ApplicationForm
from django.core.mail import send_mail

from django.core.exceptions import ValidationError
from datetime import date

# Create your views here.


def home(request):
    return render(request, 'main.html')


def success(request):
    return render(request, 'success.html')


# In your views.py or wherever you process form submissions



def is_valid_name(name):
    return all(char.isalpha() or char.isspace() for char in name)

# def user(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         dob = request.POST.get('dob', '')
#         email = request.POST.get('email', '')
#         mobile_number = request.POST.get('mobile_number', '')

#         # Custom Validations
#         errors = {}
#         if not is_valid_name(name):
#             errors['name'] = "Name must contain only alphabetic characters."
#         try:
#             dob = date.fromisoformat(dob)
#             today = date.today()
#             age = today.year - dob.year - \
#                 ((today.month, today.day) < (dob.month, dob.day))
#             if age < 18:
#                 errors['dob'] = "Age must be at least 18 years."
#         except ValueError:
#             errors['dob'] = "Invalid date format."
#         if not mobile_number.isdigit() or len(mobile_number) != 10:
#             errors['mobile_number'] = "Mobile number must be a 10-digit numeric value."

#         if errors:
#             # If there are validation errors, re-render the form with error messages
#             return render(request, 'registerform.html', {'errors': errors, 'name': name, 'dob': dob, 'email': email, 'mobile_number': mobile_number})

#         # Save the form data to the database
#         form_entry = ApplicationForm(
#             name=name, dob=dob, email=email, mobile_number=mobile_number)
#         form_entry.save()

#         return render(request, 'success.html')

#     else:
#         return render(request, 'registerform.html')



def is_valid_name(name):
    return all(char.isalpha() or char.isspace() for char in name)

def user(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dob = request.POST.get('dob', '')
        email = request.POST.get('email', '')
        mobile_number = request.POST.get('mobile_number', '')

        # Custom Validations
        errors = {}
        if not is_valid_name(name):
            errors['name'] = "Name must contain only alphabetic characters."

        try:
            dob = date.fromisoformat(dob)
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                errors['dob'] = "Age must be at least 18 years."
        except ValueError:
            errors['dob'] = "Invalid date format."

        if not mobile_number.isdigit() or len(mobile_number) != 10:
            errors['mobile_number'] = "Mobile number must be a 10-digit numeric value."

        if errors:
            # If there are validation errors, re-render the form with error messages
            return render(request, 'registerform.html', {'errors': errors, 'name': name, 'dob': dob, 'email': email, 'mobile_number': mobile_number})

        # Send the confirmation email to the user
        send_confirmation_email(name, email)

        # Save the form data to the database
        form_entry = ApplicationForm(
            name=name, dob=dob, email=email, mobile_number=mobile_number)
        form_entry.save()

        return render(request, 'success.html')

    else:
        return render(request, 'registerform.html')

# def send_confirmation_email(name, email):
#     subject = 'Registration Confirmation'
#     message = f'Dear {name},\n\nThank you for registering. Your Application is successfully Submitted.'
#     from_email = 'srsukale20@gmail.com'  # Replace with your Gmail email address or use a separate email address for sending
#     recipient_list = [email]
#     send_mail(subject, message, from_email, recipient_list)







def send_confirmation_email(name, email):
    subject = 'Registration Confirmation'
    message = f'Dear {name},\n\nThank you for registering. Your application is successfully submitted.'
    from_email = settings.EMAIL_HOST_USER  # Assuming you have defined EMAIL_HOST_USER in your Django settings
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        print("Confirmation email sent successfully.")
    except Exception as e:
        print("An error occurred while sending the confirmation email:", str(e))








def details(request):

    data = ApplicationForm.objects.all()
    content = {}
    content['details'] = data

    return render(request, 'details.html', content)
