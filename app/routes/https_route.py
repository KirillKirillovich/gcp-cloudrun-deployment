from flask import Blueprint, request, jsonify
import logging

https_bp = Blueprint('https', __name__)

@https_bp.route('/https', methods=['GET', 'POST'])
def https_trigger():
    logging.info(f"Headers: {request.headers}")
    logging.info(f"Query Params: {request.args}")
    logging.info(f"Request Method: {request.method}")
    logging.info(f"Body: {request.get_json()}")
    
    return jsonify({
        "status": "success",
        "message": "HTTPS request details logged"
    })
