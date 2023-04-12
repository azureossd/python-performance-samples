import azure.functions as func
import os, time
import aiofiles

app = func.FunctionApp()

#Global variables
num = 1
custom_list = []

#Custom Methods
def firstMethod():
    secondMethod() #Calling secondMethod
    return "I am done here"

def secondMethod():
    thirdMethod(2.5) #Calling thirdMethod 
    for loop in range(1): #CPU time spent
        for index in range(121474838):
            num * index
    thirdMethod(5) #Calling thirdMethod again

def thirdMethod(n):
    time.sleep(n) #Sleep

def generate_data(num):
    numbers = int(num/8)
    data = []
    i=0
    for i in range(numbers):
        i=i+1
        data.append(i)
    return data

def readFileSync(filename):
    with open(filename) as f:
        content = f.read()
    return content

async def readFileAsync(filename):
    async with aiofiles.open(filename, mode='r') as f:
        content = await f.read()
    return content

#Functions
@app.function_name(name="cpu")
@app.route(route="cpu") 
def cpu_function(req: func.HttpRequest) -> func.HttpResponse:
    result = firstMethod()
    return func.HttpResponse(result)

@app.function_name(name="memory")
@app.route(route="memory") 
def memory_function(req: func.HttpRequest) -> func.HttpResponse:
    num = 20000 * 1024
    data = generate_data(num)
    custom_list.append(data)
    custom_list.append(custom_list)
    return func.HttpResponse("I am done here")

@app.function_name(name="sync")
@app.route(route="sync") 
def sync_function(req: func.HttpRequest) -> func.HttpResponse:
    content = readFileSync("content.txt")
    return func.HttpResponse(content)

@app.function_name(name="async")
@app.route(route="async") 
async def async_function(req: func.HttpRequest) -> func.HttpResponse:
    content = await readFileAsync("content.txt")
    return func.HttpResponse(content)
    