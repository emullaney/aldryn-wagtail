# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'divio-demosite',
    'aldryn-wagtail',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())


# all django settings can be altered here

INSTALLED_APPS.extend([
    'bakerydemo.base',
    'bakerydemo.blog',
    'bakerydemo.breads',
    'bakerydemo.locations',
    'bakerydemo.search',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.routable_page',
    'rest_framework',
    'wagtailfontawesome',
])

INSTALLED_APPS.insert(0, 'bakerydemo.demo_admin')

GOOGLE_MAP_API_KEY = 'AIzaSyD31CT9P9KxvNUJOwDq2kcFEIG8ADgaFgw'
