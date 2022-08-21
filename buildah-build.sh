#!/usr/bin/bash
ls -l /dev/fuse

buildah build --timestamp=$(date '+%s') \
    --logfile buildah-build.log -t public.ecr.aws/v6u6a9m5/hello-http:latest-arm64v8 .

if [ $? -eq 0 ]; then
    buildah login -u AWS --password-stdin < ecr-login-password public.ecr.aws/v6u6a9m5 &&
    buildah push public.ecr.aws/v6u6a9m5/hello-http:latest-arm64v8
fi
