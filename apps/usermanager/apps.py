from django.apps import AppConfig


class UsermanegerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.usermanager'

    def ready(self):
        import apps.usermanager.signals