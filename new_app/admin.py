from django.contrib import admin

# Register your models here.
from new_app.models import Vehicle, Transport, Element

admin.site.register(Vehicle)
admin.site.register(Transport)
admin.site.register(Element)
