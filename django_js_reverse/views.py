#-*- coding: utf-8 -*-
import re
import sys

if sys.version < '3':
    text_type = unicode
else:
    text_type = str

from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from .settings import JS_VAR_NAME, JS_REVERSE_FILTERS,JS_REVERSE_USE_BACKBONE


def urls_js(request):
    if not re.match(r'^[$A-Z_][\dA-Z_$]*$', JS_VAR_NAME.upper()):
        raise ImproperlyConfigured(
            'JS_REVERSE_JS_VAR_NAME setting "%s" is not a valid javascript identifier.' % (JS_VAR_NAME))
    url_patterns = list(urlresolvers.get_resolver(None).reverse_dict.items())
    url_list = []
    url_routes={}
    print(url_patterns)
    for url_name, url_pattern in url_patterns:
        parttern = list(url_pattern[0][0])
        if not isinstance(url_name, text_type):
            url_name = url_name.__name__
        matched = False
        for f in JS_REVERSE_FILTERS:
            if url_name.startswith(f):
                matched = True
                break
        if matched == False:
            if JS_REVERSE_USE_BACKBONE:
                parttern[0]=parttern[0].replace('%(',':').replace(')s','')
                url_routes[parttern[0]]=url_name
            url_list.append((url_name, parttern))

    return render_to_response('django_js_reverse/urls_js.tpl',
                              {
                                  'urls': url_list,
                                  'url_prefix': urlresolvers.get_script_prefix(),
                                  'js_var_name': JS_VAR_NAME,
                                  'use_backbone':JS_REVERSE_USE_BACKBONE,
                                  'url_routes':url_routes
                              },
                              context_instance=RequestContext(request), content_type='application/javascript')
