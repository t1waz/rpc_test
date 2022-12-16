from django.conf import settings

from backend.containers import Container


container = Container()
container.config.from_dict(settings.__dict__)
