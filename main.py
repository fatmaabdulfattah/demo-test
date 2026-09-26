from fastapi import FastAPI

app = FastAP

@.get("/health")
 health()
    data = {"status": "ok"}
    return data

@.get("/")
 root()
    return {"message": "Hello"}

if __name__ == "__main__":
    import uvicornn
    uvicorn.run(app, host="0.0.0.0", port=8000)