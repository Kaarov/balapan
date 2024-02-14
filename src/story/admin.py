from django.contrib import admin

from .models import Story, TextModel


class TextModelAdmin(admin.TabularInline):
    model = TextModel
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Story)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    inlines = [TextModelAdmin]

    def has_delete_permission(self, request, obj=None):
        return False
