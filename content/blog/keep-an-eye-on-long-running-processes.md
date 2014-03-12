Title: 'Watch' long running processes
Date: 2009-07-08 12:23
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful tip
Tags: long running, PostGIS, watch, Free open-source software (FOSS), How to, Linux
Slug: keep-an-eye-on-long-running-processes

The other day I was loading a shapefile of approximately 11 million
records into a PostGIS database (stay tuned for more on that later) and
I wanted to know when shp2pgsql was done. Instead of continually
checking the console, I decided to 'watch' the process using the *nix
command `watch`. I discovered this handy tool a while ago, and have
found that for long running processes, I can use `watch` to notify me
when the process has finished, using the following command:

```bash
watch -ben 1 "ps u -C shp2pgsql"
```
<!--more-->

In this case, the three parameters `b`, `e`, and `n` tell `watch` to
`[b]`eep if the command has a non-zero exit (in this case when `shp2pgsql`
is no longer running), `[e]`xit watch if the command has a non-zero exit
(again when `shp2pgsql` is done), and the i`[n]`terval (in seconds) to wait
between updates (in this case 1 second). The rest of the command,
`ps u -C` is the command that `watch` runs each second. In this case, it
uses `ps` to report info on the running process, where the `-C` flag
tells `ps` to report the process matching the name `"shp2pgsql"`. When
`shp2pgsql` is no longer running, `ps u -C` will have a non-zero exit,
and I get my beep: very handy!
This can be made even more useful by changing the above command to:

```bash
watch -ben 1 "ps u -C shp2pgsql"; mail -s "Process complete!" email.address@some.one < /home/username/email_text.txt
```

Here I've added the `mail` command to send me an email when `watch`
exits (the ';' simply allows me to have two commands on one line). If
you're really smart, you could probably have `watch` save important info
about the running process to a file and send this with the email, but
for my purposes, the above works just fine.

The next step is figuring out how to make my computer text me when a
long process is complete... and thanks to [Will][], I may be [one step
closer][] to this goal.

[Will]: https://twitter.com/w_dowling
[one step closer]: http://o2sms.sourceforge.net/
