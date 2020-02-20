from django.contrib import admin
from .models import dataSolar



# admin.site.register(dataSolar)

class dataSolarAdmin(admin.ModelAdmin):
	list_display=('voltage','currents','power','hourly', 'intensity', 'temp')

admin.site.register(dataSolar, dataSolarAdmin)
