from django.contrib import admin

# Register your models here.
from .models import BusinessClass
from .models import Business

class BusinessInline(admin.TabularInline):
    model = Business
    extra = 3
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

admin.site.register(BusinessClass,BusinessClassAdmin)
admin.site.register(Business,BusinessAdmin)