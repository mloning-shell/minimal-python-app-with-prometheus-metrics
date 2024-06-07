from fastapi import FastAPI
from prometheus_client import make_asgi_app, Summary
import time
import random


# Create app for allowing prometheus server to pull/scrape metrics from app via HTTP requests
app = FastAPI(debug=False)

# Add prometheus asgi middleware to route /metrics requests
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

# Create a metric to track time spent and requests made.
request_timer = Summary("request_processing_seconds", "Time spent processing request")

# Decorate function with metric.
@request_timer.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

@app.get("/hello")
async def root():
    t = random.random()
    process_request(t)
    return {"message": "hello"}

