from flask import Blueprint, request, jsonify
import logging

https_bp = Blueprint('https', __name__)

@https_bp.route('/https', methods=['GET', 'POST'])
def https_trigger():
    data = {
        "headers": dict(request.headers),
        "query_params": request.args,
        "request_method": request.method
    }
    logging.info(f"HTTPS Request: {data}")
    
    return jsonify({
        "status": "success",
        "message": "HTTPS request details logged"
    })
