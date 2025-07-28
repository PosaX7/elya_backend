from django.contrib import admin
from .models import QuizCategory, QuizSubGroup, DifficultyLevel, Quiz, QuizQuestion, QuizAnswer, QuizResult

class QuizAnswerInline(admin.TabularInline):
    model = QuizAnswer
    extra = 4

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'correct_answer_number')
    inlines = [QuizAnswerInline]

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subgroup', 'difficulty')
    list_filter = ('category', 'subgroup', 'difficulty')
    search_fields = ('title',)

admin.site.register(QuizCategory)
admin.site.register(QuizSubGroup)
admin.site.register(DifficultyLevel)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizQuestion, QuizQuestionAdmin)
admin.site.register(QuizAnswer)
admin.site.register(QuizResult)
