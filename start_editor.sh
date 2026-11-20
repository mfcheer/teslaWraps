#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"
echo "正在启动 Tesla 全车型车机皮肤可视化编辑器 (Tesla Wrap Studio)..."
open "$DIR/index.html"
echo "已在默认浏览器中打开: file://$DIR/index.html"
