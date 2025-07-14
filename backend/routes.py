from flask import Blueprint, request, jsonify
from models import Bug
from database import db

bug_routes = Blueprint("bugs", __name__)

@bug_routes.route("/api/bugs", methods=["GET"])
def get_bugs():
    bugs = Bug.query.all()
    return jsonify([{
        "id": bug.id,
        "title": bug.title,
        "status": bug.status
    } for bug in bugs])

@bug_routes.route("/api/bugs", methods=["POST"])
def create_bug():
    data = request.json
    new_bug = Bug(
        title=data.get("title"),
        description=data.get("description"),
        status="Open",  # default status
        assigned_to=data.get("assigned_to")  # user ID
    )
    db.session.add(new_bug)
    db.session.commit()
    return jsonify({"message": "Bug created", "bug_id": new_bug.id}), 201

@bug_routes.route("/api/bugs/<int:bug_id>", methods=["PUT"])
def update_bug(bug_id):
    bug = Bug.query.get(bug_id)
    if not bug:
        return jsonify({"error": "Bug not found"}), 404

    data = request.json

    if "title" in data:
        bug.title = data["title"]
    if "description" in data:
        bug.description = data["description"]
    if "status" in data:
        bug.status = data["status"]

    db.session.commit()

    return jsonify({"message": "Bug updated"})

