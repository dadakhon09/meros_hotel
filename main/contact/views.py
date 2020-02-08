from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View


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
                         'odadaxon99@gmail.com', ['odadaxon99@gmail.com', ])
        m.send()
        return HttpResponseRedirect(reverse('contact'))
