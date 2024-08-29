from fastapi import FastAPI, File, UploadFile 
import vercel_blob
import dotenv

dotenv.load_dotenv()

app = FastAPI() 

@app.get("/")
def read_root():
    return {"message": "¡Hola vagos 3!!!!"}

@app.post('/upload')
def upload(file: UploadFile = File(...)):
    print("recibido") 
    vercel_blob.put(file.filename, file.file.read(), {})
    return {"message": "Archivo recibido"}