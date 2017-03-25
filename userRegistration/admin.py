from django.contrib import admin


from .models import (CompanyProfile, OpeningDetails)

admin.site.register(CompanyProfile)
admin.site.register(OpeningDetails)
