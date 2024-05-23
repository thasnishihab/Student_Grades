from django.contrib import admin

# Register your models here.
from .models import Student, Subject
from django.contrib.auth.models import User
# from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

anonymous_user = User.objects.all().first()
admin.site.has_permission = lambda r: setattr(r, 'user', anonymous_user) or True

admin.site.unregister(User)
admin.site.unregister(Group)
# admin.site.unregister(Site)

admin.site.register(Student)
admin.site.register(Subject)