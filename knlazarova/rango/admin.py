from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(UserProfile)

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
#admin.site.register(Page)

#admin.site.register(Category)
admin.site.register(Page, PageAdmin)
# Register your models here.


    
