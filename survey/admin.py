from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from survey.models import MultipleSelect, Preliminary1, Preliminary2, Preliminary3, Preliminary4, Onboarding1, Onboarding2, Onboarding3, Onboarding4

class DisplayUser(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user', )

# Register your models here.

admin.site.register(MultipleSelect)
admin.site.register(Preliminary1, DisplayUser)
admin.site.register(Preliminary2, DisplayUser)
admin.site.register(Preliminary3, DisplayUser)
admin.site.register(Preliminary4, DisplayUser)
admin.site.register(Onboarding1, DisplayUser)
admin.site.register(Onboarding2, DisplayUser)
admin.site.register(Onboarding3, DisplayUser)
admin.site.register(Onboarding4, DisplayUser)