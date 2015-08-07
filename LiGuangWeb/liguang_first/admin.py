from django.contrib import admin

# Register your models here.
from .models import BusinessClass
from .models import Business
from .models import CustomUser


class BusinessInline(admin.TabularInline):
    model = Business
    extra = 1
class BusinessClassAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['businessclass_name']}),
        ('Data order', {'fields': ['businessclass_order'], 'classes': ['collapse']}),
    ]
    inlines = [BusinessInline]
    list_filter = ['businessclass_order']
    list_display = ('businessclass_name', 'businessclass_order')

class BusinessAdmin(admin.ModelAdmin):
    search_fields = ['business_name']
    list_display = ('business_name', 'business_contents')


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['get_firstname','get_lastname']

    def get_firstname(self, obj):
        return obj.user.first_name
    get_firstname.short_description = 'firstname'

    def get_lastname(self, obj):
        return obj.user.last_name
    get_lastname.short_description = 'lastname'

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(BusinessClass,BusinessClassAdmin)
admin.site.register(Business,BusinessAdmin)