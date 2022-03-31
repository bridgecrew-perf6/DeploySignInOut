from django.contrib import admin
from .models import ClassForm, period1, period2, period3, period4

@admin.register(ClassForm)
class ClassFormAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(period1)
class period1Admin(admin.ModelAdmin):
    list_display = ('Student', 'Teacher', 'signedOutTime', 'signedInTime', 'Status')
    search_fields = ('EachPersonData', 'Student')
    list_filter = ('Teacher',)
    # date_hierarchy = 'dateOfSubmission'

@admin.register(period2)
class period2Admin(admin.ModelAdmin):
    list_display = ('Student', 'Teacher', 'signedOutTime', 'signedInTime', 'Status')
    search_fields = ('EachPersonData', 'Student')
    list_filter = ('Teacher',)

@admin.register(period3)
class period3Admin(admin.ModelAdmin):
    list_display = ('Student', 'Teacher', 'signedOutTime', 'signedInTime', 'Status')
    search_fields = ('EachPersonData', 'Student')
    list_filter = ('Teacher',)

@admin.register(period4)
class period4Admin(admin.ModelAdmin):
    list_display = ('Student', 'Teacher', 'signedOutTime', 'signedInTime', 'Status')
    search_fields = ('EachPersonData', 'Student')
    list_filter = ('Teacher',)



