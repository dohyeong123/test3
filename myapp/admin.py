from django.contrib import admin
from .models import Member
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'member_name', 'member_code', 'attend')

admin.site.register(Member, MemberAdmin)