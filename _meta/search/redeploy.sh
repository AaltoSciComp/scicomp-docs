#!/bin/bash

# This is our main script that does the entire redeployment.

set -e
cd $(dirname $0)
# Build the image using that build script
sh build.sh
# Push to harbor.cs.aalto.fi.  You need to have done a `docker login
# harbor.cs.aalto.fi` first.
docker push harbor.cs.aalto.fi/aaltorse/scicomp-docs-search:latest
# Apply the new YAML file.
kubectl apply -f k8s.yaml
# Rollout a new version.  if the YAML was changed, this might not be
# needed, but quite likely the YAML is the same and only the image is
# updated... so a rollout says to restart everything (and the yaml
# says "pull on every restart")
kubectl -n rse rollout restart deployment/scicomp-docs-search
