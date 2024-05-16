from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from app_users.models import Profile
from app_recipes.models import Dishes
from app_users.forms import RegisterForm


class Registrations(CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = RegisterForm

    def form_valid(self, form):
        response = super().form_valid(form)
        city = form.cleaned_data['city']
        # avatar = form.cleaned_data['avatar']
        Profile.objects.create(user=self.object, city=city)
        login(self.request, self.object)

        # html_message = render_to_string('mail_message/hello.html', {'user': self.object})

        # send_mail(
            # 'Спасибо за регистрацию',
            # '',
            # '5arhipoff5@mail.ru',
            # [self.object.email],
            # html_message=html_message,
        # )
        return response

    def get_success_url(self):
        return reverse_lazy('index')


class UsersProfile(DetailView):
    model = User
    template_name = 'users/info_user.html'
    context_object_name = 'p'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['my_dish'] = Dishes.objects.filter(user=self.request.user)
        return context

