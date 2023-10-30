import azure.functions as func
import logging
import json
import prediction_2
import outliers

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger_fdm_wqp")
def http_trigger_fdm_wqp(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()

    pH = req_body.get('pH')
    iron = req_body.get('iron')
    nitrate = req_body.get('nitrate')
    chloride = req_body.get('chloride')
    color = req_body.get('color')
    turbidity = req_body.get('turbidity')
    fluoride = req_body.get('fluoride')
    copper = req_body.get('copper')
    odor = req_body.get('odor')
    sulfate = req_body.get('sulfate')
    conductivity = req_body.get('conductivity')
    chlorine = req_body.get('chlorine')
    manganese = req_body.get('manganese')
    totalDissolvedSolids = req_body.get('totalDissolvedSolids')
    waterTemp = req_body.get('waterTemp')
    airTemp = req_body.get('airTemp')
    day = req_body.get('day')
    month = req_body.get('month')

    values = [pH, iron, nitrate, chloride, color, turbidity, fluoride, copper, odor, sulfate, conductivity, chlorine, manganese, totalDissolvedSolids, waterTemp, airTemp, month, day]

    range = [(5,8.5),(0.3,10),(0,100),(0,250),None,(0.5,1),(1e-6,1.5),(5e-4,1),(2,130),(2e-3,0.13),(0,250),(200,800),(0.2,6),(0,700),(0,100),(4,35),None,(1,31)]

    res = prediction_2.predict(values)

    outlier_list = outliers.outliers(values,range)
    response_dict = dict()
    
    if(res[0] == 0):
        response_dict['prediction'] = "This water sample is not suitable"
        response_dict['outliers'] = outlier_list
        return func.HttpResponse(json.dumps(response_dict), mimetype="application/json")
    
    elif(res[0] == 1):
        response_dict['prediction'] = "This water sample is suitable"
        response_dict['outliers'] = outlier_list
        return func.HttpResponse(json.dumps(response_dict), mimetype="application/json")
        
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    

@app.route(route="http_trigger_test", auth_level=func.AuthLevel.FUNCTION)
def http_trigger_test(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
