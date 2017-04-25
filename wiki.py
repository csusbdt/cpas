# This script does two things:
#     (1) Convert INDIR/*.md to HTML and place in OUTDIR.
#     (2) Copy github-markdown.css to OUTDIR.

import platform

if platform.python_version_tuple()[0] < '3':
    print("This script requires Python version 3.")
    exit(1)

import markdown
import codecs
from pathlib import Path
from shutil import copy2 as copyfile

INDIR = "../cpas.wiki/"
OUTDIR = "docs/"

md = markdown.Markdown([
    "markdown.extensions.wikilinks(base_url=, end_url=.html)", 
    "markdown.extensions.tables",
    "markdown.extensions.fenced_code"]
)

template = ''
with open('template.html', 'r') as f:
    template = f.read()

def createPage(filename):
    global template
    inpath = INDIR + filename + ".md"
    outpath = OUTDIR + filename + ".html"
    outfile = codecs.open(outpath, "w", encoding="utf-8", errors="xmlcharrefreplace")
    infile = codecs.open(inpath, mode="r", encoding="utf-8")
    intext = infile.read()

    content = md.convert(intext) 

    outtext = template.replace('[[content]]', content)

    outfile.write(outtext)

print("(1) Converting " + INDIR + "*.md to HTML and placing into " + OUTDIR)
print("(2) Copying github-markdown.css to " + OUTDIR)

wikiPagesDirectory = Path(INDIR)
for x in wikiPagesDirectory.iterdir():
    if not x.is_dir():
        createPage(x.stem)

copyfile("github-markdown.css", "docs")
print("Done.")

