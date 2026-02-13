import os
import re

def add_icp_to_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if '粤ICP备2025431884号-1' in content:
            return
        pattern = r'(<p\s+class="text-sm[^"]*".*?>.*?Built with.*?</a>)(\s*</p>)'
        new_content, n = re.subn(
            pattern,
            r'\1 <a href="https://beian.miit.gov.cn/" target="_blank">粤ICP备2025431884号-1</a>\2',
            content,
            flags=re.S
        )
        if n == 0:
            footer_pattern = r'(</footer>)'
            new_content, n2 = re.subn(
                footer_pattern,
                r'<div class="container"><p class="text-sm leading-loose text-center text-muted-foreground md:text-left"><a href="https://beian.miit.gov.cn/" target="_blank">粤ICP备2025431884号-1</a></p></div>\1',
                content,
                count=1,
                flags=re.S
            )
            if n2 == 0:
                return
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    except Exception:
        pass

if __name__ == '__main__':
    src_index = os.path.join('.', 'develop', 'document', '01_dl', 'build', 'html', 'index.html')
    if os.path.exists(src_index):
        add_icp_to_file(src_index)