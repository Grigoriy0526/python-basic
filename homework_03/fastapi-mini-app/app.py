from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from views.hello import router as router_ping
from views.items import router as router_items
from views.users import router as router_users

app = FastAPI()

app.include_router(router_ping)
#app.include_router(router_items)
#app.include_router(router_users)


@app.get("/")
def index_page():
    return {"message": "Hello world"}



@app.get("/demo-html", response_class=HTMLResponse)
def demo_html():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Hi</title>
    </head>
    <body>
      <h1>pong</h1>
    </body>
    </html>
    """
