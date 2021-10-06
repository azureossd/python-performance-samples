# Description
This app is using logger to report the profiling data in one file, adapted to work on Flask, defining the functions in route endpoints.



# How to use this app

1. Create a virtual environment `python -m venv <name>`
2. Activate the virtual environment. Windows: `<name>\Scripts\activate`, Linux: `source <name>/bin/activate`
3. Install requirements.txt `pip install -r requirements.txt`
4. Run the application with `python app.py`
5. Request to `/` or `/memory` and this will create a log file `memory_profile.log` with the profiling data.