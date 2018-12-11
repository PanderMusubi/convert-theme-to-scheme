# convert-theme-to-scheme

Convert Eclipse themes to [Spyder](https://github.com/spyder-ide/spyder/)
color schemes.

The follwing command downloads the Elcipse themes.

    ./1-download.sh

The subsequent command converts these themes to Spyder color schems to be
used in Python code or in in INI file.

    ./2-convert.sh

The INI file is to quickly test the output in the conversion. The content of
`test.ini` can be copied manually into `~/.config/spyder-py3/spyder.ini`.

The Python code is written to `generated.py` and can manually be copied into
Spyper's source file `spyder/spyder/config/main.py`.
