from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import SendResumeModel




class SendResumeModelForm(forms.ModelForm):
    class Meta:
        model = SendResumeModel
        fields = '__all__'
        widgets = {
            'fullname' : forms.TextInput(attrs={
                'class' : 'input--style-6' ,
                'name' : 'full_name' ,
                'placeholder' : 'Full name'
            }) ,
            'email' : forms.EmailInput(attrs={
                'class' : 'input--style-6' ,
                'name' : 'email' ,
                'placeholder' : 'example@email.com'
            }) ,
            'message' : forms.TextInput(attrs={
                'class' : 'textarea--style-6' ,
                'name' : 'message'
            }) ,
            'cv' : forms.FileInput(attrs={
                'class' : 'input-file' ,
                'name' : 'file_cv' ,
                'id' : 'file'
            })
        }
        labels = {
            'fullname' : 'Full Name' ,
            'email' : 'Email Address' ,
            'message' : 'Message' ,
            'cv' : 'Upload CV'
        }
        validators = {
            'fullname' : [
                validators.MinLengthValidator(3) ,
                validators.MaxLengthValidator(250)
            ] ,
            'email' : [
                validators.MaxLengthValidator(250) ,
                validators.EmailValidator
            ] ,
            'message' : [
                validators.MaxLengthValidator(600)
            ]
        }
        error_messages = {
            'fullname' : {
                'required' : 'Please Enter Your Full Name' ,
                'min_length' : 'Full Name Cannot be Under 3 Characters' ,
                'max_length' : 'Full Name Cannot be More Than 250 Characters'
            } ,
            'email' : {
                'required' : 'Please Enter Your Email' ,
                'max_length' : 'Email Cannot be More Than 250 Characters'
            } ,
            'message' : {
                'required' : 'Please Enter Your Message' ,
                'max_length' : 'Message Cannot be More Than 600 Characters'
            } ,
            'cv' : {
                'required' : 'Please Choose Your CV File'
            }
        }