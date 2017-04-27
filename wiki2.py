# This script does two things:
#     (1) Read wiki markdown from this project's wiki and converts to HTML.
#     (2) Copy github-markdown.css to OUTDIR.

import platform

if platform.python_version_tuple()[0] < '3':
    print("This script requires Python version 3.")
    exit(1)

import urllib.request

url = 'https://raw.githubusercontent.com/wiki/csusbdt/cse2/index.md'
contents = urllib.request.urlopen(url).read().decode('utf-8')

import markdown
import codecs
from pathlib import Path
from shutil import copy2 as copyfile

OUTDIR = "docs/"

md = markdown.Markdown([
    "markdown.extensions.wikilinks(base_url=, end_url=.html)", 
    "markdown.extensions.tables",
    "markdown.extensions.fenced_code"]
)

template = ''
with open('template.html', 'r') as f:
    template = f.read()

from pathlib import Path
import codecs

import markdown

def createPage(pageTitle):
    global template
    url = 'https://raw.githubusercontent.com/wiki/csusbdt/cpas/' + pageTitle + '.md'
    wikiText = urllib.request.urlopen(url).read().decode('utf-8')
    outpath = OUTDIR + pageTitle + ".html"
    outfile = codecs.open(outpath, "w", encoding="utf-8", errors="xmlcharrefreplace")
    content = md.convert(wikiText) 
    html = template.replace('[[content]]', content)
    outfile.write(html)

createPage("Home")
createPage("Experience-Working-with-Python")
createPage("Install-Python")
createPage("Learn-the-Python-Language")
createPage("Classes")
createPage("Experiment-with-Blender")
createPage("Working-in-a-Python3-Virtual-Environment")
createPage("Blender-Notes")

copyfile("github-markdown.css", "docs")

# Push into remote repo.

from git import Repo

repo = Repo('.')

path_list = Path('./docs').glob('*.html')
file_list = [p.as_posix() for p in path_list]

repo.index.add(file_list)
repo.index.commit('push docs')
origin = repo.remote('origin')
origin.push()

print("Done.")

