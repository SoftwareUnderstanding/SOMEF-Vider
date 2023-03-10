FROM node:16 AS build
COPY ./client src

WORKDIR src
RUN npm install && npm run build

FROM python:3.9
COPY ./server web
COPY --from=build /src/dist /web/static

WORKDIR web

RUN python -m pip install -r requirements.txt --no-dependencies
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader omw-1.4
RUN python -m nltk.downloader stopwords
RUN somef configure -a

CMD python app.py

EXPOSE 5000

