from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View


class AdminLoginView(View):
    def get(self, request):
        return render(request, 'adminka/login.html', {})

    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('adminka-index'))
        return render(request, 'adminka/login.html', {'error': True})


class ProfileUpdateView(LoginRequiredMixin, View):
    def post(self, request):
        username = self.request.POST.get('username')
        old_password = self.request.POST.get('old_password')
        new_password = self.request.POST.get('new_password')
        confirm_pass = self.request.POST.get('confirm_pass')

        user = User.objects.get(id=self.request.user.id)
        if user.check_password(old_password):
            if new_password == confirm_pass:
                user.username = username
                user.set_password(new_password)
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse('adminka-profile'))
            else:
                return render(request, 'adminka/profile.html', {'error_2': True})
        else:
            return render(request, 'adminka/profile.html', {'error_1': True})


class AdminLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('adminka-login'))


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = self.request.user
        return render(request, 'adminka/profile.html', {'user': user})

