from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Biography, Education, Projects_photos, Publications_photos, Photo
from django.template import loader
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


def index(request):
    latest_project = Biography.objects.get(pk=3)
    photo = Photo.objects.get(pk=1)
    Projects_images = Projects_photos.objects.all()
    Publications_images = Publications_photos.objects.all()
    latest_stages = Education.objects.all()

###################################################
    message = '''
    New Message: {}
    
    sender name: {}
    sender email: {}'''.format(request.POST.get('message', False), request.POST.get('name', False), request.POST.get('email', False))
    if(request.method == 'POST'):
        send_mail('Personal website message', message, '', [
                  'algezoly2020@gmail.com'])
################################################

    context = {
        'latest_project': latest_project,
        'latest_stages': latest_stages,
        'Projects_images': Projects_images,
        'Publications_images': Publications_images,
        'photo': photo
    }

    template = loader.get_template('core/index.html')
    return HttpResponse(template.render(context, request))
