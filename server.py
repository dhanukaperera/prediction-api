from flask import Flask, jsonify,request
import mlmodel

app = Flask(__name__)

@app.route("/",methods=['GET'])
def main():
    return 'Explore-Eco Prediction API running...'

@app.route("/getMonthlyPreditions",methods=['POST'])
def getMothlyPredictions():
    if request.method  == 'POST':
        result = request.form
        _area = result.get('area')
        _month = result.get('month')
        if _area != None and _month != None:
            if _area == 'COLOMBO_CITY':
                result = mlmodel.getColomboCityMonthlyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'GREATER_COLOMBO':
                result = mlmodel.getGreaterColomboMonthlyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'SOUTH_COAST':
                result = mlmodel.getSouthCoastMonthlyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'EAST_COST':
                result = mlmodel.getEastCoastMonthlyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'HIGH_COUNTRY':
                result = mlmodel.getHighCountryMonthlyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'ANCIENT_CITIES':
                result = mlmodel.getAncientCitiesMonthlyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'NORTHERN_REGIONS':
                result = mlmodel.getNorthernRegionsMonthlyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            else:
                resp = jsonify("Error")
                resp.status_code = 404
                return resp
        else:
            resp = jsonify("Error")
            resp.status_code = 404
            return resp
    return

@app.route("/getDailyPreditions",methods=['POST'])
def getDailyPredictions():
    if request.method  == 'POST':
        result = request.form
        _area = result.get('area')
        _month = result.get('date')
        if _area != None and _month != None:
            if _area == 'COLOMBO_CITY':
                result = mlmodel.getColomboDailyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'GREATER_COLOMBO':
                result = mlmodel.getGreaterColomboDailyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'SOUTH_COAST':
                result = mlmodel.getSouthCoastDailyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'EAST_COST':
                result = mlmodel.getEastCoastDailyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'HIGH_COUNTRY':
                result = mlmodel.getHighCountryDailyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'ANCIENT_CITIES':
                result = mlmodel.getAncientCitiesDailyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            elif _area == 'NORTHERN_REGIONS':
                result = mlmodel.getNorthernRegionsDailyPredictions()
                resp = jsonify(result)
                resp.status_code = 200
                return resp
            else:
                resp = jsonify("Error")
                resp.status_code = 404
                return resp
        else:
            resp = jsonify("Bad Input")
            resp.status_code = 404
            return resp
    return

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)