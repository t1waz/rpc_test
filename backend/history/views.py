from dependency_injector.wiring import (
    inject,
    Provide,
)
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.containers import Container
from backend.rpc import ScrapRpcClient
from history.models import (
    ScrapResult,
    InvalidScrapJobs,
)
from utils.models import GetDataResponse


class ScrapView(APIView):
    @inject
    def get(
        self,
        request: HttpRequest,
        scrap_rpc_client: ScrapRpcClient = Provide[Container.scrap_rpc_client],
    ) -> Response:
        try:
            content_response = scrap_rpc_client.process_scrap()
        except Exception as e:
            content_response = GetDataResponse(is_valid=False, content='')

        if content_response.is_valid:
            ScrapResult.objects.create(content=content_response.content)
            return Response(status=200, data={})

        InvalidScrapJobs.objects.create(request_meta=request.META)
        return Response(status=400, data={})

