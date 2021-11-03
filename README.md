# SOMEF Vider
Web application for [SOMEF](https://github.com/KnowledgeCaptureAndDiscovery/somef)

## Description
SOMEF Vider is a web application based on Vue.js and Flask to visualize the metadata retrieved from the
SOMEF API.


## Development Installation
In the development installation client and service are independent. They are mounted and executed separately
from each other.

### Dependencies

* npm 6.14.8
* Python 3.9

### Installation

Clone this repository
```
$ git clone https://github.com/Vitoriox/SOMEF-Vider.git      
```

#### Client
Install dependencies for client
```
$ cd SOMEF-Vider/client/
```
```
$ npm install
```
Run client
```
$ npm run serve
```

#### Service
Install dependencies for server
```
$ cd SOMEF-Vider/server/
```
```
$ python3.9 -m venv virtualenv/
$ source virtualenv/bin/activate 
(virtualenv) $ python -m pip install -r requirements.txt
```
Run service
```
(virtualenv) $ python -m flask run
```



## Production installation
Production module is currently unavailable

## Authors
@Vitoriox
