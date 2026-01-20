import os
import re

def creat_view_counts_file(file_path):
    """
    在HTML文件中插入浏览量显示代码和JavaScript代码
    
    参数:
    file_path (str): HTML文件路径
    """
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 定义要查找的模式 - 匹配版本信息
        # 两种模式：1. <strong>版本</strong>: 1.0<br/></p>
        #          2. <p><strong>版本</strong>: 1.0</p>
        pattern1 = r'(<strong>版本</strong>:\s*\d+\.\d+<br/>\s*</p>)'
        pattern2 = r'(<p>\s*<strong>版本</strong>:\s*\d+\.\d+\s*</p>)'
        
        # 浏览量显示的HTML代码片段
        view_count_html = '<p><strong>浏览量</strong>: <span id="viewCount" style="font-weight: 700; color: rgb(59, 130, 246); transition: 0.3s;"> </span></p>'
        
        # JavaScript代码片段
        js_code = '''<script>
  document.addEventListener('DOMContentLoaded', function() {
    // 获取当前页面的路径
    const pagePath = window.location.pathname;
    // 对于根页面，使用'/'或空字符串
    const pageInfo = pagePath.endsWith('/') ? pagePath.slice(0, -1) : pagePath;
    const currentPage = pageInfo || '/';
    
    console.log('正在统计页面浏览量:', currentPage);
    
    // 发送请求到后端API
    fetch('/api/view_count', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        page: currentPage,
        timestamp: new Date().toISOString()
      })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('网络响应不正常');
      }
      return response.json();
    })
    .then(data => {
      console.log('收到浏览量数据:', data);
      // 更新页面上的浏览量显示
      const viewCountElement = document.getElementById('viewCount');
      if (viewCountElement && data.count !== undefined) {
        // 格式化显示数字，添加千位分隔符
        const formattedCount = new Intl.NumberFormat('zh-CN').format(data.count);
        viewCountElement.textContent = formattedCount;
        
        // 为浏览量数字添加样式
        viewCountElement.style.fontWeight = '700';
        viewCountElement.style.color = '#10b981'; // 成功时改为绿色
        
        // 添加简单的动画效果
        viewCountElement.style.transition = 'all 0.3s ease';
        setTimeout(() => {
          viewCountElement.style.color = '#3b82f6'; // 0.3秒后变回蓝色
        }, 300);
      }
    })
    .catch(error => {
      console.error('获取浏览量时出错:', error);
      const viewCountElement = document.getElementById('viewCount');
      if (viewCountElement) {
        viewCountElement.textContent = '加载失败';
        viewCountElement.style.color = '#ef4444'; // 失败时改为红色
        viewCountElement.style.fontWeight = '600';
      }
    });
  });
</script>'''
        
        # 尝试匹配第一个模式
        modified = False
        
        if re.search(pattern1, content):
            # 在匹配到的版本信息后面插入浏览量显示
            new_content = re.sub(pattern1, r'\1\n' + view_count_html, content)
            modified = True
        elif re.search(pattern2, content):
            # 在匹配到的版本信息后面插入浏览量显示
            new_content = re.sub(pattern2, r'\1\n' + view_count_html, content)
            modified = True
        
        if not modified:
            print(f"警告: 在文件 {file_path} 中未找到版本信息")
            return
        
        # 在</body>标签前插入JavaScript代码
        if '</body>' in new_content:
            # 确保不会重复插入
            if 'fetch(\'/api/view_count\'' not in new_content:
                new_content = new_content.replace('</body>', js_code + '\n</body>')
                # 将修改后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
            else:
                print(f"信息: 文件 {file_path} 已包含浏览量代码，跳过处理")
        else:
            print(f"警告: 文件 {file_path} 中没有找到</body>标签")
            
    except Exception as e:
        print(f"错误: 处理文件 {file_path} 时出错: {str(e)}")

def creat_view_counts_dir(dir_path):
    """
    遍历目录下的所有HTML文件并调用creat_view_counts_file函数
    
    参数:
    dir_path (str): 目录路径
    """
    try:
        # 检查目录是否存在
        if not os.path.exists(dir_path):
            print(f"错误: 目录 {dir_path} 不存在")
            return
        
        # 统计处理的文件数量
        count = 0
        
        # 遍历目录下的所有文件
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                # 只处理HTML文件
                if file.lower().endswith('.html'):
                    file_path = os.path.join(root, file)
                    print(f"正在处理: {file_path}")
                    creat_view_counts_file(file_path)
                    count += 1
        
        print(f"完成: 总共处理了 {count} 个HTML文件")
        
    except Exception as e:
        print(f"错误: 处理目录 {dir_path} 时出错: {str(e)}")

if __name__ == "__main__":
    # 测试代码
    file_path = "./develop/document/01_dl/build/html/index.html"
    dir_path = "./develop/document/01_dl/build/html/01_Python介绍"
    
    # 如果文件存在，则处理单个文件
    if os.path.exists(file_path):
        creat_view_counts_file(file_path)
    else:
        print(f"测试文件不存在: {file_path}")
    
    # 如果目录存在，则处理目录
    if os.path.exists(dir_path):
        creat_view_counts_dir(dir_path)
    else:
        print(f"测试目录不存在: {dir_path}")