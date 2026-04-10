# Marketplace Management Portal

一个基于纯静态文件的市场管理系统，可直接部署到 GitHub Pages。

## 📁 项目结构

```
marketplace-portal/
├── index.html              # 主页面
├── data/                   # 数据文件
│   ├── categories.json     # 分类数据
│   ├── brands.json         # 品牌数据
│   ├── sub-brands.json     # 子品牌数据
│   ├── vouchers.json       # 优惠券数据
│   └── price-history.json  # 价格历史数据
└── excel-templates/        # Excel 模板（用于编辑数据）
```

## 🚀 部署到 GitHub Pages

### 步骤 1：准备仓库

```bash
# 在 GitHub 创建新仓库，例如：marketplace-portal
git clone https://github.com/你的用户名/marketplace-portal.git
cd marketplace-portal

# 复制项目文件
cp /path/to/marketplace-portal/* .
```

### 步骤 2：推送代码

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 步骤 3：启用 GitHub Pages

1. 进入仓库 Settings → Pages
2. Source 选择 `main` 分支
3. 保存后，你的网站将在 `https://你的用户名.github.io/marketplace-portal/` 上线

## 📝 数据管理

### 方法 1：直接编辑 JSON 文件

每个 JSON 文件包含对应模块的数据，格式如下：

**categories.json**:
```json
[
  {
    "id": "1001",
    "nameEn": "Games",
    "nameAr": "ألعاب",
    "priority": 1,
    "iconLight": "🎮",
    "iconDark": "🎮",
    "status": "Enable"
  }
]
```

### 方法 2：使用 Excel 编辑（推荐）

1. 打开 `excel-templates/` 中的 Excel 模板
2. 编辑数据
3. 另存为 CSV 格式
4. 使用转换脚本转为 JSON：

```bash
python excel-to-json.py
```

### 方法 3：在线 JSON 编辑器

- 访问 https://jsoneditoronline.org/
- 编辑后保存为对应的 JSON 文件

## 📊 数据字段说明

### Categories (分类)
| 字段 | 说明 | 示例 |
|------|------|------|
| id | 分类 ID | 1001 |
| nameEn | 英文名称 | Games |
| nameAr | 阿拉伯语名称 | ألعاب |
| priority | 优先级（数字越小越靠前） | 1 |
| iconLight | 浅色模式图标 | 🎮 |
| iconDark | 深色模式图标 | 🎮 |
| status | 状态：Enable/Disable | Enable |

### Brands (品牌)
| 字段 | 说明 | 示例 |
|------|------|------|
| id | 品牌 ID | 2001 |
| nameEn | 英文名称 | Amazon Gift Cards |
| nameAr | 阿拉伯语名称 | أمازون بطاقات هدايا |
| category | 所属分类 | Shop |
| priority | 优先级 | 1 |
| logoLight | 浅色模式 Logo | 📦 |
| logoDark | 深色模式 Logo | 📦 |
| status | 状态 | Enable |

### Vouchers (优惠券)
| 字段 | 说明 | 示例 |
|------|------|------|
| id | 优惠券 ID | 4001 |
| nameEn | 英文名称 | Netflix 1 Month |
| nameAr | 阿拉伯语名称 | نتفليكس شهر واحد |
| brandId | 品牌 ID | 2001 |
| brandName | 品牌名称 | Netflix |
| subBrandId | 子品牌 ID | 3001 |
| subBrandName | 子品牌名称 | Netflix Premium |
| priceBefore | 税前价格 | 50.00 |
| priceAfter | 税后价格 | 57.50 |
| vat | VAT 金额 | 7.50 |
| priority | 优先级 | 1 |
| outOfStock | 是否缺货 | No |
| status | 状态：Enable/Disable/Scheduled | Enable |
| startTime | 开始时间（Scheduled 状态） | 2026-04-10 00:00 |
| endTime | 结束时间（Scheduled 状态） | 2026-04-30 23:59 |

## 🔄 更新数据流程

1. 在本地编辑 JSON 文件（或使用 Excel 转换）
2. 测试：在本地用浏览器打开 `index.html`
3. 提交更改：
   ```bash
   git add data/*.json
   git commit -m "Update voucher data"
   git push origin main
   ```
4. GitHub Pages 会自动更新（约 1-2 分钟）

## 🛠️ 本地开发

```bash
# 启动本地服务器
cd marketplace-portal
python3 -m http.server 8888

# 访问 http://localhost:8888
```

## ⚠️ 注意事项

1. **CORS 限制**：由于浏览器的安全策略，直接双击打开 `index.html` 可能无法加载 JSON 数据。请使用本地服务器或部署到 GitHub Pages。

2. **数据备份**：更新数据前请备份 JSON 文件。

3. **ID 唯一性**：确保每个数据项的 ID 是唯一的。

4. **特殊字符**：阿拉伯语名称请确保使用 UTF-8 编码保存。

## 📞 支持

如有问题，请创建 GitHub Issue。
