# Open Telemetry instrumentation with Flask

https://opentelemetry.io/docs/languages/python/getting-started/

## Run Flask app

```bash
flask run --port 8080
```

In your browser, open: `http://localhost:8080/rolldice`

## Run Flask app with auto-instrumentation

```bash
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    --logs_exporter console \
    --service_name dice-server \
    flask run --port 8080
```
