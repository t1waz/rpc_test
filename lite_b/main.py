from blacksheep import Application
import settings


app = Application()


@app.route(settings.LOADERIO_URL)
async def loader_io_token():
    return settings.LOADERIO_TOKEN


@app.route('/scrap/')
async def home():
    return 'Hello, World!'
