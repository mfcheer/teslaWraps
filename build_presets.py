# -*- coding: utf-8 -*-
import os
import json
import base64
import io
from PIL import Image

wraps_dir = 'custom-wraps'

models_meta = [
    {
        "id": "modely-l",
        "name": "Model Y L",
        "subtitle": "Model Y L 专用",
        "series": "Model Y",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "ModelY_L_Wrap.png",
        "hoodCenter": [512, 222],
        "placements": {
            "hood": {"x": 512, "y": 250, "scale": 0.32},
            "front_left_door": {"x": 120, "y": 380, "scale": 0.28},
            "rear_left_door": {"x": 125, "y": 645, "scale": 0.28},
            "front_right_door": {"x": 900, "y": 380, "scale": 0.28},
            "rear_right_door": {"x": 896, "y": 647, "scale": 0.28}
        }
    },
    {
        "id": "modely",
        "name": "Model Y (经典版)",
        "subtitle": "Model Y 2020-2024",
        "series": "Model Y",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "ModelY_Wrap.png",
        "hoodCenter": [512, 219],
        "placements": {
            "hood": {"x": 512, "y": 250, "scale": 0.32},
            "front_left_door": {"x": 120, "y": 380, "scale": 0.28},
            "rear_left_door": {"x": 125, "y": 645, "scale": 0.28},
            "front_right_door": {"x": 900, "y": 380, "scale": 0.28},
            "rear_right_door": {"x": 896, "y": 647, "scale": 0.28}
        }
    },
    {
        "id": "modely-2025-base",
        "name": "Model Y 焕新版 (标准版)",
        "subtitle": "Juniper Standard 2025+",
        "series": "Model Y",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "ModelY_2025_Base_Wrap.png",
        "hoodCenter": [512, 177],
        "placements": {
            "hood": {"x": 512, "y": 210, "scale": 0.30},
            "front_left_door": {"x": 200, "y": 380, "scale": 0.26},
            "rear_left_door": {"x": 200, "y": 640, "scale": 0.26},
            "front_right_door": {"x": 820, "y": 380, "scale": 0.26},
            "rear_right_door": {"x": 820, "y": 640, "scale": 0.26}
        }
    },
    {
        "id": "modely-2025-premium",
        "name": "Model Y 焕新版 (长续航版)",
        "subtitle": "Juniper Premium 2025+",
        "series": "Model Y",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "ModelY_2025_Premium_Wrap.png",
        "hoodCenter": [512, 188],
        "placements": {
            "hood": {"x": 512, "y": 220, "scale": 0.30},
            "front_left_door": {"x": 140, "y": 380, "scale": 0.27},
            "rear_left_door": {"x": 140, "y": 640, "scale": 0.27},
            "front_right_door": {"x": 880, "y": 380, "scale": 0.27},
            "rear_right_door": {"x": 880, "y": 640, "scale": 0.27}
        }
    },
    {
        "id": "modely-2025-performance",
        "name": "Model Y 焕新版 (高性能版)",
        "subtitle": "Juniper Performance 2025+",
        "series": "Model Y",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "ModelY_2025_Perf_Wrap.png",
        "hoodCenter": [512, 182],
        "placements": {
            "hood": {"x": 512, "y": 220, "scale": 0.30},
            "front_left_door": {"x": 120, "y": 380, "scale": 0.28},
            "rear_left_door": {"x": 125, "y": 645, "scale": 0.28},
            "front_right_door": {"x": 900, "y": 380, "scale": 0.28},
            "rear_right_door": {"x": 896, "y": 647, "scale": 0.28}
        }
    },
    {
        "id": "model3",
        "name": "Model 3 (经典版)",
        "subtitle": "Model 3 2017-2023",
        "series": "Model 3",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "Model3_Wrap.png",
        "hoodCenter": [512, 212],
        "placements": {
            "hood": {"x": 512, "y": 240, "scale": 0.30},
            "front_left_door": {"x": 115, "y": 380, "scale": 0.27},
            "rear_left_door": {"x": 120, "y": 645, "scale": 0.27},
            "front_right_door": {"x": 905, "y": 380, "scale": 0.27},
            "rear_right_door": {"x": 900, "y": 647, "scale": 0.27}
        }
    },
    {
        "id": "model3-2024-base",
        "name": "Model 3 焕新版 (标准/长续航)",
        "subtitle": "Highland Standard & Premium 2024+",
        "series": "Model 3",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "Model3_2024_Base_Wrap.png",
        "hoodCenter": [512, 223],
        "placements": {
            "hood": {"x": 512, "y": 240, "scale": 0.30},
            "front_left_door": {"x": 115, "y": 380, "scale": 0.27},
            "rear_left_door": {"x": 120, "y": 645, "scale": 0.27},
            "front_right_door": {"x": 905, "y": 380, "scale": 0.27},
            "rear_right_door": {"x": 900, "y": 647, "scale": 0.27}
        }
    },
    {
        "id": "model3-2024-performance",
        "name": "Model 3 焕新版 (高性能版)",
        "subtitle": "Highland Performance 2024+",
        "series": "Model 3",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "Model3_2024_Perf_Wrap.png",
        "hoodCenter": [512, 234],
        "placements": {
            "hood": {"x": 512, "y": 240, "scale": 0.30},
            "front_left_door": {"x": 115, "y": 380, "scale": 0.27},
            "rear_left_door": {"x": 120, "y": 645, "scale": 0.27},
            "front_right_door": {"x": 905, "y": 380, "scale": 0.27},
            "rear_right_door": {"x": 900, "y": 647, "scale": 0.27}
        }
    },
    {
        "id": "cybertruck",
        "name": "Cybertruck (赛博皮卡)",
        "subtitle": "Cybertruck 2023+ (1024×768)",
        "series": "Cybertruck",
        "width": 1024,
        "height": 768,
        "defaultFileName": "Cybertruck_Wrap.png",
        "hoodCenter": [512, 116],
        "placements": {
            "hood": {"x": 512, "y": 120, "scale": 0.28},
            "front_left_door": {"x": 220, "y": 260, "scale": 0.28},
            "rear_left_door": {"x": 220, "y": 520, "scale": 0.28},
            "front_right_door": {"x": 804, "y": 260, "scale": 0.28},
            "rear_right_door": {"x": 804, "y": 520, "scale": 0.28}
        }
    },
    {
        "id": "models-2021",
        "name": "Model S (2021+)",
        "subtitle": "Model S 2021+",
        "series": "Model S",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "ModelS_2021_Wrap.png",
        "hoodCenter": [512, 199],
        "placements": {
            "hood": {"x": 512, "y": 220, "scale": 0.30},
            "front_left_door": {"x": 145, "y": 380, "scale": 0.27},
            "rear_left_door": {"x": 150, "y": 645, "scale": 0.27},
            "front_right_door": {"x": 875, "y": 380, "scale": 0.27},
            "rear_right_door": {"x": 870, "y": 647, "scale": 0.27}
        }
    },
    {
        "id": "models-2025-plaid",
        "name": "Model S Plaid (2025+)",
        "subtitle": "Model S Plaid 2025+",
        "series": "Model S",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "ModelS_2025_Plaid_Wrap.png",
        "hoodCenter": [512, 217],
        "placements": {
            "hood": {"x": 512, "y": 230, "scale": 0.30},
            "front_left_door": {"x": 145, "y": 380, "scale": 0.27},
            "rear_left_door": {"x": 150, "y": 645, "scale": 0.27},
            "front_right_door": {"x": 875, "y": 380, "scale": 0.27},
            "rear_right_door": {"x": 870, "y": 647, "scale": 0.27}
        }
    },
    {
        "id": "modelx-2021",
        "name": "Model X (2021+)",
        "subtitle": "Model X 2021+",
        "series": "Model X",
        "width": 1024,
        "height": 1024,
        "defaultFileName": "ModelX_2021_Wrap.png",
        "hoodCenter": [512, 166],
        "placements": {
            "hood": {"x": 512, "y": 180, "scale": 0.30},
            "front_left_door": {"x": 220, "y": 380, "scale": 0.26},
            "rear_left_door": {"x": 220, "y": 645, "scale": 0.26},
            "front_right_door": {"x": 804, "y": 380, "scale": 0.26},
            "rear_right_door": {"x": 804, "y": 647, "scale": 0.26}
        }
    }
]

