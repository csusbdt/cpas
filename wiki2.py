# This script reads wiki markdown from this project's wiki 
# and converts to HTML and stores the result in docs.
# It also copies github-markdown.css to docs.

import platform
import markdown
import codecs
import urllib.request
from pathlib import Path
from shutil import copy2 as copyfile
from git import Repo

if platform.python_version_tuple()[0] < '3':
    print("This script requires Python version 3.")
    exit(1)

url = 'https://raw.githubusercontent.com/wiki/csusbdt/cse2/index.md'
contents = urllib.request.urlopen(url).read().decode('utf-8')

copyfile("github-markdown.css", "docs")

md = markdown.Markdown([
    "markdown.extensions.wikilinks(base_url=, end_url=.html)", 
    "markdown.extensions.tables",
    "markdown.extensions.fenced_code"]
)

template = ''
with open('template.html', 'r') as f:
    template = f.read()

def createPage(pageTitle):
    global template
    url = 'https://raw.githubusercontent.com/wiki/csusbdt/cpas/' + pageTitle + '.md'
    wikiText = urllib.request.urlopen(url).read().decode('utf-8')
    content = md.convert(wikiText) 
    html = template.replace('[[content]]', content)
    outpath = 'docs/' + pageTitle + '.html'
    outfile = codecs.open(outpath, "w", encoding="utf-8", errors="xmlcharrefreplace")
    outfile.write(html)

pageTitles = [
    "Home",
    "Experience-Working-with-Python",
    "Install-Python",
    "Learn-the-Python-Language",
    "Classes",
    "Experiment-with-Blender",
    "Working-in-a-Python3-Virtual-Environment",
    "Blender-Notes"
]

for pageTitle in pageTitles:
    createPage(pageTitle)

repo = Repo('.')

repo.index.add(['docs/' + pageTitle + '.html' for pageTitle in pageTitles])
repo.index.commit('push docs')
repo.remote('origin').push()

print("Done.")

