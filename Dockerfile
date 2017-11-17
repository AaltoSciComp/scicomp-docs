FROM debian:latest

RUN apt-get update && apt-get install -y \
    python-sphinx \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/docbuilder
RUN chown 1001:1001 /home/docbuilder

RUN adduser --home /home/docbuilder --uid 1001 --shell /bin/bash --disabled-password --gecos '' docbuilder

USER docbuilder
WORKDIR /home/docbuilder
