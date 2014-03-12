Title: gedit: The ultimate LaTeX editor
Date: 2008-12-12 00:56
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful tip
Tags: gedit, LaTeX, Free open-source software (FOSS), How to, Linux
Slug: gedit-the-ultimate-latex-editor
Latex:

Out of the box *gedit* is a basic text editor, but it comes equipped
with about 12 standard plugins, and another 9 readily available. In
addition to this, there are a range of 'third-party' plugins developed
to do various specific tasks, such as assist you in writing and
exporting LaTeX documents!
<!--more-->
First, get all the basic plugins:
```bash
sudo apt-get install gedit-plugins`
```
and enable them in gedit by going to `Edit > Preferences > Plugins`, and
checking the ones that you want.

Second, make sure you have all the required dependencies for the actual
$\LaTeX$ plugin:
1. The plugin is written in Python 2.4 and relies on PyGTK 2.4: `sudo apt-get install python-gtk2`
2. Ensure that you have rubber installed. It is used for automated document 
compiling: `sudo apt-get install rubber`
3. To use the DVI inverse search you need the Python bindings for D-BUS: `sudo apt-get install python-dbus`

Third, download the latest version of the $\LaTeX$ plugin from [here][],
and extract and copy the contained folder and a file to
`~/.gnome2/gedit/plugins`. You may have to create `gedit/plugins` if you 
haven't installed any other plugins yet.

After that, restart `gedit` and activate the plugin in the settings
dialog as we did with the other plugins.

Now you have an editor with all sorts of handy functions, including
inline spell check, code completion, tag, symbol, and character
insertion, a file and document browser, and an embedded terminal, as
well as tools to automatically create new $\LaTeX$ files, insert graphics,
tables, and matrices, and a fantastic dialog for automatically inserting
BibTeX entries. Also, if you're an R user who creates reports etc. you
can use Sweave directly from gedit to embed R code in your LaTeX
documents.

All this in a lightweight text editor, nice!

[here]: http://live.gnome.org/Gedit/LaTeXPlugin
