#!/bin/bash

# This script builds a new docker image.  It's a script
# because... that's how I first saw it and it saves needing to
# remember the commands.

set -e
cd $(dirname $0)
export DOCKER_BUILDKIT=1  # needed for --mount option
docker build ../../ -f Dockerfile -t harbor.cs.aalto.fi/aaltorse/scicomp-docs-search:latest
