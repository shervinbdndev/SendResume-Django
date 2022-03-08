from django.urls.conf import path
from . import views



urlpatterns = [
    path(route='' , view=views.SendResumeView.as_view() , name='index')
]