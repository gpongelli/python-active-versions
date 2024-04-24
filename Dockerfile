# SPDX-FileCopyrightText: 2024 Gabriele Pongelli
#
# SPDX-License-Identifier: MIT


# ref.  https://github.com/jmaupetit/md2pdf

# -- Base image --
FROM python:3.12-slim as base

MAINTAINER Gabriele Pongelli <gabriele.pongelli@gmail.com>

# Upgrade pip to its latest release to speed up dependencies installation
RUN pip install --upgrade pip

# Upgrade system packages to install security updates
RUN apt update && \
    apt -y upgrade

# -- Builder --
FROM base as builder

WORKDIR /build

COPY . /build/

ENV PATH  $PATH:/root/.local/bin

# Install poetry
RUN pip install pipx && \
    pipx install poetry
# Build and install package
RUN poetry build && \
    pip install dist/*.whl

# -- Core --
FROM base as core

COPY --from=builder /usr/local /usr/local

# -- App --
FROM core as production

VOLUME ["/app"]

WORKDIR /app

USER "1000:1000"

ENTRYPOINT ["python-active-versions"]