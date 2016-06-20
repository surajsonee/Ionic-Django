from django.contrib import admin
from .models import Team, Kpi, KpiValue, Organization
# Register your models here.



@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Kpi)
class KpiAdmin(admin.ModelAdmin):
    pass

@admin.register(KpiValue)
class KpiAdmin(admin.ModelAdmin):
    pass