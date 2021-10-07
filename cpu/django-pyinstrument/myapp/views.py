from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import json
from ftfy import fix_text

def getNumberOfRows(num):
    dataset = pd.read_csv("users.csv")
    results = dataset.loc[1:num, ['User Name','Display Name']].to_json(orient='records')
    return json.dumps(results)
	
def savingToJson(filename, results):
    filehandle = open(filename, "a+")
    filehandle.writelines(results)
    filehandle.seek(0)
    filehandle.close()

def homePageView(request):
    results = getNumberOfRows(3000)
    formated_data = json.loads(fix_text(results))
    savingToJson("formated_users.json", formated_data)
    return render(request, 'home/index.html', {'msg':'Hello World'})
