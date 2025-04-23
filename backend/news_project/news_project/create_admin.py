# create_admin.py
import os
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username=os.environ.get("DJANGO_SUPERUSER_USERNAME")).exists():
    User.objects.create_superuser(
        os.environ.get("DJANGO_SUPERUSER_USERNAME"),
        os.environ.get("DJANGO_SUPERUSER_EMAIL"),
        os.environ.get("DJANGO_SUPERUSER_PASSWORD")
    )
    print("Суперпользователь создан!")
else:
    print("Суперпользователь уже существует.")