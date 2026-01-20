from os import path
import os
from pathlib import Path
import sqlite3
from flask import Flask, render_template, redirect, url_for,request, jsonify



template_folder = path.abspath('build/main_pages/app/templates/')

app = Flask(__name__, template_folder=template_folder)




def init_db():
    os.makedirs('./data', exist_ok=True)
    conn = sqlite3.connect('./data/view_counts.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS view_counts (
            page TEXT PRIMARY KEY,
            count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()



@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/docs')
def docs():
    "点击培训文档"
    base_url = request.host_url.rstrip('/')
    server_address = base_url.replace(':5000', ':8080')
    print(f"Redirecting to: {server_address}")
    return redirect(server_address)



@app.route('/api/view_count', methods=['POST'])
def view_count():
    try:
        # 获取页面路径
        data = request.json
        page = data.get('page', '/')
        conn = sqlite3.connect('./data/view_counts.db')
        c = conn.cursor()
        
        c.execute('SELECT count FROM view_counts WHERE page = ?', (page,))
        result = c.fetchone()

        if result:
            # 更新现有记录
            new_count = result[0] + 1
            c.execute('UPDATE view_counts SET count = ? WHERE page = ?', 
                     (new_count, page))

        else:
            # 插入新记录
            new_count = 1
            c.execute('INSERT INTO view_counts (page, count) VALUES (?, ?)', 
                     (page, new_count))
        
        conn.commit()
        conn.close()

        # 返回当前浏览量
        return jsonify({
            'success': True,
            'count': new_count,
            'page': page
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/test')
def test():
    """渲染test.html页面"""
    return render_template('pages/test.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True,port=5000)
