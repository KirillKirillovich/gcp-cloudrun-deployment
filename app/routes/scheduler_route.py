from flask import Blueprint, request, jsonify
import logging

scheduler_bp = Blueprint('scheduler', __name__)

@scheduler_bp.route('/scheduler', methods=['POST'])
def scheduler_trigger():
    timestamp = request.headers.get('X-Scheduler-Timestamp', 'Not Provided')
    
    logging.info(f"Timestamp: {timestamp}")
    logging.info(f"Payload Data: {request.get_json()}")
    
    return jsonify({
        "status": "success",
        "message": "Scheduler job details logged"
    })
