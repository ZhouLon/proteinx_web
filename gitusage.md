# 初始化并拉取项目

## 初始化本地Git仓库
git init

## 关联远程GitHub仓库
git remote add origin <你的仓库URL>

## 拉取代码并整合
git pull origin main --allow-unrelated-histories

# 推送项目

## 暂存更改的文件
git add .

## 提交更改到本地仓库
git commit -m "描述本次修改的说明信息"

## 推送到远程仓库
git push origin main

## 拉取远程更新并自动合并
git pull origin main

## 查看本地和远程的差异
git log --oneline --graph --all


# 配置个人信息
## 配置邮箱
git config --global user.email "你的邮箱"

## 配置公钥
ssh-keygen -t ed25519 -C "1922450589@qq.com"

## 配置名字
git config --global user.name "你的名字"

## 查看配置是否生效
git config --global --list | grep user

## 查看公钥
cat ~/.ssh/id_ed25519.pub

## 配置链接
git remote set-url origin git@github.com:

