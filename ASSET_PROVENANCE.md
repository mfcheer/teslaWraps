# 特斯拉车机涂装工程素材来源与许可规范记录 (Asset Provenance & Licensing)

## 一、 项目背景与定性说明
本项目为 Tesla 车机 Toybox 3D 个性化车漆涂装设计（Tesla Custom Wraps for Toybox Paint Shop）。
所有素材用于用户个人车机本地 3D 渲染显示（Private In-Car Local Visualization）。根据开源合规准则与团队复核意见，本文件记录各素材的具体出处、处理管线与授权状态。

> [!WARNING]
> **授权状态声明**：目前全套角色素材属于 Marvel/Disney 版权保护资产，仅适用于车主个人车机私域离线预览。因尚未获取公开发行授权或开源商业许可证（如 CC-BY），**明确标定为“未补齐可追溯授权”**，如需对外公开发布必须替换为全原创插画或合规开源素材。

---

## 二、 角色素材来源与处理记录表

| 角色 (Hero) | 所属位置 | 原始素材出处与可追溯性 | 原作者 / 版权归属 | 授权状态核定 | 工程精修与二创加工步骤 | 交付文件路径 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **奇异博士 (Doctor Strange)** | 副驾前门 (Passenger Front) | 上半身源自漫威官方推广表情包贴纸；下半身由算法工程合成重绘 | © Marvel Entertainment / The Walt Disney Company | **待补充可追溯授权（未补齐）**<br>仅限个人车机私有预览，无公开外发授权 | 1. 彻底切除头顶字幕 TEACH ME! 与版权杂字 © Marvel<br>2. 像素级透明底抠图（Alpha=0）<br>3. 由 `synthesize_chibi_doctor_strange_fullbody.py` 补充 2.5 头身下半身（深蓝法袍、金色饰带、藏青长裤与战术皮靴）<br>4. 双手实装金黄色能量秘法阵（Eldritch Tao Mandalas） | `assets_dynamic_heroes/drstrange_fullbody_chibi.png` |
| **蜘蛛侠 (Spider-Man)** | 主驾前门 (Driver Front) | 漫威经典动画动态全身体素材库 (`assets_lineup_clean/`) | © Marvel Entertainment / The Walt Disney Company | **仅限个人私域渲染（未补齐公开授权）** | 1. 赛璐璐（Cel-shaded）平涂重构，消除软渐变杂色<br>2. 完整保留经典红蓝战衣与腿部落地动态<br>3. 墨黑硬勾线与高反差动漫平涂对齐 | `assets_dynamic_heroes/spiderman.png` |
| **美国队长 (Captain America)** | 主驾后门 (Driver Rear) | 经典 Q 版平涂突进持盾造型 (`assets_anime/captain2.png`) | © Marvel Entertainment / The Walt Disney Company | **仅限个人私域渲染（未补齐公开授权）** | 1. 纯净 Alpha 透明通道切除<br>2. 振金盾牌与星条制服高对比平涂饱和度校色 | `assets_dynamic_heroes/cap.png` |
| **雷神托尔 (Thor)** | 副驾后门 (Passenger Rear) | 经典 Q 版挥锤引雷全身体造型 (`assets_anime/thor.png`) | © Marvel Entertainment / The Walt Disney Company | **仅限个人私域渲染（未补齐公开授权）** | 1. 纯净 Alpha 透明通道切除<br>2. 轮廓体量优化，锤子与飞扬披风无损缩放 | `assets_dynamic_heroes/thor.png` |
| **钢铁侠 (Iron Man)** | 前机盖核心 (Front Hood) | 翱翔动态二次元动漫造型 (`assets_anime/ironman.png`) | © Marvel Entertainment / The Walt Disney Company | **仅限个人私域渲染（未补齐公开授权）** | 1. 飞行仰角与掌心/胸口反应堆能量光晕增强<br>2. 机盖中心对齐 | `assets_dynamic_heroes/ironman.png` |
| **绿巨人浩克 (Hulk)** | 车尾画廊 (Rear Gallery) | 二次元 Q 版咆哮战斗造型 (`assets_lineup_clean/char_hulk.png`) | © Marvel Entertainment / The Walt Disney Company | **仅限个人私域渲染（未补齐公开授权）** | 1. 纯净 Alpha 透明通道提取<br>2. 统一横向 56px 等高画廊排布规范 | `assets_dynamic_heroes/hulk.png` |

---

## 三、 涂装底图与排查基准
1. **Model Y L 官方 UV 展开模板**：
   - 来源：`custom-wraps/modely-l/template.png`（Tesla Motors 官方开源仓库 `teslamotors/custom-wraps`）
   - 许可：请以 Tesla 官方仓库的实际授权条款为准；本仓库未独立核实授权
2. **纯色排查基准贴图**：
   - `ModelYL_Baseline_PureWhite.png`（纯白 Alpha 对齐官方基准底图）
