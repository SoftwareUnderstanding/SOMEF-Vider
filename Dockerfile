FROM node:16 AS build
COPY ./client src

WORKDIR src
RUN npm install && npm run build

FROM python:3.9
COPY ./server web
COPY --from=build /src/dist /web/static

WORKDIR web
# Due to conflicts with Click dependencie between flask and somef
# the instalation doesn't use the requirements.txt file
RUN pip install somef
RUN pip install flask
RUN pip install flask-cors
RUN somef configure -a

CMD python app.py

EXPOSE 5000

