from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from .models import Profesor

class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            profesor = Profesor.objects.filter(nombre=username, password=password).get()
            return profesor
        except:
            return None

    def get_user(self, user_id):
        try:
            return Profesor.objects.get(pk=user_id)
        except Profesor.DoesNotExist:
            return None