# Read existing heroes from presets.js
heroes = []
if os.path.exists('presets.js'):
    with open('presets.js', 'r', encoding='utf-8') as f:
        t = f.read()
        marker = 'window.TESLA_PRESETS = '
        start = t.find(marker)
        if start >= 0:
            existing_data, _ = json.JSONDecoder().raw_decode(t[start + len(marker):].lstrip())
            heroes = existing_data.get('heroes', [])

models_dict = {}

for m in models_meta:
    mid = m["id"]
    t_path = os.path.join(wraps_dir, mid, 'template.png')
    v_path = os.path.join(wraps_dir, mid, 'vehicle_image.png')
    
    with open(t_path, 'rb') as f:
        t_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')
    
    # generate thumbnail for vehicle_image
    v_b64 = ""
    if os.path.exists(v_path):
        vim = Image.open(v_path)
        vim.thumbnail((160, 160), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        vim.save(buf, format='PNG', optimize=True)
        v_b64 = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode('utf-8')
    
    m_copy = dict(m)
    m_copy["template"] = t_b64
    m_copy["vehicleImage"] = v_b64
    models_dict[mid] = m_copy
    print(f'Processed {mid}: width={m["width"]}, height={m["height"]}')

output = {
    "models": models_dict,
    "heroes": heroes,
    "defaultModel": "modely-l",
    "template": models_dict["modely-l"]["template"]
}

js_content = "// Tesla Wrap Editor - All 12 Official Vehicle Models & Presets\n"
js_content += "window.TESLA_MODELS = " + json.dumps(models_dict, ensure_ascii=False) + ";\n"
js_content += "window.TESLA_PRESETS = " + json.dumps(output, ensure_ascii=False) + ";\n"

with open('presets.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print('Successfully generated presets.js! Size:', os.path.getsize('presets.js') / 1024, 'KB')
