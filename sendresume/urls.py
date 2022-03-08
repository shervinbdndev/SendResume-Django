from django.urls.conf import path
from . import views



urlpatterns = [
    path(route='' , view=views.SendResumeView.as_view() , name='index') ,
    path(route='' , view=views.error404) ,
    path(route='' , view=views.error500)
]