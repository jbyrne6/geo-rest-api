from flask import Flask, jsonify, request
from shapely.geometry import Polygon

app = Flask(__name__)

@app.route('/')
def geo_rest_api():
    return 'Geo REST API'

@app.route('/polygons-intersect', methods=['POST'])
def checkPolygonIntersection():

    data = request.get_json()
    polygon_1 = data['features'][0]
    polygon_2 = data['features'][1]
    # intersects = polygon_1.intersects(polygon_2)
    intersects = True

    return jsonify({'polygon_1' : polygon_1, 'polygon_2' : polygon_2})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)