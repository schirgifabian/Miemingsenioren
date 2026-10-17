"""Builds index.html (standalone page with app icon) from kleiderordnung.html (the Claude artifact page)."""
from pathlib import Path

root = Path(__file__).parent
fragment = (root / "kleiderordnung.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<meta name="theme-color" content="#1C4733">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Golf-Kleidung">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
(root / "index.html").write_text(head + fragment + "\n</body>\n</html>\n", encoding="utf-8")
print("index.html geschrieben")
