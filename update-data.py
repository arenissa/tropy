"""Update the embedded term bank after editing data.json: python3 update-data.py"""
import json
from pathlib import Path
root = Path(__file__).resolve().parent
terms = json.loads((root / 'data.json').read_text())
assert len({t['id'] for t in terms}) == len(terms), 'Duplicate term IDs'
for term in terms:
    assert term['variants'], term['name']
page = root / 'index.html'
text = page.read_text()
start = text.index('/* DATA START */')
end = text.index('/* DATA END */') + len('/* DATA END */')
data = '/* DATA START */\nconst TERMS=' + json.dumps(terms, ensure_ascii=False).replace('</', '<\\/') + ';\n/* DATA END */'
page.write_text(text[:start] + data + text[end:])
print(f'Embedded {len(terms)} terms into index.html')
