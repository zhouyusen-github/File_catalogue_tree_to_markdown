import os

def level_to_string(level):
    """
    将层级转换为对应的Markdown标题格式
    """
    if level <= 6:
        return "#" * level + " "
    else:
        return ("    " * (level - 7)) + "- "

def analyze_directory(path, level, level_limit, mind_map_markdown):
    """
    分析目录结构并生成Markdown格式的思维导图
    """
    dirs = os.listdir(path)
    dirs.sort()
    for file in dirs:
        level_string = level_to_string(level)
        sub_path = os.path.join(path, file)
        mind_map_markdown.write(level_string + file + "\n")
        if os.path.isdir(sub_path) and level <= level_limit:
            sub_level = level + 1
            analyze_directory(sub_path, sub_level, level_limit, mind_map_markdown)

# 获取用户输入的文件夹路径和层级深度
path = input("输入文件夹路径：")  # 例如: 'D:\\01爬虫工作指南'
level_limit = int(input("探索层级深度：") or 20)

# 设置初始层级和输出文件名
level = 1
file_name = os.path.split(path)[-1] + '.md'

# 打开Markdown文件并开始分析目录结构
with open(file_name, 'w', encoding='utf-8') as mind_map_markdown:
    analyze_directory(path, level, level_limit, mind_map_markdown)

print(f"Markdown文件 {file_name} 已生成。")
