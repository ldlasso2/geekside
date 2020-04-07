from django.contrib import admin
from .models import Post

#admin.site.register(Post)
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','excerpt', 'is_active')
    list_filter= ['is_active']
    exclude=['is_active']