## Using the Dockerfile


The dockerfile will build the client bundle application without the need of installing npm.

To obtain and deploy the client bundle in the server, follow the instructions below:

1- Build the image: `docker build -t vider-client .` This creates an image with the bundle inside it

2- Copy the bundle outside: 
```
docker run -it -v $PWD:/out vider-client /bin/bash
#: mv dist /out
```
This will copy the bundle to the client folder.

3- Move the client bundle to the server: `mv dist ../server/static`

4- Run the server: `python -m flask run`

