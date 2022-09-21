from django.contrib import admin
from .models import Catergory
# Register your models here.


class CatergoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')


admin.site.register(Catergory, CatergoryAdmin)
