# How to run this sample code

## Flask App
1. Create a virtual environment with any python version >=3.
    - If you are using Windows:
        ```shell
            python -m venv env
        ```
    - If you are using Linux:
        ```shell
            python3 -m venv env
       ```
2. Activate the virtual environment.
    - If you are using Windows in cmd:
        ```shell
            env\Scripts\activate.bat
        ```
    - If you are using Linux
        ```shell
            source env/bin/activate
        ```
3. Once the virtual environment is activated, install **requirements.txt**.
    ```shell
        pip install -r requirements.txt
    ```
4. Run the application.
    - If you are using Windows:
        ```shell
            python app.py
        ```
    - If you are using Linux:
        ```shell
            python3 app.py
        ```
    > The application will be listening by default on **http://127.0.0.1:5000/**
5. Configure output.
    If you want to print the results in console use the following lines of code:
        ```python
            ps.print_stats()
            print(s.getvalue())
        ```

    If you want to redirect stdout to a file, use the following code:
        ```python
            ps.dump_stats('output.txt')
        ```
     > You will need another step to review this output.

6. You can also use the following ways to run cProfile to specific function: 
`cProfile.run('firstMethod()')`  Or  `cProfile.runctx('firstMethod()', globals(), locals())`

## Python script
> For this sample you don't need any virtual environment since there are not extra libraries to be installed.
1. Run the application.
    - If you are using Windows:
        ```shell
            python script.py
        ```
    - If you are using Linux:
        ```shell
            python3 script.py
        ```
2. To run cprofile you can use the following command in this script:
```shell
    python -m cProfile -s cumtime script.py
```
3. You can also use the following ways to run cProfile to specific function: 
`cProfile.run('firstMethod()')`  Or  `cProfile.runctx('firstMethod()', globals(), locals())`