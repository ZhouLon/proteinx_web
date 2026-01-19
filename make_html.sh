#!/bin/bash

#删除构建好的build
rm -rf build

cd ./develop/build/nginx-static/document/01_dl
make html