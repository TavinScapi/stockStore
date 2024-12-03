from django.apps import AppConfig


class TccConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TCC'

# apps.py
from django.apps import AppConfig

class EstoqueConfig(AppConfig):
    name = 'TCC'

    def ready(self):
        import TCC.signals  # Certifique-se de que os sinais sejam importados
