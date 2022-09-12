#!/usr/bin/bash -l
eval "$(micromamba shell hook --shell=bash)"
micromamba activate /opt/conda
exec "$@"
