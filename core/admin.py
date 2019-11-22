from django.contrib import admin
from .models import Pro, Usuario

# Register your models here.

class StartAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]
    list_filter = ["stock"]


admin.site.register(Pro, StartAdmin)
admin.site.register(Usuario)


 
