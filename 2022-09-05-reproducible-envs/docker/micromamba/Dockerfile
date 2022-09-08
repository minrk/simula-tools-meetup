# syntax: dockerfile-1.3
# date-tagged ubuntu:22.04 build
FROM ubuntu:jammy-20220815

# setup basic apt packages
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get -y update \
 && apt-get -y install --no-install-recommends bzip2 ca-certificates wget \
 && rm -rf /var/lib/apt/lists/*

# install micromamba to bootstrap environment
ENV MAMBA_ROOT_PREFIX=/tmp/conda
RUN wget -qO- https://micro.mamba.pm/api/micromamba/linux-64/0.25.0 | tar --directory /usr/local -xvj  bin/micromamba

# install locked env with micromamba
ENV CONDA_DIR=/opt/conda
ENV PATH=${CONDA_DIR}/bin:$PATH
COPY conda-linux-64.lock /tmp/conda.lock
RUN --mount=type=cache,target=${MAMBA_ROOT_PREFIX} \
    micromamba create -y -p "${CONDA_DIR}" -f /tmp/conda.lock

# register entrypoint so our env is activated no matter what command is launched in the container
COPY conda-entrypoint.sh /usr/local/bin/entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint"]
