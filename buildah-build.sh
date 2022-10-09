#!/usr/bin/bash

buildah build -t public.ecr.aws/v6u6a9m5/hello-http:latest-arm64v8 .

if [ $? -eq 0 ]; then
    (buildah login -u AWS --password $ECR_PASSWORD public.ecr.aws/v6u6a9m5 &&
     buildah push public.ecr.aws/v6u6a9m5/hello-http:latest-arm64v8)
fi

