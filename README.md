## Bottlelow

A wine-bottle wine-level quality checker

### Development
Build Docker image and launch the development container:
```
docker compose up
```

Connect to the container with:
```
docker exec -it bottlelow-app-1 sh
```

Install Python dependencies dependencies:
```
pip install src/requirements.txt
```

Run the program:
```
python src/main.py
```

#### Only for MacOS
In order to render the GUI, the followind steps are also necessary before running the program:

* Install XQuartz
* From preferences, enable `Allow connections from network clients` option
* Run command:
```
xhost + 127.0.0.1
```