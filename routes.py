from flask import Blueprint, jsonify, request
from models import db, Episode, Guest, Appearance

api = Blueprint('api', __name__)

# GET all episodes
@api.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        "id": episode.id,
        "date": episode.date,
        "number": episode.number
    } for episode in episodes])

# GET a specific episode by ID
@api.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        appearances = [{
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id,
            "guest": {
                "id": appearance.guest.id,
                "name": appearance.guest.name,
                "occupation": appearance.guest.occupation
            }
        } for appearance in episode.appearances]

        return jsonify({
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": appearances
        })
    return jsonify({"error": "Episode not found"}), 404

# DELETE an episode by ID
@api.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    if episode:
        try:
            db.session.delete(episode)
            db.session.commit()
            return jsonify({"message": "Episode deleted successfully"}), 204
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "An error occurred while deleting the episode"}), 500
    return jsonify({"error": "Episode not found"}), 404

# GET all guests
@api.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        "id": guest.id,
        "name": guest.name,
        "occupation": guest.occupation
    } for guest in guests])

# POST to create a new appearance
@api.route('/appearances', methods=['POST'])
def create_appearance():
    json_data = request.get_json()

    if not json_data or not all(k in json_data for k in ("rating", "episode_id", "guest_id")):
        return jsonify({"error": "Missing data"}), 400

    appearance = Appearance(
        rating=json_data.get("rating"),
        episode_id=json_data.get("episode_id"),
        guest_id=json_data.get("guest_id")
    )
    
    try:
        db.session.add(appearance)
        db.session.commit()
        return jsonify({
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id,
            "episode": {
                "date": appearance.episode.date,
                "id": appearance.episode.id,
                "number": appearance.episode.number
            },
            "guest": {
                "id": appearance.guest.id,
                "name": appearance.guest.name,
                "occupation": appearance.guest.occupation
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while creating the appearance"}), 500
