from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "admin@correo.com"
password = "Admin12345"  # cámbiala

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print("Superusuario creado correctamente")
else:
    print("El superusuario ya existe")