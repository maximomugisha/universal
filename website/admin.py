from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *
from django.apps import apps


# Register your models here.
# Define an inline admin descriptor for System admin model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'user_profiles'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register all models except already registered
# models = apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Work)
admin.site.register(Biography)
admin.site.register(Hobby)
admin.site.register(HobbyCategory)
admin.site.register(Skill)
admin.site.register(SkillCategory)
