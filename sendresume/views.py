from django.shortcuts import (render , redirect)
from django.urls.base import reverse
from django.contrib import messages
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.core.exceptions import BadRequest
from .forms import SendResumeModelForm





class SendResumeView(View):
    def get(self , request : HttpRequest):
        resume_model_form : SendResumeModelForm = SendResumeModelForm()
        return render(request=request , template_name='resume/resume.html' , context={'resume_model_form' : resume_model_form , 'title' : 'Send Your Resume' , 'header' : 'Apply for job'})
    
    def post(self , request : HttpRequest):
        resume_model_form : SendResumeModelForm = SendResumeModelForm(request.POST or None , request.FILES or None)
        if (resume_model_form.is_valid()):
            instance = resume_model_form.save(commit=False)
            instance.save()
            messages.success(request=request , message='Successfully Sent')
            return redirect(to=reverse(viewname='index'))
        return render(request=request , template_name='resume/resume.html' , context={'resume_model_form' : resume_model_form , 'title' : 'Send Your Resume' , 'header' : 'Apply for job'})
    
    
    
    

def error404(request : HttpRequest , *args : BadRequest , **argv : BadRequest):
    return render(request=request , template_name='resume/errors/bad_requests.html' , status=404 , context={'error' : str(request).split(':')[1].split("'")[1].split('/')[1] , 'e404' : 404})
def error500(request : HttpRequest , *args : BadRequest , **argv : BadRequest):
    return render(request=request , template_name='resume/errors/bad_requests.html' , status=500 , context={'error' : str(request).split(':')[1].split("'")[1].split('/')[1] , 'e404' : 500})