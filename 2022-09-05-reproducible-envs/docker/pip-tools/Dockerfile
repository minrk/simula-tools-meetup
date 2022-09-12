# syntax = docker/dockerfile:1.3
FROM python:3.10-slim-bullseye

ARG PIP_CACHE_DIR=/tmp/pip-cache

# install wheels built in the build-stage
COPY requirements.txt /tmp/requirements.txt
RUN --mount=type=cache,target=${PIP_CACHE_DIR} \
    pip install -r /tmp/requirements.txt
