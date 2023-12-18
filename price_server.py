import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi import Body
from pydantic import BaseModel

APP_PORT = 8000

app = FastAPI(
    description="This is a price query service for a private hardware vendor, which returns a quotation based on the product model",
    servers=[{"url": f"http://localhost:{APP_PORT}"}],
)


class Cpu(BaseModel):
    model: str


class Gpu(BaseModel):
    model: str


@app.post("/cpu/price")
def get_cpu_price(cpu: Cpu):
    """Given a CPU model, return the price"""
    if "i3" in cpu.model:
        return {"price": 1000, "model": cpu.model}
    elif "i5" in cpu.model:
        return {"price": 5000, "model": cpu.model}
    elif "i7" in cpu.model:
        return {"price": 15000, "model": cpu.model}
    elif "i9" in cpu.model:
        return {"price": 20000, "model": cpu.model}
    else:
        raise HTTPException(status_code=404, detail="Model not found")


@app.post("/gpu/price")
def get_gpu_price(gpu: Gpu):
    """Given a GPU model, return the price"""
    if gpu.model.startswith("gtx"):
        return {"price": 10000, "model": gpu.model}
    elif gpu.model.startswith("rtx"):
        return {"price": 30000, "model": gpu.model}
    elif gpu.model.startswith("titan"):
        return {"price": 50000, "model": gpu.model}
    else:
        raise HTTPException(status_code=404, detail="Model not found")


if __name__ == "__main__":
    uvicorn.run("price_server:app", port=APP_PORT, reload=True)
