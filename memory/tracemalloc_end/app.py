from flask import Flask, jsonify
import os,json
import tracemalloc

app = Flask(__name__)

def generate_data(num):
    numbers = int(num/8)
    data = []
    i=0
    for i in range(numbers):
        i=i+1
        data.append(i)
    return data

custom_list = []

@app.route('/')
def home():

    tracemalloc.start() #Start tracemalloc

    # ... Your code ...
    num = 20000 * 1024
    data = generate_data(num)
    custom_list.append(data)
    custom_list.append(custom_list)
    # ... Your code ...

    snapshot = tracemalloc.take_snapshot() # Taking snapshot
    top_stats = snapshot.statistics('lineno') # Getting statistics

    # ... Printing to console ...
    print("[ Top 10 ]") 
    for stat in top_stats[:10]:
        print(stat)
    # ... Printing to console ...

    return jsonify({"msg":"Data generated"})

if __name__ == "__main__":
    app.run()

