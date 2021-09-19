from django.contrib import admin

# Register your models here.

from firstpage.models import subject

class subjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_code','subject_name','subject_semester','subject_year','subject_seat')

class studentAdmin(admin.ModelAdmin):
    filter_horizontal = ("subjects",)

    
admin.site.register(subject, subjectAdmin)

#admin.site.register(student, studentAdmin)