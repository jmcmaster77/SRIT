from fastapi import FastAPI
from fastapi import APIRouter
from routes.Auth import auth
from routes.consulta import consulta
import uvicorn

app = FastAPI()

app.include_router(auth)
app.include_router(consulta)


if __name__ == '__main__':
    config = uvicorn.Config("main:app", port=5000,
                            log_level="info", reload=True)
    server = uvicorn.Server(config)

    server.run()

    # uvicorn.run(app, host='127.0.0.1', port=5000)
