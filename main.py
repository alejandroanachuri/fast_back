from fastapi import FastAPI, File, UploadFile 
import vercel_blob


app = FastAPI() 

@app.get("/")
def read_root():
    return {"message": "¡Hola vagos!!!!"}

@app.post('/upload')
def upload(file: UploadFile = File(...)):
    vercel_blob.put(file.filename, file.read(), {})
    return {"message": "Archivo recibido"}