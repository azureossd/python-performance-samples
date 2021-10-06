# Description
This app is taking a snapshot and saving it into a file `snap.out`.

# How to use this app

1. Create a virtual environment `python -m venv <name>`
2. Activate the virtual environment. Windows: `<name>\Scripts\activate`, Linux: `source <name>/bin/activate`
3. Install requirements.txt `pip install -r requirements.txt`
4. Run the application with `python app.py`
5. Request to `/` and then `/snapshot` to generate the file.
6. Run `python analyze.py` to analyze the data from snapshot.
