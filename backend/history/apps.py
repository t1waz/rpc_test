from django.apps import AppConfig

from backend import container


class HistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'history'

    def ready(self):
        container.wire(modules=['.views'])
