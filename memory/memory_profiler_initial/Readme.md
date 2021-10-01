# How to profile memory with memory_profiler

- Download this example using `git clone https://github.com/azureossd/python-performance-samples.git`
- Cd into **python-performance-samples/memory/memory_profiler_initial/**


---

## Create a virtual environment and install dependencies
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
            env\Scripts\activate
        ```
    - If you are using Linux
        ```shell
            source env/bin/activate
        ```
3. Once the virtual environment is activated, install **requirements.txt**.
    ```shell
        pip install -r requirements.txt
    ```

## Installing and configuring memory_profiler
1. Install memory_profiler with `pip install memory_profiler`
2. Then you will need to import the following module:
    ```python
        from memory_profiler import profile
    ```
3. In order to profile you can use two ways:

    a) Use profile and precision and execute python app as normal execution as followed:

    ```python
        from memory_profiler import profile

        @profile(precision=4)
        def create_data():
            ret = []
            for n in range(50):
                ret.append(np.random.randn(1, 70, 71, 72))
            return ret
            
        @profile(precision=4)
        def process_data(data):
            data = np.concatenate(data)
            detrended = scipy.signal.detrend(data, axis=0)
            return detrended
        
    ```
    
        And run the application with normal execution as followed:

    ```shell
        python app.py
    ```

    b) Or use profile without precision and pass the module as argument to python process as followed:

    ```python
        from memory_profiler import profile

        @profile()
        def create_data():
            ret = []
            for n in range(50):
                ret.append(np.random.randn(1, 70, 71, 72))
            return ret
            
        @profile()
        def process_data(data):
            data = np.concatenate(data)
            detrended = scipy.signal.detrend(data, axis=0)
            return detrended
    ```

    Run the application passing the module to python process:

    ```shell
        python -m memory_profiler app.py
    ```
