from django.apps import AppConfig


class DocJaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doc_ja_app'

    def ready(self):
        import doc_ja_app.signals
