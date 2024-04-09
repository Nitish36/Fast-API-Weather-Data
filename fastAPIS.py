from fastapi import FastAPI,Path
import json
import uvicorn
app = FastAPI()

@app.get("/get")
def home():
    with open('LiveWeatherData.json', 'r') as file:
        jsoneddata = json.load(file)
        return jsoneddata
if __name__ == "__main__":
    uvicorn.run("fastAPIS:app", host="127.0.0.1", port=10000, log_level="info")