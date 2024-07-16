from django.shortcuts import render

from . models import Profile
# Create your views here.
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

def accept(request):
    if request.method=="POST":

        name = request.POST.get("name" , "")
        email = request.POST.get("email" , "")
        phone = request.POST.get("phone" , "")
        summary = request.POST.get("summary" , "")
        degree1 = request.POST.get("degree1" , "")
        degree2 = request.POST.get("degree2" , "")
        skills = request.POST.get("skills" , "")
        projects = request.POST.get("projects" , "")
        experience = request.POST.get("experience" , "")
        language = request.POST.get("language" , "")

        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree1=degree1,degree2=degree2,skills=skills,projects=projects,experience=experience,language=language)
        profile.save()

    return render(request , 'cvgenerator/accept.html')

def resume(request,id):
    user_profiles = Profile.objects.get(pk=id)

    template = loader.get_template('cvgenerator/resume.html')
    html = template.render({'user_profile':user_profiles})
    options ={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment'
    filename = "resume.pdf"
    return response