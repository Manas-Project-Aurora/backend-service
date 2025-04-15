from django.contrib import admin

from board.models import Organization, OrganizationContact, Vacancy
from import_export.admin import ImportExportModelAdmin

@admin.register(Organization)
class OrganizationAdmin(ImportExportModelAdmin):
    pass


@admin.register(OrganizationContact)
class OrganizationContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(ImportExportModelAdmin):
    pass
