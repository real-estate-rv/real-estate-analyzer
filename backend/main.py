from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Real Estate Analyzer", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/v1/properties")
async def get_properties(skip: int = 0, limit: int = 10):
    return {"properties": [], "total": 0}

@app.post("/api/v1/scrape/search")
async def scrape_search(city: str, state: str):
    return {"status": "scraping_started", "city": city, "state": state}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
