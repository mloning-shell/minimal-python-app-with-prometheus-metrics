# Minimal Python app with Prometheus metrics collection

## Run the app locally

This requires a local Python environment with Python version 3.11 and all requirements: `pip install -r app/requirements.txt`. 

```bash
fastapi run app/app.py --port 5000
```

* For the app, go to: `http://localhost:5000/docs/`

This app has a simple `/hello` endpoint and a `/metrics` endpoint to allow Prometheus to pull metrics.

## Run the app locally with Prometheus

```bash
docker-compose --file docker/docker-compose.yml up --build
```

* For the app, go to: `http://localhost:5000/docs/`
* For the Prometheus UI, go to: `http://localhost:9090/`

We use `docker-compose` to run our app and Prometheus in a container network. 
In `prometheus.yml`, we configure Prometheus to pull metrics from our app, using the app name and port from the `docker-compose.yml` file as a target.

## Run the app on Kubernetes with Prometheus

TODO
