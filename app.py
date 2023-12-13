# save this as app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Software Enginner',
    'location': 'New York, USA',
    'salary': '199000'
}, {
    'id': 2,
    'title': 'Software Developer',
    'location': 'Kabul, Afghanistan',
    'salary': '130000'
}, {
    'id': 3,
    'title': 'Data Analyist',
    'location': 'Kunduz, Afghanistan',
    'salary': '170000'
}, {
    'id': 4,
    'title': 'Senior HR Officer',
    'location': 'Jalalabad, Afghanistan',
    'salary': '120000'
}]


@app.route("/")
def home():
  return render_template("home.html", jobs=JOBS)


@app.route('/api/jobs')
def jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
