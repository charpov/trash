# trash

A command-line program to trash files instead of permanently deleting them.

There are a few of those floating around, but this one has given me satisfaction for many years, so I thought I'd share.
On macOS, it uses the Finder to actually trash; on other systems, it simply renames and moves files to what is guessed as a suitable trash location.
Because I sometimes combine `find` with `trash`, I wrote the program so it can handle an extremely large number of files on the command-line.

The program is used as:

```commandline
trash [-q | --quiet] [files and dirs...]
```

`trash` invokes `trash.py` on macOS.
Both scripts should reside in the same location.
