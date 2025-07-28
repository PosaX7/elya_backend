from django.contrib import admin
from .models import Programme

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('classe', 'matiere', 'periode', 'num_chapitre', 'chapitre')
    list_filter = ('classe', 'matiere', 'periode')
    search_fields = ('chapitre',)
