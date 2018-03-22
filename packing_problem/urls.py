"""packing_problem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from new_app.views import UserLoginView, UserLogoutView, NewUserView, StartPageView, AddElementView, \
    UpdateElementView, ElementsView, ElementView, AddObstacleView, UpdateObstacleView, ObstaclesView, ObstacleView, \
    DeleteObstacleView, AddVehicleView, UpdateVehicleView, VehiclesView, VehicleView, DeleteVehicleView, SetTransport
from packing_problem import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', StartPageView.as_view(), name='main'),
    url(r'^login$', UserLoginView.as_view(), name='login'),
    url(r'^logout$', UserLogoutView.as_view(), name='logout'),
    url(r'^add_user$', NewUserView.as_view(), name='new-user'),
    url(r'^add_element$', AddElementView.as_view(), name='add-element'),
    url(r'^update_element/(?P<pk>\d+)/$', UpdateElementView.as_view(), name='update-element'),
    url(r'^elements', ElementsView.as_view(), name="elements"),
    url(r'^element/(?P<element_id>(\d)+)', ElementView.as_view(), name='element'),
    url(r'^add_obstacle$', AddObstacleView.as_view(), name='add-obstacle'),
    url(r'^update_obstacle/(?P<pk>\d+)/$', UpdateObstacleView.as_view(), name='update-obstacle'),
    url(r'^obstacles', ObstaclesView.as_view(), name="obstacles"),
    url(r'^obstacle/(?P<obstacle_id>(\d)+)', ObstacleView.as_view(), name='obstacle'),
    url(r'^delete_obstacle/(?P<pk>(\d)+)$', DeleteObstacleView.as_view(), name='delete-obstacle'),
    url(r'^add_vehicle$', AddVehicleView.as_view(), name='add-vehicle'),
    url(r'^update_vehicle/(?P<pk>\d+)/$', UpdateVehicleView.as_view(), name='update-vehicle'),
    url(r'^vehicles', VehiclesView.as_view(), name="vehicles"),
    url(r'^vehicle/(?P<vehicle_id>(\d)+)', VehicleView.as_view(), name='vehicle'),
    url(r'^delete_vehicle/(?P<pk>(\d)+)$', DeleteVehicleView.as_view(), name='delete-vehicle'),
    url(r'^set_transports/$', SetTransport.as_view(), name="set-transport"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
