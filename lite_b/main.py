from blacksheep import Application
import settings
import grpc
from utils.grpc import services_pb2
from utils.grpc import services_pb2_grpc


app = Application()

channel = grpc.insecure_channel('scrap:50051')
stub = services_pb2_grpc.ScrapServiceStub(channel)


@app.route(settings.LOADERIO_URL)
async def loader_io_token():
    return settings.LOADERIO_TOKEN


@app.route('/scrap/')
async def home():
    auth_response = stub.AuthLaunchUrl(services_pb2.LaunchUrlData(params={'foo': 'bar'}))
    # print(auth_response)
    return 'Hello, World!'
