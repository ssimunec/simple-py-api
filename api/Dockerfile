# set base image (host OS)
FROM python:3.8 AS base
EXPOSE 8004

# install dependencies
FROM base AS build
WORKDIR /app
COPY "api/requirements.txt" requirements.txt

RUN pip install -r requirements.txt;

FROM build AS final
# cache buster
ADD https://google.com cache_bust
# set the working directory in the container
# copy the content of the local src directory to the working directory
COPY "api/" .

# command to run on container start
CMD [ "python", "-u", "./server.py" ]