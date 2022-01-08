from fastapi import FastAPI

from routes.file import file_router
from routes.user import user_router
from routes.util import util_router

from fastapi.staticfiles import StaticFiles
import uvicorn



app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/output",StaticFiles(directory="output"),name="output")

app.include_router(user_router, prefix="/user")
app.include_router(file_router,prefix="/file")
app.include_router(util_router,prefix='/util')

if __name__ == "__main__":
    uvicorn.run(app='main:app', host='172.30.40.51', port=8080, reload=True)
