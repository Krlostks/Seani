from django.contrib import admin
from .models import Module, Question
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk','question_text', 'module', 'correct']
    list_filter = ['module']

class QuestionInLine(admin.StackedInline):
    model = Question


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_questions']
    inlines = [QuestionInLine]