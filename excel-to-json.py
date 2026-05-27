#!/usr/bin/env python3
"""
Excel to JSON Converter for Marketplace Portal
将 Excel/CSV 文件转换为 JSON 格式

使用方法:
1. 编辑 excel-templates/ 中的 Excel 模板
2. 另存为 CSV 格式
3. 运行此脚本：python excel-to-json.py
"""

import json
import csv
import os
from pathlib import Path

# 配置
DATA_DIR = Path('data')
CSV_DIR = Path('excel-templates/csv')

# 字段映射
FIELD_MAPPINGS = {
    'categories': ['id', 'nameEn', 'nameAr', 'priority', 'iconLight', 'iconDark', 'status'],
    'brands': ['id', 'nameEn', 'nameAr', 'category', 'priority', 'logoLight', 'logoDark', 'status'],
    'sub-brands': ['id', 'nameEn', 'nameAr', 'brandId', 'brandName', 'store', 'priority', 'iconLight', 'iconDark', 'status'],
    'vouchers': ['id', 'nameEn', 'nameAr', 'brandId', 'brandName', 'subBrandId', 'subBrandName', 
                 'priceBefore', 'priceAfter', 'vat', 'priority', 'outOfStock', 'status', 'startTime', 'endTime'],
    'price-history': ['id', 'detectedAt', 'merchantId', 'merchantName', 'productId', 'productName', 
                      'vendorChannel', 'prevCost', 'currCost', 'prevRrp', 'currRrp', 
                      'prevMdr', 'currMdr', 'mdrChange', 'alertSent']
}

def convert_csv_to_json(csv_file, json_file, fields):
    """将 CSV 转换为 JSON"""
    data = []
    
    try:
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 过滤空行
                if not any(row.values()):
                    continue
                
                # 转换数据类型
                item = {}
                for field in fields:
                    value = row.get(field, '')
                    
                    # 数字类型转换
                    if field in ['priority']:
                        value = int(value) if value else 0
                    elif field in ['priceBefore', 'priceAfter', 'vat', 'prevCost', 'currCost', 
                                   'prevRrp', 'currRrp', 'prevMdr', 'currMdr', 'mdrChange']:
                        value = float(value) if value else 0.0
                    
                    item[field] = value
                
                data.append(item)
        
        # 写入 JSON
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f'✓ 转换成功：{csv_file} → {json_file} ({len(data)} 条记录)')
        return True
        
    except Exception as e:
        print(f'✗ 转换失败：{csv_file} - {e}')
        return False

def main():
    print('=== Excel to JSON Converter ===\n')
    
    # 创建目录
    CSV_DIR.mkdir(exist_ok=True)
    
    # 检查 CSV 文件
    csv_files = {
        'categories.csv': 'categories.json',
        'brands.csv': 'brands.json',
        'sub-brands.csv': 'sub-brands.json',
        'vouchers.csv': 'vouchers.json',
        'price-history.csv': 'price-history.json'
    }
    
    converted = 0
    for csv_name, json_name in csv_files.items():
        csv_path = CSV_DIR / csv_name
        json_path = DATA_DIR / json_name
        
        if csv_path.exists():
            fields = FIELD_MAPPINGS.get(csv_name.replace('.csv', ''), [])
            if convert_csv_to_json(csv_path, json_path, fields):
                converted += 1
        else:
            print(f'⊘ 跳过：{csv_name} (文件不存在)')
    
    print(f'\n✓ 完成：转换了 {converted} 个文件')
    print('\n提示：将生成的 JSON 文件推送到 GitHub 即可更新网站数据')

if __name__ == '__main__':
    main()
