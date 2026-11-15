import base64, re, pathlib, zipfile

root = pathlib.Path(__file__).parent
html = (root / 'index.html').read_text(encoding='utf-8')
css = (root / 'css' / 'styles.css').read_text(encoding='utf-8')
js = (root / 'js' / 'main.js').read_text(encoding='utf-8')

def data_uri(match):
    path = root / match.group(0)
    mime = 'image/png' if path.suffix == '.png' else 'image/jpeg'
    return 'data:%s;base64,%s' % (mime, base64.b64encode(path.read_bytes()).decode())

html = html.replace('<link rel="stylesheet" href="css/styles.css">', '<style>\n%s\n</style>' % css)
html = html.replace('<script src="js/main.js" defer></script>', '<script>\n%s\n</script>' % js)
html = re.sub(r'assets/img/[\w.\-]+', data_uri, html)

dist = root / 'dist'
dist.mkdir(exist_ok=True)
(dist / 'sc-couverture-maquette.html').write_text(html, encoding='utf-8')

with zipfile.ZipFile(dist / 'sc-couverture-projet.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for p in ['index.html', 'build.py', 'README.md']:
        z.write(root / p, 'sc-couverture/' + p)
    for folder in ['css', 'js', 'assets']:
        for f in (root / folder).rglob('*'):
            if f.is_file():
                z.write(f, 'sc-couverture/' + str(f.relative_to(root)))
print('ok')
