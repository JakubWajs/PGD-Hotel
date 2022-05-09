from django.apps import apps
from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email',)


app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
