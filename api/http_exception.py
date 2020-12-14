from flask import abort, jsonify


def http_exception(statu_code=500, message='Error', data=''):
    abort(statu_code, message)
    return jsonify({
        'status': 'error',
        'data': data,
    })


def bad_request(message='BadRequest', data=''):
    return http_exception(500, message, data)


def not_found(message='NotFound', data=''):
    return http_exception(400, message, data)


def forbidden(message='Forbidden', data=''):
    return http_exception(403, message, data)
