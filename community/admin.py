from django.contrib import admin

from community.models import CommunityResource, CommunityResourceGroup


@admin.register(CommunityResourceGroup)
class CommunityResourceGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority')
    search_fields = ('name',)
    ordering = ('-priority',)
    list_filter = ('created_at',)


@admin.register(CommunityResource)
class CommunityResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'url', 'color', 'priority')
    search_fields = ('name',)
    ordering = ('-priority',)
    list_filter = ('created_at',)
    list_select_related = ('group',)
