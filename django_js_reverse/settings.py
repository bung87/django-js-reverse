# -*- coding: utf-8 -*-
from django.conf import settings

JS_VAR_NAME = getattr(settings, 'JS_REVERSE_JS_VAR_NAME', 'Urls')
JS_REVERSE_FILTERS =getattr(settings,'JS_REVERSE_FILTERS')
JS_REVERSE_USE_BACKBONE =getattr(settings,'JS_REVERSE_USE_BACKBONE',False)