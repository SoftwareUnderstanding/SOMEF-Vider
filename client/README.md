## Using the Dockerfile


The dockerfile will build the client bundle application without the need of installing npm.

To obtain and deploy the client bundle in the server, follow the instructions below:

0. If the image already exists, delete it: `docker rmi -f <image_id_>`. Alternatively, you can reuse your previous image, but remember to reclone the SOMEF-Vider repository to get the latest version.

1. Build the image: `docker build -t vider-client .` This creates an image with the bundle inside it

2. Copy the bundle in your target folder: 
```
docker run -it -v $PWD:/out vider-client /bin/bash
#: mv dist /out
```
This will copy the bundle to the client folder.

3. Move the client bundle to the server: `mv dist ../server/static`

4. Run the server: `python -m flask run`

