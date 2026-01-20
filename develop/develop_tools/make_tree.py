"""改脚本用于生成项目目录结构树，方便查看项目文件组织情况。"""
import os

def tree(dir_path, level=-1, prefix=""):
    if level == 0:
        return
    
    entries = list(os.scandir(dir_path))
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        print(prefix + ("└── " if is_last else "├── ") + entry.name)
        if entry.is_dir():
            tree(entry.path, level - 1, prefix + ("    " if is_last else "│   "))

if __name__ == "__main__":
    tree(".", level=2)  # 显示2层结构