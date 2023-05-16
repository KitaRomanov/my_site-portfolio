from django.contrib import admin

from blog.models import Publication, PublicationCategory

admin.site.register(PublicationCategory)
admin.site.register(Publication)
