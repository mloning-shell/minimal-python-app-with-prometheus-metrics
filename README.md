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
docker-compose --file ./docker/docker-compose.yml up --build
```

* For the app, go to: `http://localhost:5000/docs/`
* For the Prometheus UI, go to: `http://localhost:9090/`

We use `docker-compose` to run our app and Prometheus in a container network. 
In `prometheus.yml`, we configure Prometheus to pull metrics from our app, using the app name and port from the `docker-compose.yml` file as a target.

## Run the app on Kubernetes with Prometheus

* install loki-stack Helm chart in k8s
* build and push app Docker image
* install app in k8s
* use port-forwarding to see app
* use port-forwarding to see Prometheus UI

We use [annotations](https://artifacthub.io/packages/helm/prometheus-community/prometheus#scraping-pod-metrics-via-annotations) on our app in `deployment.yaml` to configure Prometheus to pull metrics from our app.

## TODO

- [ ] run multiple processes in app, all exposing metrics to /metrics endpoint
- [ ] deploy to k8s
