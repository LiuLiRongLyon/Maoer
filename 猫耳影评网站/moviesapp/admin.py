from django.contrib import admin
from .models import MoviesInfo,UserInfo,Reviews,Tag
# Register your models here
class MoviesInfoAdmin(admin.ModelAdmin):
    list_display = ('name','actor','time','score','category','critics_num')
    list_display_links = ('name')
    list_editable = ('score','category','critics_num')
    list_filter = ('is_notice')

admin.site.register(MoviesInfo)
admin.site.register(UserInfo)
admin.site.register(Reviews)
admin.site.register(Tag)