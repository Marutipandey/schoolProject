from django.contrib import admin
from .models import studentDetails
# Register your models here.
@admin.register(studentDetails)
class studentDetailsAdmin(admin.ModelAdmin):
    list_display = ['Name','Father_name','Mother_name','Class','Email','Contact_number','Address']