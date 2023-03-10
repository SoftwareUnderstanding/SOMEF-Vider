# SOMEF Vider
Web application for [SOMEF](https://github.com/KnowledgeCaptureAndDiscovery/somef)

## Description
SOMEF Vider is a web application based on Vue.js and Flask to visualize the metadata retrieved from the
SOMEF API.

## Demo
We have a running demo in [https://somef.linkeddata.es](https://somef.linkeddata.es). If the demo is down, please let us know by opening an issue.

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

Before installation, configure the target server in `client/src/service/axiosService` by changing the variable `LOCAL_URL`. For local tests, use `127.0.0.1:5000` (assuming the application is deployed in that port).

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
cd SOMEF-Vider/server/
```
```
python3.9 -m venv virtualenv/
```
```
source virtualenv/bin/activate 
```
```
python -m pip install -r requirements.txt --no-dependencies
```
```
python -m nltk.downloader all
```
Run service. Ports can be configures in `app.py`
``` 
python app.py
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

To generate the bundle with Docker, see the [client deployment instructions](https://github.com/SoftwareUnderstanding/SOMEF-Vider/blob/master/client/README.md).

## Docker bundle
If you want an image of the whole application, you can generate a Docker image as follows:

First configure the GitHub token in the `/server/installer.sh` setting the property `token`
to the desired GitHub token. (ensure that this file is marked as executable)

Then run the Docker command in the root directory
```
docker build -t somef-vider .
```
And run the container
```
docker run -p 5000:5000 somef-vider
```

Now you will have the complete application running on the port 5000

## Authors
- @Vitoriox: design and implementation
- @dgarijo: supervision, testing and deployment

## Contributing

If you find problems or if you wish to add new features, please let us know by opening an [issue](https://github.com/SoftwareUnderstanding/SOMEF-Vider/issues) or submitting a pull request.
