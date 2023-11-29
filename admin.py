from django.contrib import admin
from app1.models import Branch, Email, Home, Section, Year
from app1.models import Attendance
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Home)
class PersonAdmin(ImportExportModelAdmin):
   pass
admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(Section)

@admin.register(Email)
class PersonAdmin(ImportExportModelAdmin):
   pass
@admin.register(Attendance)
class PersonAdmin(ImportExportModelAdmin):
   pass
