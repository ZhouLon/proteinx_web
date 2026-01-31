@echo off

:: 删除旧的构建目录
if exist build rmdir /s /q build

:: 创建必要的目录结构
mkdir build\nginx-static\document >nul 2>&1

:: 复制文档
xcopy "develop\document\01_dl\build\html\*" "build\nginx-static\document\01_dl\" /E /I /Y

:: 复制主要页面
xcopy "develop\main_pages\*" "build\main_pages\" /E /I /Y

:: 复制配置
xcopy "develop\configs\*" "build\configs\" /E /I /Y
