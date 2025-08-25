from django.contrib import admin
from .models import Genealogy, Council, Department


class CouncilInline(admin.TabularInline):
    model = Council
    extra = 1


class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1


@admin.register(Genealogy)
class GenealogyAdmin(admin.ModelAdmin):
    list_display = ("id", "title_name")
    inlines = [CouncilInline]  # Genealogy ostida Council qo‘shib bo‘lasiz


@admin.register(Council)
class CouncilAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "rector")
    list_filter = ("rector",)
    search_fields = ("title",)
    inlines = [DepartmentInline]  # Council ostida Department qo‘shib bo‘lasiz


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "council", "parent", "row", "order")
    list_filter = ("council",)
    search_fields = ("title",)