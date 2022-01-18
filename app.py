from flask import Flask, jsonify, request
from arcgis.geometry import Polygon

app = Flask(__name__)

@app.route('/')
def geo_rest_api():
    return 'Geo REST API'

@app.route('/polygons-intersect', methods=['POST'])
def checkPolygonIntersection():
    # geojson data -> json
    data = request.get_json()

    # polygons being compared for intersection
    polygon_1 = Polygon(data['features'][0]["geometry"])
    polygon_2 = Polygon(data['features'][1]["geometry"])

    #  boolean value for if polygons intersect or not
    # geom_intersection = polygon_1.intersect(second_geometry=polygon_2, dimension=4)
    geom_intersection = polygon_1.overlaps(polygon_2)

    # return boolean polygon intersection result via json
    return jsonify({'intersection' : geom_intersection})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)