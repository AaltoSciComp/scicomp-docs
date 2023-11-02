set -e
cd $(dirname $0)
export DOCKER_BUILDKIT=1  # needed for --mount option
docker build ../../ -f Dockerfile -t harbor.cs.aalto.fi/aaltorse/scicomp-docs-search:latest
