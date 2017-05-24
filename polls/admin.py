# -*- coding: utf-8 -*-

"""polls administration."""

from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    """polls question answer choice inline admin form."""

    model = Choice
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """polls questions admin form."""

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = (
        'question_text',
        'pub_date',
        'was_published_recently',
    )
    list_per_page = 50
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]
