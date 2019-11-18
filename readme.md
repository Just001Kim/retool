# Retool
Retool scans [Redump](http://redump.org/) dats, and attempts to generate new
dats without dupes. Some call this 1G1R. This is not an official Redump project.

## Installation
If you don't know Python or don't want to deal with code, download the
appropriate ZIP file in the `dist` folder for Windows or MacOS. Only 64-bit
executables are available, 32-bit operating systems are not supported. Extract
and run the executable files directly, no installation is required.

Otherwise, _Retool_ requires a minimum of [Python 3.5](https://www.python.org/)
with `pip`.

You'll need to install two modules with `pip` before using _Retool_. To do so,
open Terminal, Command Prompt, or whatever the CLI is on your system, and type:

```python
pip install bs4
pip install lxml
```
### Troubleshooting pip
* Some systems have multiple versions of Python installed. You might need to
run `pip3` instead of `pip`.
* Python will complain that the `bs4` module doesn't exist if `pip`
is installing modules to the wrong folder for Python 3.x access. If using
`pip3` instead of `pip` doesn't fix the issue, do a web search to solve the
problem on your OS of choice.

## Usage
`python retool.py -i <input dat/folder> -o <output dat/folder> <options>`

Or for the binary version:

`retool  -i <input dat/folder> -o <output dat/folder> <options>`

**Note:** Some systems have the Python 3.x binary installed separately as
`python3`. You might need to run this instead of `python`.

## Options
* `-en` Only include English titles
* `-a` Remove applications
* `-d` Remove demos and coverdiscs
* `-e` Remove educational
* `-l` Remove titles with (Alt) tags
* `-m` Remove multimedia
* `-o` Set an output folder
* `-p` Remove betas and prototypes
* `-r` Split dat into regional dats
* `-s` Split dat into regional dats, include dupes

## How it works
The input dat is split into regions, then each region is processed in a
specific order. Each region cannot include titles that are in the regions
that precede it. The USA version of a title is usually considered canonical.

Regions are parsed in the following order:

1. USA
1. World
1. UK
1. Canada
1. Australia
1. New Zealand
1. Singapore
1. Ireland
1. Europe
1. Asia
1. Scandinavia
1. Japan
1. Argentina
1. Austria
1. Belgium
1. Brazil
1. China
1. Croatia
1. Czech
1. Denmark
1. Finland
1. France
1. Germany
1. Greece
1. Hungary
1. India
1. Israel
1. Italy
1. Korea
1. Latin America
1. Netherlands
1. Norway
1. Poland
1. Portugal
1. Russia
1. Slovakia
1. South Africa
1. Spain
1. Sweden
1. Switzerland
1. Taiwan
1. Thailand
1. Turkey
1. Ukraine
1. United Arab Emirates
1. Unknown

As the program progresses through the regions, `_regional_renames.py` is
referenced to check if any titles in the current region are the same as
another region's title, but with a different name. For example, apart from the
name, **_Dancing Stage Unleashed 3 (Europe)_** and
**_Dance Dance Revolution Ultramix 3 (USA)_** are the same title, and so
**_Dancing Stage Unleashed 3 (Europe)_** would not be included.

## FAQs
#### How did you figure out what the dupes were?
I went through each dat for games that weren't tagged as USA. I then used
[Wikipedia](https://www.wikipedia.org),
[Moby Games](https://www.mobygames.com),
[Retroplace](https://www.retroplace.com), [GameTDB](https://www.gametdb.com),
[VDGB](https://vgdb.io), [YouTube](https://www.youtube.com),
[Amazon.jp](https://www.amazon.co.jp) and good old web searching to turn up
information. I went through Redump's site for Japanese and Chinese characters
for the titles, so I could do translations and find out the equivalent English
titles. Later in the process I discovered
[FilterQuest](https://github.com/UnluckyForSome/FilterQuest), a similar tool,
and added some missing titles from there.

## Known limitations
Be aware of the following limitations when using _Retool_. These might or
might not be addressed in the future.

#### Doesn't remove single titles in favor of compilation titles
For example, **_Assassin's Creed - Ezio Trilogy_** does not supersede
**_Assassin's Creed II_**, **_Assassin's Creed - Brotherhood_**, and
**_Assassin's Creed - Revelations_**.

#### Doesn't remove different language versions from the same region
For example, **_Suffering, The - Ties That Bind (Europe) (En,Es,It)_** and
**_Suffering, The - Ties That Bind (Europe) (En,Fr)_**.

#### Can only follow Redump language tags for non-English countries
If Redump missed tagging titles from regions where English isn't their first
language (for example, Japan), those titles won't be included.

#### Will remove titles that have the same name in different regions, regardless of content or which version is better
For example:
* Some versions of singing titles have additional local tracks, yet only one
  version of the title will be included.
* Some regional versions of titles might be superior to, for example, USA
  titles with the same name, but only the USA title will be included.