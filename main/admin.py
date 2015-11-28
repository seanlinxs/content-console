from django.contrib import admin
from main.models import SiteOwner, Website

# Register your models here.

class WebsiteInline(admin.TabularInline):
    model = Website
    extra = 1


class SiteOwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Email&Phone', {'fields': ['email', 'phone'], 'classes': ['collapse']}),
    ]
    inlines = [WebsiteInline]


admin.site.register(SiteOwner, SiteOwnerAdmin)
