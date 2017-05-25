from django.contrib import admin
from instructors.models import Instructor,Position,Course
from django.db import models
from django.forms import widgets
# Register your models here.


class InstructorInline(admin.StackedInline):
    model = Instructor
    fields = ["name","surname"]

class PositionAdmin(admin.ModelAdmin):
    inlines = [InstructorInline]

class InstructorAdmin(admin.ModelAdmin):
    list_display = ["name","surname","is_active","position"]
    list_display_links = ["name","surname"]

    list_filter = ["is_active","position"]
    search_fields = ["name","surname"]
    list_editable = ["is_active"]
    # fields = ["name","surname","email","position","is_active","date_of_birthday"]
    # exclude = []
    readonly_fields = ['is_active']
    raw_id_fields = ['position']
    save_as = True
    save_on_top = True
    fieldsets = [
        (None,{'fields':['name','surname']}),
        ('Other information',{'fields':['email','date_of_birthday',
                                        'position','is_active'],'classes':['collapse']}),
    ]
    formfield_overrides = {
        models.DateField:{'widget':widgets.TextInput}
    }
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Position,PositionAdmin)
admin.site.register(Course)




