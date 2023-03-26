from django.contrib import admin

from .models import Question, Choice

admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Question)
class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


