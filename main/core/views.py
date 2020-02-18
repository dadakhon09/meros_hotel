from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from adminka.model import About


class IndexView(View):
    def get(self, request):
        about = About.objects.get(id=1)

        context = {
            'about': about,
        }

        return render(request, 'main/index.html', context)

    def post(self, request):
        start_date = self.request.POST.get('start_date')
        end_date = self.request.POST.get('end_date')
        num_of_adults = self.request.POST.get('num_of_adults')
        num_of_children = self.request.POST.get('num_of_children')

        return HttpResponseRedirect(reverse('available-rooms', kwargs={'start_date': start_date, 'end_date': end_date,
                                                                       'num_of_adults': num_of_adults,
                                                                       'num_of_children': num_of_children}))

