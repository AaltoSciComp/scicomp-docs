cd $(dirname $0)
sh build.sh
docker push harbor.cs.aalto.fi/aaltorse/scicomp-docs-search:latest
kubectl apply -f k8s.yaml
kubectl -n rse rollout restart deployment/scicomp-docs-search
