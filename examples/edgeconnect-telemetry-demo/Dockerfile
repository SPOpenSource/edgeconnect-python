FROM ubuntu:20.04
RUN mkdir /app
COPY ./app/ec-telemetry /app/ec-telemetry
RUN chmod +x /app/ec-telemetry
RUN set -xe
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y iputils-ping && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq install dnsutils
RUN pip install --upgrade pip
RUN pip install -r /app/ec-telemetry/requirements.txt
