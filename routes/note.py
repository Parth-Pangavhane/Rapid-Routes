from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from config.db import conn
from fastapi.templating import Jinja2Templates
from schemas.note import noteEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.data.data.find({})
    data = []
    for doc in data:
        data.append({
            "_id": data["_id"],
            "title": data["title"],
            "desc": data["desc"],
            "important": doc["important"]
        })
    return templates.TemplateResponse(
        request=request, name="index.html", context={"data": data}
    )


@note.post("/", response_class=HTMLResponse)
async def create_item(request:Request):
    form = await request.form()
    data = conn.data.data.insert_one(form)
    return {"Success" : True}
