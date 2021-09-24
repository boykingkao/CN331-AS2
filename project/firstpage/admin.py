from django.contrib import admin

# Register your models here.

from firstpage.models import Subject

class subjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_code','subject_name','subject_semester','subject_year','subject_seat','status')

class studentAdmin(admin.ModelAdmin):
    filter_horizontal = ("subjects",)

    
admin.site.register(Subject, subjectAdmin)

#admin.site.register(student, studentAdmin)