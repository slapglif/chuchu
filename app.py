from flask import Flask, request, jsonify
from models import db, Place, Event, Booking

app = Flask(__name__)


@app.route("/api/places", methods=["GET", "POST"])
def places():
    if request.method == "GET":
        return jsonify(db.query(Place).all())
    if request.method == "POST":
        for r in request.data:
            Place.get_or_create(r)
        return jsonify({"response": "success"})


@app.route('/api/places/<id>', methods=["GET"])
def places_by_id(id):
    if request.method == "GET":
        return jsonify(db.query(Place).filter_by(PlaceId=id))


@app.route('/api/events/<id>', methods=["GET"])
def event_by_id(id):
    if request.method == "GET":
        return jsonify(db.query(Event).filter_by(EventId=id))


@app.route('/api/events/', methods=["GET", "POST"])
def events():
    if request.method == "POST":
        for r in request.data:
            Event.get_or_create(r)
        return jsonify({"response": "success"})


if __name__ == '__main__':
    app.run()
