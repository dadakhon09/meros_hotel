from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from meros_hotel.settings import EMAIL_HOST_USER


class ContactView(View):
    def get(self, request):
        return render(request, 'main/contact.html')

    def post(self, request):
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        m = EmailMessage(subject,
                         f'Name: {full_name}\n Email: {email}\n Message:\n{message}',
                         EMAIL_HOST_USER, ['meros.khiva@gmail.com', ])
        m.send()
        return render(request, 'main/contact.html')
