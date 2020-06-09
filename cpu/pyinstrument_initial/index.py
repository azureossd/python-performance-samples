
import bottle, json
import pandas as pd
from bottle import route, run
from ftfy import fix_text

@route('/')
def index():
    results = getNumberOfRows(3000)
    formated_data = json.loads(fix_text(results))
    savingToJson("formated_users.json", formated_data)
    return formated_data

def getNumberOfRows(num):
    dataset = pd.read_csv("users.csv")
    results = dataset.loc[1:num, ['User Name','Display Name']].to_json(orient='records')
    return json.dumps(results)
	
def savingToJson(filename, results):
    filehandle = open(filename, "a+")
    filehandle.writelines(results)
    filehandle.seek(0)
    filehandle.close()
	
if __name__ == '__main__':
	run()
	
app = bottle.default_app()
