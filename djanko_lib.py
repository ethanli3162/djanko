import os
class pyx:
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><script src="https://cdn.jsdelivr.net/pyodide/v0.29.4/full/pyodide.js"></script></head><body></body></html>'
    def add_style(self, href):
        self.html = self.html.replace('</head>', f'<link rel="stylesheet" href="{href}"></head>')
    def add_script(self, src):
        self.html = self.html.replace('</head>', f'<script src="{src}"></script></head>')
    def add_metadata(self, metadata):
        self.html = self.html.replace('</head>', f'{metadata}</head>')
    def add(self, content):
        self.html = self.html.replace('</body>', f'{content}</body>')
    def compile(self):
        return self.html
    def title(self, title):
        self.html = self.html.replace('</head>', f'<title>{title}</title></head>')
    def lang(self, lang):
        self.html = self.html.replace('<html', f'<html lang="{lang}"')
    def charset(self, charset):
        self.html = self.html.replace('<head>', f'<head><meta charset="{charset}">')
    def viewport(self, content):
        self.html = self.html.replace('<head>', f'<head><meta name="viewport" content="{content}">')
    def python(self, code, compiler='py', terminal=False):
        if terminal:
            self.html = self.html.replace('</body>', f'<script type="{compiler}" terminal>{code}</script></body>')
        else:
            self.html = self.html.replace('</body>', f'<script type="{compiler}">{code}</script></body>')

def paragraph(text, styles=None, id=None):
    if styles:
        if id:
            return (f'<p id="{id}" class="{styles}">{text}</p>')
        else:
            return (f'<p class="{styles}">{text}</p>')
    else:
        if id:
            return (f'<p id="{id}">{text}</p>')
        else:
            return (f'<p>{text}</p>')
def heading(text, level=1, styles=None, id=None):
    if styles:
        if id:
            return (f'<h{level} id="{id}" class="{styles}">{text}</h{level}>')
        else:
            return (f'<h{level} class="{styles}">{text}</h{level}>')
    else:
        if id:
            return (f'<h{level} id="{id}">{text}</h{level}>')
        else:
            return (f'<h{level}>{text}</h{level}>')
def image(src, alt='', styles=None, id=None):
    if styles:
        if id:
            return (f'<img src="{src}" alt="{alt}" id="{id}" class="{styles}">')
        else:
            return (f'<img src="{src}" alt="{alt}" class="{styles}">')
    else:
        if id:
            return (f'<img src="{src}" alt="{alt}" id="{id}">')
        else:
            return (f'<img src="{src}" alt="{alt}">')
def link(href, text, styles=None, id=None):
    if styles:
        if id:
            return (f'<a href="{href}" class="{styles}" id="{id}">{text}</a>')
        else:
            return (f'<a href="{href}" class="{styles}">{text}</a>')
    else:
        if id:
            return (f'<a href="{href}" id="{id}">{text}</a>')
        else:
            return (f'<a href="{href}">{text}</a>')
def br():
    return '<br>'
def hr():
    return '<hr>'

def python(code):
    return '<script type="text/javascript">async function main(){let pyodide = await loadPyodide();console.log(pyodide.runPython(`' + code + '`));}main();</script>'

def pyscript(filename):
    filename = os.path.join(os.getcwd(), filename)
    with open(filename, 'r') as f:
        return f.read().replace('from djanko_lib import *', '')

def style(name, value):
    css = '.' + name + ' { '
    for i in range(len(value)):
        css += f'{value[i]};'
    css += '}'
    css = f'<style>{css}</style>'
    return css

def serve_pyx(filename):
    output_variables = {}
    filename = os.path.join(os.getcwd(), filename)
    with open(filename, 'r') as f:
        pyxcode = f.read()
    exec(pyxcode, output_variables)
    return output_variables.get('content')

def script(code):
    return ('</body>', f'<script>{code}</script></body>')
