
# A Simple Blockchain Program Using Python 


## Setup:

1. To Create a Virtual Environment
```
python3 -m venv blockc-venv
```

2. Activating virtual environment
```
# For Windows
.\blockc-venv\Scripts\activate

# For Linux
source ./blockc-venv/bin/activate
```
3. install package
```
pip install -r requirements.txt
```

4. Run The Server
```
python server.py 
python server.py -p 5001
python server.py --port 5002
```

## Docker

Another option for running this blockchain program is to use Docker:

1. Clone this repository
2. Build the docker container
```
$ docker build -t blockchain .
```

3. Run the container
```
$ docker run --rm -p 5000:5000 blockchain
```

4. To add more instances, vary the public port number before the colon:
```
$ docker run --rm -p 5000:5000 blockchain
$ docker run --rm -p 5001:5000 blockchain
$ docker run --rm -p 5002:5000 blockchain
```


## Resources:
[Guide](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)
| 
[Repo](https://github.com/dvf/blockchain/tree/master)
