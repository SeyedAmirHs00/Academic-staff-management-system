from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.account'
    verbose_name = _('account')
