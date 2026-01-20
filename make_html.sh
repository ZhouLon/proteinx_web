#!/bin/bash

#删除构建好的build
rm -rf build

# # # 构建文档
# cd ./develop/document/01_dl
# rm -rf build
# make html

# # 打补丁
# cd ../../..
# python ./develop/develop_tools/view_counts.py


# 复制生成的html文件到build目录下
mkdir -p build/nginx_static/document
cp -r ./develop/document/01_dl/build/html ./build/nginx_static/document/01_dl

# 复制主要页面
cp -r ./develop/main_pages ./build/main_pages

# 复制配置参数
cp -r ./develop/configs ./build/configs

# 创建nginx站点链接
sudo ln -s /mnt/e/repos/proteinx_web/build/configs/nginx /etc/nginx/sites-enabled/

