import sqlite3

# 最简单的版本
conn = sqlite3.connect('./data/view_counts.db')
c = conn.cursor()

# 查看表内容
c.execute("SELECT * FROM view_counts")
rows = c.fetchall()

print("页面浏览统计：")
for page, count in rows:
    print(f"{page}: {count}次")

conn.close()