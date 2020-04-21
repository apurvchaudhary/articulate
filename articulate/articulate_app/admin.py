from django.contrib import admin
from django.contrib.auth.models import Group, User
from articulate_app.models import Article

# Register your models here.
admin.site.register([Article])
admin.site.unregister([Group, User])
admin.site.site_header = 'Admin by geeky@purv ©2020'
admin.site.site_url = "/ani/home"