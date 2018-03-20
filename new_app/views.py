from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from new_app.forms import ObstacleForm
from new_app.models import Element, Obstacle
from .forms import LoginForm, NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse


class StartPageView(View):
    def get(self, request):
        return render(request, template_name='base.html')


class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        ctx = {
            'form': form
        }
        return render(request, template_name='login_view.html', context=ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('main'))
            return HttpResponse('no nie koniecznie')
        ctx = {
            'form': form
        }
        return render(request, template_name='base.html', context=ctx)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('main'))


class NewUserView(View):
    def get(self, request):
        form = NewUserForm()
        ctx = {
            'form': form
        }
        return render(request, template_name='login_view.html', context=ctx)

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            if User.objects.filter(username=login).exists():
                form.add_error('login', 'Taki login jest już zajęty')
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            if password != password2:
                form.add_error('password', 'hasła nie pasują do siebie')
            if not form.errors:
                email = form.cleaned_data['email']
                User.objects.create_user(login, email, password, first_name=first_name, last_name=last_name)
                return redirect(reverse('main'))
        ctx = {
            'form': form
        }
        return render(request, template_name='login_view.html', context=ctx)


class ElementsView(View):

    def get(self, request):
        elements = Element.objects.all()  #order by?
        cnx = {
            'elements': elements
        }
        return render(request, template_name="elements_list.html", context=cnx)


class AddElementView(CreateView):
    model = Element
    fields = '__all__'
    success_url = reverse_lazy('elements')


class UpdateElementView(UpdateView):
    model = Element
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('elements')


class ElementView(View):
    def get(self, request, element_id):
        element = get_object_or_404(Element, pk=element_id)
        cnx = {
            'element': element,
        }
        return render(request, template_name='element.html', context=cnx)


class ObstaclesView(View):

    def get(self, request):
        obstacles = Obstacle.objects.all()  #order by?
        cnx = {
            'obstacles': obstacles
        }
        return render(request, template_name="obstacles_list.html", context=cnx)


class AddObstacleView(CreateView):
    model = Obstacle
    form_class = ObstacleForm
    success_url = reverse_lazy('obstacles')


class UpdateObstacleView(UpdateView):
    model = Obstacle
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('obstacles')


class ObstacleView(View):
    def get(self, request, obstacle_id):
        obstacle = get_object_or_404(Obstacle, pk=obstacle_id)
        cnx = {
            'obstacle': obstacle,
        }
        return render(request, template_name='obstacle.html', context=cnx)


class DeleteObstacleView(DeleteView):
    model = Obstacle
    success_url = reverse_lazy('obstacles')