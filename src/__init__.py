#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import shutil
import FileUtil


def getImage(microsoft_path):
    print('\n---------------------- start 获取微软壁纸图片 ----------------------')

    image_files = FileUtil.getImage(microsoft_path)
    print("微软壁纸图片 数量:%s 文件名:%s" % (len(image_files), image_files))
    print('---------------------- end 获取微软壁纸图片 ----------------------\n')
    return image_files


def copyImage(target_path, microsoft_path, image_files):
    print('\n---------------------- start 比较和copy ----------------------')
    if not os.path.isdir(target_path):
        print("%s文件夹未创建" % target_path)
        FileUtil.mkdir(target_path)

    # 比较(文件名是否在目标文件夹已存在) 分辨率文件夹
    # 微软壁纸文件
    num = 0
    for key, value in image_files.items():

        # 目标文件路径和+分辨率
        now_path = target_path + '\\' + value

        # 路径已存在-判断文件
        if not os.path.isdir(now_path):
            # 创建目标路径+分辨率
            FileUtil.mkdir(now_path)

        # 比较文件
        files = os.listdir(now_path)
        if key + '.png' in files:
            print(key, '文件已存在')
        else:
            num = num + 1
            print(str(num) + '. ' + key + '文件不存在-copy文件')
            shutil.copyfile(
                microsoft_path + '\\' + key,
                now_path + '\\' + key + '.png')

    print('---------------------- end 比较和copy ----------------------\n')


if __name__ == '__main__':

    # 微软壁纸所在的绝对路径
    microsoft_path = os.path.expanduser('~') \
                     + '\\AppData\\Local\\Packages' \
                     + '\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy' \
                     + '\\LocalState\\Assets'

    # 输出保存目标目录的绝对路径
    target_path = os.path.expanduser('~') + '\\OneDrive\\图片\\壁纸\\微软聚焦'

    # 获取微软聚焦文件夹的图片 分辨率 > 500 * 500
    image_files = getImage(microsoft_path)

    # copy到目标位置
    copyImage(target_path, microsoft_path, image_files)

