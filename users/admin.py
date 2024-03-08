from django.contrib import admin
from .models import CustomUser


# Опционально: Вы можете создать кастомный класс администратора, если хотите настроить отображение модели пользователя в админке.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'phone_number', 'is_active', 'is_staff']  # Пример поля, которые можно отобразить
    # Добавьте другие настройки здесь по необходимости


# Затем регистрируйте модель пользователя с использованием кастомного класса администратора (или без него, если не нужны дополнительные настройки)
admin.site.register(CustomUser, CustomUserAdmin)  # Убедитесь, что используете CustomUserAdmin, если хотите кастомизировать интерфейс
