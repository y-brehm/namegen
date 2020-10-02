FROM tensorflow/tensorflow:1.14.0-gpu-py3

ENV LANG C.UTF-8
ENV APT_INSTALL="apt-get install -y --no-install-recommends"
ENV PIP_INSTALL="python -m pip --no-cache-dir install --upgrade --upgrade pip"

RUN rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/cuda.list /etc/apt/sources.list.d/nvidia-ml.list \
    && apt-get update

# Basic tools
RUN $APT_INSTALL \
    apt-utils \
    dialog \
    build-essential \
    ca-certificates \
    wget \
    libssl-dev \
    curl \
    unzip \
    unrar \
    vim

# Python
RUN $APT_INSTALL software-properties-common

# pip dependencies
RUN $PIP_INSTALL \
  setuptools \
  jupyter \
  wikipedia \
  duckduckpy

# Copy project files
RUN mkdir namegen
WORKDIR /namegen/

EXPOSE 6006
