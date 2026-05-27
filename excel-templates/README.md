# Excel 数据模板使用说明

## 📋 模板文件

`csv/` 文件夹中包含以下 CSV 模板文件：

| 文件名 | 说明 | 数据量 |
|--------|------|--------|
| categories.csv | 分类数据 | 6 条 |
| brands.csv | 品牌数据 | 200 条 |
| sub-brands.csv | 子品牌数据 | 50 条 |
| vouchers.csv | 优惠券数据 | 8 条 |
| price-history.csv | 价格历史 | 10 条 |

## ✏️ 编辑步骤

### 方法 1：使用 Excel

1. **打开 Excel**
2. **导入 CSV**：
   - 文件 → 打开 → 选择对应的 CSV 文件
   - 或者：数据 → 从文本/CSV 导入
3. **编辑数据**
4. **保存**：
   - 文件 → 另存为 → 选择 CSV (UTF-8) 格式
   - 确保文件名不变，保存在原位置

### 方法 2：使用 Google Sheets

1. 访问 https://sheets.google.com
2. 新建表格
3. 复制 CSV 内容粘贴
4. 编辑完成后：文件 → 下载 → CSV 格式
5. 替换 `csv/` 中的对应文件

## 📊 字段说明

### Vouchers (优惠券) - 重点

| 字段 | 必填 | 说明 | 示例 |
|------|------|------|------|
| id | ✅ | 优惠券唯一 ID | 4001 |
| nameEn | ✅ | 英文名称 | Netflix 1 Month |
| nameAr | ✅ | 阿拉伯语名称 | نتفليكس شهر واحد |
| brandId | ✅ | 品牌 ID（参考 brands.csv） | 2001 |
| brandName | ✅ | 品牌名称 | Netflix |
| subBrandId | ✅ | 子品牌 ID（参考 sub-brands.csv） | 3001 |
| subBrandName | ✅ | 子品牌名称 | Netflix Premium |
| priceBefore | ✅ | 税前价格 | 50.00 |
| priceAfter | ✅ | 税后价格 | 57.50 |
| vat | ✅ | VAT 金额（自动计算：after - before） | 7.50 |
| priority | ✅ | 优先级（数字越小越靠前） | 1 |
| outOfStock | ✅ | 是否缺货：Yes/No | No |
| status | ✅ | 状态：Enable/Disable/Scheduled | Enable |
| startTime | ⚠️ | 开始时间（仅 Scheduled 状态需要） | 2026-04-10 00:00 |
| endTime | ⚠️ | 结束时间（仅 Scheduled 状态需要） | 2026-04-30 23:59 |

## 🔄 转换为 JSON

编辑完成后，运行转换脚本：

```bash
cd /home/admin/openclaw/workspace/marketplace-portal
python3 excel-to-json.py
```

脚本会：
1. 读取 `csv/` 中的所有 CSV 文件
2. 转换为 JSON 格式
3. 保存到 `data/` 目录

## 📤 推送到 GitHub

```bash
# 添加更改
git add data/*.json

# 提交
git commit -m "Update voucher data"

# 推送
git push origin main
```

GitHub Pages 会在 1-2 分钟内自动更新。

## ⚠️ 注意事项

1. **ID 唯一性**：确保每行的 ID 不重复
2. **编码格式**：保存为 UTF-8 编码，否则阿拉伯语会乱码
3. **数字格式**：价格字段不要带货币符号（如 $、﷼）
4. **状态字段**：必须是 Enable、Disable 或 Scheduled（区分大小写）
5. **缺货字段**：必须是 Yes 或 No（区分大小写）

## 💡 提示

- **批量编辑**：可以用 Excel 的填充功能快速填充重复数据
- **数据验证**：可以在 Excel 中设置下拉菜单限制状态字段
- **公式计算**：VAT 字段可以用公式 `=priceAfter - priceBefore` 自动计算
- **备份**：编辑前建议复制一份 CSV 文件作为备份

## 🆘 常见问题

**Q: 阿拉伯语显示乱码？**
A: 确保 CSV 文件保存为 UTF-8 编码。在 Excel 中：文件 → 另存为 → 工具 → Web 选项 → 编码 → Unicode (UTF-8)

**Q: 转换脚本报错？**
A: 检查 CSV 文件格式是否正确，字段名是否与模板一致

**Q: 网站没有更新？**
A: 检查是否推送了正确的 JSON 文件到 GitHub，并等待 1-2 分钟让 GitHub Pages 构建完成
