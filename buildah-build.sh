#!/usr/bin/bash
# Build container and push to public ecr registry.  This script is
# intended to be used by the k8s job defined in buildah-job.yaml

buildah build -t public.ecr.aws/v6u6a9m5/hello-http:latest-arm64v8 .

if [ $? -eq 0 ]; then
    (buildah login -u AWS --password $ECR_PASSWORD public.ecr.aws/v6u6a9m5 &&
     buildah push public.ecr.aws/v6u6a9m5/hello-http:latest-arm64v8)
fi
