from django.contrib import admin

from .models import State
from .models import Student
from .models import Marks




class StateAdmin(admin.ModelAdmin):
    sta_display = ('state_and_UTs', 'state_id')
    sta_filter = ('state_id',)
    search_fields = ('state_and_UTs', 'state_id',)

admin.site.register(State,StateAdmin)
# Register your models here.

class StudentAdmin(admin.ModelAdmin):

    stu_display = ('name', 'roll_number','state_id')
    stu_filter = ('name','roll_number')
    search_fields = ('roll_number',)

admin.site.register(Student,StudentAdmin)
# Register your models here.

class MarksAdmin(admin.ModelAdmin):
    mrk_display = ('roll_number', 'english','hindi','science','physics')
    stu_filter = ('roll_number',)
    search_fields = ('roll_number',)

admin.site.register(Marks,MarksAdmin)