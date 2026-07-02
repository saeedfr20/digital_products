from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class SKUValidator(RegexValidator):
    regex = '^[a-zA-Z0-9\-\_]{6,20}$'
    message = 'SKU must be alphanumeric with 6 to 20 characters'
    code = 'invalid_sku'


class PhoneNumberValidator(RegexValidator):
    regex = '^98(9[0-3,9]\d{8}|[1-9]\d{9})$'
    message = 'Phone number must be a VALID 12 digits like 98xxxxxxxxxx'
    code = 'invalid_phone_number'


validate_sku = SKUValidator()
validate_phone_number = PhoneNumberValidator()
