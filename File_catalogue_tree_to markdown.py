import os


def level_to_string(level):  # 对应层级，xmind导入markdown需要的格式
    if level <= 6:
        return "#" * level + " "
    else:
        return "* "


def analysis(path, level, level_limit, MindMap_markdown):
    dirs = os.listdir(path)
    dirs.sort()
    for file in dirs:
        level_string = level_to_string(level)
        sub_path = path + '/' + file
        MindMap_markdown.write(level_string + file + "\n")
        if os.path.isdir(sub_path) and level < level_limit:
            sub_level = level + 1
            analysis(sub_path, sub_level, level_limit, MindMap_markdown)


# 打开文件
path = input("文件夹地址：")  # 'D:\01爬虫工作指南'
level_limit = int(input('文件夹显示深度（默认2,至多7）：') or 2)
level = 1
file = path.split('\\')[-1] + '.md'
MindMap_markdown = open(file, 'w', encoding='utf-8')
analysis(path, level, level_limit, MindMap_markdown)
MindMap_markdown.close()
