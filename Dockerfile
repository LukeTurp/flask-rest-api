FROM python:3.6-alpine

MAINTAINER Luke Turpin "takooon007@yahoo.com"

ENV HASH_API_LOG="/var/log/hash_api/hash_api.log"

# Copy shell script with env vars into Docker File System.
RUN mkdir -p /var/log/hash_api/ && \
  touch /var/log/hash_api/hash_api.log && \
  chmod 0775 /var/log/hash_api/hash_api.log

# Set hash_api's working directory to /hashapi in Docker.
WORKDIR /hashapi

# Copy everything from hash_api repo to Docker File System.
COPY . /hashapi

# Remove .git folder (unnecessary for Docker).
RUN rm -rf /hashapi/.git/

# Install Python dependencies based upon dependency list in requirements.txt.
RUN pip install -r /hashapi/requirements.txt

# Set our entrypoint - telling Python3 to run our application.
ENTRYPOINT ["python", "/hashapi/app.py"]
