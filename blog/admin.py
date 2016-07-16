from django.contrib import admin

# Register your models here.
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
	list_display = ['title', 'timestamp','updated']
	list_display_links = ['title']
	list_filter = ['timestamp','updated']
	search_fields = ['title']
	# list_editable = ['title']
	class Meta:
	 	model = Blog


admin.site.register(Blog,BlogAdmin)