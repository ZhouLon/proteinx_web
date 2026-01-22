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

## 配置私钥和公钥
ssh-keygen -t ed25519 -C "xxxxxxxx@qq.com"

## 查看公钥
cat ~/.ssh/id_ed25519.pub

## 复制公钥
注意复制公钥到github

## 配置ssh本地设置
编辑 `~/.ssh/config`（Windows 在 `C:\Users\用户名\.ssh\config`）
```
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_laptop
```
## 配置名字
git config --global user.name "你的名字"

## 查看配置是否生效
git config --global --list | grep user


## 配置链接
git remote set-url origin git@github.com:your_username/your_repo.git

## 推送流程
1. 先fork别人的仓库到自己的仓库
2. 执行更改后推到自己的仓库
3. 拉取最新的更新
4. 在自己的fork仓库上向原仓库提出pull request