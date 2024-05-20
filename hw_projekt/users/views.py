from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm




class RegisterView(View):
    template_name = 'users/register.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:main")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Congratulations {username}.Your account has been successfully created")
            return redirect(to="users:signin")
        return render(request, self.template_name, {"form": form})
    

class LogoutUser(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/logout.html')

    def post(self, request):
        logout(request)
        return redirect(to='quotes:main')