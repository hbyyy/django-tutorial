from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

# admin.site.register(Question, QuestionAdmin)


# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     pass
