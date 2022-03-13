from django.contrib import admin
from .models import Biography, Education, Projects_photos, Publications_photos, Photo

admin.site.register(Photo)
admin.site.register(Biography)
admin.site.register(Education)
admin.site.register(Projects_photos)
admin.site.register(Publications_photos)
