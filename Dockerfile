FROM debian:latest

RUN apt-get update && apt-get install -y \
    python-sphinx \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /docbuild

CMD make -C /docbuild
