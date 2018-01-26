# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from primera_app.models import AccessRecord, Topic, Webpage

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
