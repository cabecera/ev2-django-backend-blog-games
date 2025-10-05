from django.contrib import admin
from .models import Comunidad

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Comunidad,ProjectAdmin)

