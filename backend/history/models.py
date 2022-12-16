import uuid

from django.db import models


class ScrapResult(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)

    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


class InvalidScrapJobs(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    request_meta = models.JSONField()
