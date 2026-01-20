# 项目简介

本项目用于管理proteinx的官网以及文档，工具。

## 项目结构
```
├── build    #项目构建好的运行目录
├── develop  #项目构建开发目录
├── data     #项目数据
├── logs     #运行日志
├── make_html.sh   #构建运行目录
├── env.yaml       #依赖
├── gitusage.md    
├── README.md
└── usage.md
```

## 运行网址

* 培训文档:[`https://proteinx.com.cn/`](https://proteinx.com.cn/)
* 官网主页:[`http://proteinx.com.cn:5000/`](http://proteinx.com.cn:5000/)

# nginx

## 测试默认配置文件<br>
sudo nginx -t

## 查看状态<br>
sudo systemctl status nginx

## 启动<br>
sudo systemctl start nginx

## 重启<br>
sudo systemctl restart nginx

## 停止<br>
sudo systemctl stop nginx

# 符号操作

## 启用站点链接
sudo ln -s ./build/configs/nginx /etc/nginx/sites-enabled/

## 验证链接是否创建成功
ls -l /etc/nginx/sites-enabled/

## 取消符号链接 
sudo unlink /etc/nginx/sites-enabled/nginx