
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TranslationTabularInline

from model_search.models import SearchTag, SearchTagGroup, SearchQuery


class SearchTagInline(TranslationTabularInline):
    fields = ['text']
    model = SearchTag


@admin.register(SearchTagGroup)
class SearchTagGroupAdmin(admin.ModelAdmin):

    inlines = [SearchTagInline]

    list_display = ['name', 'get_latest_tag_names']

    def get_latest_tag_names(self, obj):
        return ', '.join(
            obj.tags.all().order_by('-id')[:5].values_list('text', flat=True))

    get_latest_tag_names.short_description = _('Latest tags')


@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False
