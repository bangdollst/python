# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
import os, sys, BaseHTTPServer

# Create your tests here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print (BASE_DIR)


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
print (STATICFILES_DIRS)



full_path = os.getcwd()
print (full_path)
