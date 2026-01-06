# Space Weather Dashboard

A modern web application for monitoring space weather data from the Australian Bureau of Meteorology (BOM).

## Structure

- `backend/`: FastAPI application that proxies BOM SWS API requests.
- `frontend/`: React + TypeScript + Vite + Tailwind CSS dashboard.
- `archive/`: Old files and LLM-generated chaos preserved for reference.

## Getting Started

### Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Create a `.env` file and add your BOM API key:
   ```
   BOM_API_KEY=your_key_here
   ```
4. Run the server:
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`.

### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
   The dashboard will be available at `http://localhost:5173`.

## Features

- Real-time fetching of A-Index, K-Index, and Dst-Index.
- Modern dark-themed UI with Tailwind CSS 4.
- Clean, modular codebase replacing previous iterations.