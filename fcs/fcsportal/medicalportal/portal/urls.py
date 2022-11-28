# from django.contrib import admin
from django.urls import path
from .views import Patientregister,adminwait, logpatient,loggedinpatient, nope,loginproffesional,professionalregister

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , Patientregister,name="Patientregister"),
    path('waithere',adminwait,name="adminwait"),
    path('loginpatient',logpatient,name="logpatient"),
    path('patientdashboard',loggedinpatient,name="logpatient"),
    path('noapproval',nope,name="nope"),
    path('loginprof',loginproffesional,name=",loginproffesional"),
    path('profsignup',professionalregister,name="professionalregister")
    
]