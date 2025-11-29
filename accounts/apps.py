from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        # conectar signal para crear grupos después de migrate
        from django.db.models.signals import post_migrate
        from . import signals
        post_migrate.connect(signals.create_groups, sender=self)
