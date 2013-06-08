#itermcolors2terminator
Convert iTerm2 [color scheme][l1] files (.itermcolors files) to [terminator][l2] color palletes.
There might be some differences in the color produced because of rounding during conversion.


##Usage: 
    ./convert.py <file|directory>


Accepts .itermcolors file or a directory containing .itermcolors files as argument.
The conversion results will be written to stdout.

Example: 

    ./convert.py symfony.itermcolors
    ./convert.py ~/iTerm-2-Color-Themes > terminatorschemes.txt

[l1]: http://code.google.com/p/iterm2/wiki/ColorGallery
[l2]: http://www.tenshu.net/p/terminator.html