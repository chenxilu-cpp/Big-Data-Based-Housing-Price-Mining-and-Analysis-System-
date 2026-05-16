# Big-Data-Based-Housing-Price-Mining-and-Analysis-System-

## 项目简介

本项目实现了一套针对链家二手房数据的爬取与分析系统。主要功能包括：
- 自动抓取链家二手房页面中的房源数据
- 提取房源标题、小区、区域、售价、单价、户型、面积、朝向、装修、楼层、年份、建筑类型、详情页链接等字段
- 将抓取结果保存为 `data.csv` 供后续分析使用
- 提供基于采集数据的分析与可视化示例（Jupyter Notebook）

## 技术栈

- Python 3
- `requests`：发送 HTTP 请求，获取网页内容
- `parsel`：解析页面 HTML、抽取数据
- `csv`：CSV 文件读写
- Jupyter Notebook：数据分析与可视化

## 项目结构

- `项目源码/链家.py`：链家二手房爬虫脚本
- `项目源码/data.csv`：示例数据文件（可由爬虫生成）
- `项目源码/data_analysis.ipynb`：数据分析笔记本
- `项目源码/链家二手房可视化 (1).ipynb`：可视化分析笔记本
- `项目源码/render.html`：可视化结果或报告展示文件

## 安装环境

建议使用 Python 3.8 及以上版本。

1. 安装 Python
2. 创建虚拟环境（可选）：
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. 安装依赖库：
   ```bash
   pip install requests parsel
   ```

> 如果需要执行 Jupyter Notebook，请额外安装：
> ```bash
> pip install notebook pandas matplotlib seaborn
> ```

## 使用方法

1. 进入项目源码目录：
   ```bash
   cd 项目源码
   ```
2. 运行爬虫脚本：
   ```bash
   python3 链家.py
   ```
3. 脚本执行后，会在当前目录生成 `data.csv` 文件，包含采集到的二手房信息。
4. 使用 Jupyter Notebook 打开分析文件：
   ```bash
   jupyter notebook data_analysis.ipynb
   ```

## 注意事项

- 本项目仅用于学习与研究。爬取网站数据请遵守目标站点的服务条款和法律法规。
- 如果网站结构调整，爬虫解析规则可能需要更新。
- 运行爬虫时请控制请求频率，避免给目标网站带来过大压力。

## 结果说明

爬取结果保存为 `data.csv`，主要字段包括：
- 标题
- 小区
- 区域
- 售价
- 单价
- 户型
- 面积
- 朝向
- 装修
- 楼层
- 年份
- 建筑类型
- 详情页

## 推荐流程

1. 先运行 `链家.py` 收集数据
2. 然后打开 `data_analysis.ipynb` 查看分析结果
3. 如果需要可视化，可打开 `链家二手房可视化 (1).ipynb` 或 `render.html`
