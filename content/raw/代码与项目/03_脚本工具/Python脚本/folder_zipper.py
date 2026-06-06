#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
通用文件夹打包工具 (Universal Folder Zipper)

功能：
1. 接收任意文件夹路径作为输入
2. 遍历并单独打包所有子文件夹
3. 生成同名.zip文件
4. 包含进度显示和错误处理
5. 跨平台兼容 (Windows/Linux/macOS)

用法：
    python folder_zipper.py [文件夹路径]
    python folder_zipper.py --help
"""

import os
import shutil
import sys
import argparse
from datetime import datetime

def setup_arg_parser():
    """设置命令行参数解析器"""
    parser = argparse.ArgumentParser(
        description='通用文件夹打包工具 - 将指定目录下的每个子文件夹单独打包为ZIP文件',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog='示例:\n  python folder_zipper.py "C:\\Users\\Data"\n  python folder_zipper.py /home/user/projects'
    )
    parser.add_argument('path', nargs='?', help='包含待打包子文件夹的目标目录路径')
    return parser

def zip_subfolders(target_dir):
    """
    遍历并压缩指定目录下的所有子文件夹
    """
    # 1. 验证路径有效性
    if not os.path.exists(target_dir):
        print(f"❌ 错误: 路径不存在 - {target_dir}")
        return
    if not os.path.isdir(target_dir):
        print(f"❌ 错误: 路径不是一个目录 - {target_dir}")
        return

    target_dir = os.path.abspath(target_dir)
    print(f"📂 正在扫描目录: {target_dir}\n")

    # 2. 获取所有子目录
    try:
        items = os.listdir(target_dir)
    except PermissionError:
        print(f"❌ 权限拒绝: 无法访问目录 {target_dir}")
        return
    except Exception as e:
        print(f"❌ 扫描目录出错: {e}")
        return

    subdirs = [d for d in items if os.path.isdir(os.path.join(target_dir, d))]
    total = len(subdirs)
    
    if total == 0:
        print("⚠️  未发现子文件夹，无需操作。")
        return

    print(f"发现 {total} 个子文件夹，准备开始打包...\n")

    success_count = 0
    fail_count = 0
    skip_count = 0

    # 3. 遍历处理
    for index, subdir in enumerate(subdirs, 1):
        subdir_path = os.path.join(target_dir, subdir)
        zip_filename = f"{subdir}.zip"
        zip_file_path = os.path.join(target_dir, zip_filename)

        # 进度显示
        print(f"[{index}/{total}] 处理: {subdir} ...", end='', flush=True)

        # 检查压缩包是否已存在 (可选：如果需要覆盖，可以去掉此检查或添加参数控制)
        if os.path.exists(zip_file_path):
            print(f"\r[{index}/{total}] ⏭️  跳过: {subdir} (压缩包已存在)")
            skip_count += 1
            continue

        try:
            # 4. 创建压缩包 (shutil.make_archive 自动处理 .zip 后缀)
            # base_name 是不带后缀的文件名路径
            base_name = os.path.join(target_dir, subdir)
            
            # root_dir 是要压缩的根目录
            shutil.make_archive(base_name, 'zip', subdir_path)
            
            print(f"\r[{index}/{total}] ✅ 完成: {subdir}")
            success_count += 1
            
        except PermissionError:
            print(f"\r[{index}/{total}] ❌ 失败: {subdir} (权限不足)")
            fail_count += 1
        except Exception as e:
            print(f"\r[{index}/{total}] ❌ 失败: {subdir} (错误: {str(e)})")
            fail_count += 1

    # 5. 总结输出
    print("\n" + "="*30)
    print(f"任务完成!")
    print(f"✅ 成功: {success_count}")
    print(f"⏭️  跳过: {skip_count}")
    print(f"❌ 失败: {fail_count}")
    print("="*30)

def main():
    parser = setup_arg_parser()
    
    # 检查是否提供了参数，如果没有，尝试提示用户输入
    if len(sys.argv) == 1:
        parser.print_help()
        print("\n请输入要处理的文件夹路径:")
        try:
            user_input = input("路径 > ").strip()
            # 处理可能的引号（Windows复制路径时常带有引号）
            if (user_input.startswith('"') and user_input.endswith('"')) or \
               (user_input.startswith("'") and user_input.endswith("'")):
                user_input = user_input[1:-1]
            
            if user_input:
                zip_subfolders(user_input)
            else:
                print("未输入路径，程序退出。")
        except KeyboardInterrupt:
            print("\n用户取消。")
    else:
        args = parser.parse_args()
        zip_subfolders(args.path)

if __name__ == "__main__":
    main()
