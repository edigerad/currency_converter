from django.core.validators import RegexValidator
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

name_regex = RegexValidator(regex=f'^[^{settings.ACCOUNT_SYMBOLS_REGEX}]',
                            message=_("Name is not correct!"))
