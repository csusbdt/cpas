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

header = '''<html>
  <head>
    <title>CSE 1010</title>

      <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
      <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
      <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>

    <!-- stylesheet from http://www.bootcdn.cn/github-markdown-css/ -->
    <link rel="stylesheet" href="github-markdown.css">
    <style>
      .markdown-body {
        box-sizing: border-box;
        min-width: 200px;
        max-width: 850px; /* 980px; */
        margin: 0 auto;
        padding: 45px;
      }
      .menu {
        padding-bottom: .3em;
        border-bottom: 1px solid #eaecef;
      }
    </style>
  </head>
  <body>
    <div class='markdown-body'>
      <div class="menu">
        <span>CSE 1010</span> &bull;
        <a href="Home.html">Home</a> &#9702; 
        <a href="https://github.com/csusbdt/cpas/wiki">Wiki</a> <br>
      </div>
'''

footer = '''
    </div>
  </body>
</htlm>
'''

md = markdown.Markdown([
    "markdown.extensions.wikilinks(base_url=, end_url=.html)", 
    "markdown.extensions.tables",
    "markdown.extensions.fenced_code"]
)

def createPage(filename):
    inpath = INDIR + filename + ".md"
    outpath = OUTDIR + filename + ".html"
    outfile = codecs.open(outpath, "w", encoding="utf-8", errors="xmlcharrefreplace")
    infile = codecs.open(inpath, mode="r", encoding="utf-8")
    intext = infile.read()
    outtext = header + md.convert(intext) + footer
    outfile.write(outtext)

print("(1) Converting " + INDIR + "*.md to HTML and placing into " + OUTDIR)
print("(2) Copying github-markdown.css to " + OUTDIR)

wikiPagesDirectory = Path(INDIR)
for x in wikiPagesDirectory.iterdir():
    if not x.is_dir():
        createPage(x.stem)

copyfile("github-markdown.css", "docs")
print("Done.")

