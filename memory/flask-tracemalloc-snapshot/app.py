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

def add_to_list(num):
    data = generate_data(num)
    custom_list.append(data)
    custom_list.append(custom_list)

custom_list = []
@app.route('/')
def home():
    num = 20000 * 1024
    add_to_list(num)
    return jsonify({"msg":"Data generated"})

@app.route('/snapshot')
def snapshot():
    tracemalloc.start() #Start tracemalloc

    ## Your code
    num = 20000 * 1024
    add_to_list(num)

    ##Taking snapshot
    snapshot = tracemalloc.take_snapshot()
    snapshot.dump("snap.out")
    
    #tracemalloc.stop() 

    return jsonify({"msg":"Snapshot generated"})

if __name__ == "__main__":
    app.run()