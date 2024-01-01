from fastapi import FastAPI

from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.post("/process")
async def process(
    input:str,
    ):
    return {"response": input}


@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    ):
    return {
    "file": file,
    }


@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile,
    ):
    return {
    "file_name": file.filename,
    "file_contnet": file.file.read(),
    }