#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from PIL import Image


def mkdir(path):
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    is_exists = os.path.exists(path)

    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' \t创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' \t目录已存在')
        return False


# 获取微软壁纸文件
def getImage(microsoft_path):
    files = os.listdir(microsoft_path)
    print("读取目录:%s 文件数:%s" % (microsoft_path, len(files)))
    return_files = {}
    for filename in files:

        # 组装准备读取的文件
        file_path = microsoft_path + '\\' + filename

        # 过滤不存在文件
        if os.path.isdir(file_path):
            continue

        # 打开文件
        fp = open(file_path, 'rb')
        try:
            img = Image.open(fp)
            # 筛选分辨率 > 500 * 500
            if img.size[0] * img.size[1] > 500 * 500:
                # 文件属性
                stat_info = os.stat(file_path)
                print("文件名:%s 分辨率:%s 文件大小:%s" % (filename, img.size, stat_info.st_size))
                # key=文件名 value=分辨率
                return_files[filename] = str(img.size[0]) + 'x' + str(img.size[1])

        except Exception as e:
            print(e)
        finally:
            fp.close()
    return return_files