Title: Find and replace multiple files
Date: 2008-09-08 09:09
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful tip
Tags: Helpful tip, Linux, How to
Slug: find-and-replace-multiple-files

Recently, I had to do a find and replace over several individual python
files.There are plenty of scripts out there which will accomplish this,
but I was interested in something simple, and preferably a single line
command. After a lot of Google-ing, I ended up finding [this post][],
which does a great job of explaining how to do this in linux. The basic
command is:

```bash
find . -name "\*.py" -print | xargs sed -i 's/foo/bar/g'
```

where `find . -name "*.py"` is used to find all python files (recursively) in 
your directory,  and `xargs sed -i 's/foo/bar/g'` is used to replace all 
occurrences of 'foo' in the files with 'bar'.
The link above gives a good explanation of each command (find, xargs, sed), 
and how they combine together to create this useful single line command.

[this post]: http://rushi.wordpress.com/2008/08/05/find-replace-across-multiple-files-in-linux/#comment-26487
