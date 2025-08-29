from django.contrib import admin
from .models import Note, Tag
# Register your models here.
@admin.register(Note)
class NoteAdmoin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created']
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']