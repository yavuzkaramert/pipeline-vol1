from flask import Flask, jsonify # type: ignore
from prometheus_flask_exporter import PrometheusMetrics # type: ignore

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return jsonify({"message": " MESUT KAHPEDIR :D "})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

