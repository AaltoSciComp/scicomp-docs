FROM debian:latest

RUN apt-get update && apt-get install -y \
    python-sphinx \
    build-essential \
    python-sphinx-rtd-theme \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r /docbuild/requirements.txt

RUN mkdir -p /docbuild

CMD make -C /docbuild html
