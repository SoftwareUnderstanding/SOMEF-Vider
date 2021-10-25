# Metavider
Web application for [SOMEF](https://github.com/KnowledgeCaptureAndDiscovery/somef)

## Description
Metavider is a web application based on Vue.js and Flask to visualize the metadata retrieved from the
SOMEF API.


## Development Installation
In the development installation client and service are independent. They are mounted and executed separately
from each other.

### Dependencies

* npm 6.14.8
* Python 3.7.3

### Installation

Clone this repository
```
$ git clone https://github.com/Vitoriox/SOMEF-WebApp.git      
```

#### Client
Install dependencies for client
```
$ cd SOMEF-WebApp/client/
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
$ cd SOMEF-WebApp/server/
```
```
$ python3 -m venv virtualenv/
$ source virtualenv/bin/activate 
(virtualenv) $ python3 -m pip install -r requirements.txt
```
Run service
```
(virtualenv) $ python3 app.py
```



## Production installation
Production module is currently unavailable

## Authors
@Vitoriox
