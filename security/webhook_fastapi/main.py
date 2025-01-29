import uvicorn

from fastapi import FastAPI, Query, Header, Cookie, Body, Path, status, Request
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from typing import Annotated, Union
from pydantic import BaseModel

from pprint import pprint
import json, io

app = FastAPI()
# app.add_middleware(HTTPSRedirectMiddleware)


# pydantic 이라면 http 바디로 해석된다.
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
def read_root(header: Union[str, None] = Header(default=None, convert_underscores=True) , body = Body):
    print(header)
    print(body)
    return {
            "header": header,
            "body": body
    }

@app.post("/audit/")
async def fetch_audit(
    timeout: str, 
    # header: Union[str, None] = Header(default=None) , 
    body = Body,
    # request: Request
):
    print('this is timeout second of api server: ', timeout)

    # body: dict = json.load(io.BytesIO(await request.body()))
    pprint(body())
    return { }

@app.post("/items/")
def create_items(item: Item):
    return item

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        port=8000, 
        host='192.168.80.1', 
        reload=True, 
        ssl_keyfile= 'pki/webhook.key',
        ssl_certfile= 'pki/webhook.crt',
    )
