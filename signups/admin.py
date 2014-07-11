from django.contrib import admin

# Register your models here.
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp

# makes signups app / model renderable in admin panel
admin.site.register(SignUp, SignUpAdmin)