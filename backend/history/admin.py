from django.contrib import admin

from history import models


admin.site.register(models.ScrapResult)
admin.site.register(models.InvalidScrapJobs)
