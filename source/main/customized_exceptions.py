# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException
from django.utils.translation import gettext as _




class Custom400Exception(ValidationError):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Bank partner's admin cannot create lead or order")
    default_code = 1203


class Custom403Exception(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _("Bank partner's admin cannot create lead or order")
    default_code = 1204
