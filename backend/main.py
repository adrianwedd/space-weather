from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Space Weather API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = "https://sws-data.sws.bom.gov.au/api/v1"
API_KEY = os.getenv("BOM_API_KEY")

def fetch_bom_data(endpoint: str, params: dict = None):
    url = f"{BASE_URL}/{endpoint}"
    # Note: If an API key is required, it usually goes in headers or params.
    # The archived code used HEADERS = {"Content-Type": "application/json"} but didn't show the key being used in the actual request in the snippet I saw.
    # However, it mentioned an api_key variable.
    headers = {"Content-Type": "application/json"}
    if API_KEY:
        params = params or {}
        params["api_key"] = API_KEY # Assuming it's a query param, adjust if it should be a header
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from BOM: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "Space Weather API is running"}

@app.get("/api/a-index")
def get_a_index():
    return fetch_bom_data("get-a-index")

@app.get("/api/k-index")
def get_k_index(location: str = None):
    params = {"location": location} if location else {}
    return fetch_bom_data("get-k-index", params=params)

@app.get("/api/dst-index")
def get_dst_index():
    return fetch_bom_data("get-dst-index")

@app.get("/api/alerts/magnetic")
def get_magnetic_alerts():
    return fetch_bom_data("get-mag-alert")

@app.get("/api/warnings/magnetic")
def get_magnetic_warnings():
    return fetch_bom_data("get-mag-warning")

@app.get("/api/alerts/aurora")
def get_aurora_alerts():
    return fetch_bom_data("get-aurora-alert")

@app.get("/api/watch/aurora")
def get_aurora_watch():
    return fetch_bom_data("get-aurora-watch")

@app.get("/api/outlook/aurora")
def get_aurora_outlook():
    return fetch_bom_data("get-aurora-outlook")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
