from django.urls import path
from extra_apps import xadmin

urlpatterns = [
    path('xadmin/',xadmin.site.urls),
]
