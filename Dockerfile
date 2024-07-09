# SPDX-FileCopyrightText: 2024 Gabriele Pongelli
#
# SPDX-License-Identifier: MIT

# ref.  https://github.com/jmaupetit/md2pdf

# -- Base image --
FROM python:3.12-slim as base

ARG PKG_VERSION

# https://snyk.io/blog/how-and-when-to-use-docker-labels-oci-container-annotations/
# https://github.com/opencontainers/image-spec/blob/main/annotations.md#pre-defined-annotation-keys
LABEL org.opencontainers.image.created=2024-07-09T23:20:50.52Z
LABEL org.opencontainers.image.authors="Gabriele Pongelli <gabriele.pongelli@gmail.com>"
LABEL org.opencontainers.image.version="${PKG_VERSION}"
LABEL org.opencontainers.image.licenses=MIT
LABEL org.opencontainers.image.documentation="https://gpongelli.github.io/python-active-versions/"
LABEL org.opencontainers.image.source="https://github.com/gpongelli/python-active-versions"
LABEL org.opencontainers.image.url="https://hub.docker.com/r/gpongelli/python-active-versions"
LABEL org.opencontainers.image.revision=738e35c1b087704f043b424a3e3831997895cc3b
LABEL org.opencontainers.image.description="Gather active python versions."

# Upgrade pip to its latest release to speed up dependencies installation
RUN pip install --no-cache-dir --upgrade pip==24.0

# Upgrade system packages to install security updates
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y --no-install-recommends install g++ gcc && \
    rm -rf /var/lib/apt/lists/*
    # g++ and gcc needed by pytomlpp

# -- Builder --
FROM base as builder

WORKDIR /build

COPY . /build/

ENV PATH  $PATH:/root/.local/bin

# Install poetry
RUN pip install --no-cache-dir pipx && \
    pipx install poetry

ARG PKG_VERSION

# Build and install package
RUN poetry build && \
    pip install --no-cache-dir dist/*-$PKG_VERSION-*.whl

# -- Core --
FROM base as core

COPY --from=builder /usr/local /usr/local

# -- App --
FROM core as production

VOLUME ["/app"]

WORKDIR /app

USER "1000:1000"

ENTRYPOINT ["python-active-versions"]
