# Tesla Wrap Studio

在浏览器中制作 Tesla 车机自定义涂装。支持 12 款车型模板、图片图层编辑、工程暂存、PNG 和 U 盘 ZIP 导出。

## 使用

直接打开 `index.html`，或在 macOS 执行 `./start_editor.sh`。在左侧上传图片，选择车型并编辑图层，最后从右上角导出。

## 开发

- `generate_editor_html.py`：编辑器源码。运行 `python3 generate_editor_html.py` 更新 `index.html`。
- `build_presets.py`：从 `custom-wraps/` 中的车型模板生成 `presets.js`，需要 Pillow：`python3 -m pip install Pillow`。
- `presets.js`：预生成的 12 款车型数据，打开页面无需安装依赖。

公开版本不包含尚未取得公开发布授权的角色图片预设；可以上传自己的图片使用全部编辑功能。车型模板来自 [Tesla custom-wraps](https://github.com/teslamotors/custom-wraps)。素材出处和使用范围见 `ASSET_PROVENANCE.md`。
