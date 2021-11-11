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
$ git clone https://github.com/SoftwareUnderstanding/SOMEF-Vider.git      
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
It follows roughly the same process as the development installation but, in this case, the client is compiled and
integrated into the flask service.

Go to the client folder and install the dependencies if they are not installed.
```
$ cd SOMEF-Vider/client/
$ npm install
```
Now instead of running the client, execute the following command to build it:
```
$ npm run build
```
This will generate a new folder in the current directory called "dist" with all the client files compiled.
To integrate this files in the service, just move the folder "dist" to the service folder and rename it to "static".
```
$ mv dist ../server/static
```
This last 2 mandates are (for now) the only difference between development and production. To run the tool
follow the steps listed above at the "Service" section.

## Authors
@Vitoriox
