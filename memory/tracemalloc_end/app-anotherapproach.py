from flask import Flask, jsonify
import os,json
import tracemalloc
import linecache

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
    
    tracemalloc.start()

    num = 20000 * 1024
    data = generate_data(num)
    custom_list.append(data)
    custom_list.append(custom_list)

    snapshot = tracemalloc.take_snapshot()
    display_top(snapshot)

    return jsonify({"msg":"Data generated"})

def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print("#%s: %s:%s: %.1f KiB"
              % (index, frame.filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


if __name__ == "__main__":
    app.run()

