from flask import Flask, Response
from prometheus_client import Counter, generate_latest, Gauge, Histogram, Summary
from flask import jsonify

app = Flask(__name__)

# Prometheus Metrics
request_counter = Counter('my_requests_total', 'Total number of requests.')
cpu_usage = Gauge('cpu_usage_percent', 'Current CPU usage percentage')
request_duration = Histogram('http_request_duration_seconds', 'HTTP request duration in seconds')
response_time = Summary('http_response_time_seconds', 'HTTP response time in seconds')

@app.route('/metrics')
def prometheus_metrics():
    return Response(generate_latest(), mimetype='text/plain')

# Additional endpoint for Grafana
@app.route('/grafana-metrics')
def grafana_metrics():
    # You can customize this endpoint to return metrics in a format suitable for Grafana
    metrics_data = {
        'my_requests_total': request_counter._value.get(),
        'cpu_usage_percent': cpu_usage._value.get(),
        'http_request_duration_seconds_count': request_duration.count,
        'http_response_time_seconds_sum': response_time.sum,
        # Add more metrics as needed
    }
    return jsonify(metrics_data)

@app.route('/')
def hello():
    # Sample code to simulate CPU usage
    cpu_usage.set(30.5)  # Replace with your dynamic CPU usage value

    # Simulate a request with random duration
    import random
    import time
    request_duration.observe(random.uniform(0.1, 2.0))

    # Simulate a response time with random duration
    with response_time.time():
        time.sleep(random.uniform(0.1, 1.0))

    request_counter.inc()
    return "Hello, World! I'm being used for Prometheus and Grafana"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

