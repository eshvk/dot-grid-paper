# Dot Grid Paper

These are PDF templates for 0.25 inch dot grid paper in US letter, A4 A6 and Good Note Essentials formats.

## Overview

Since they are in PDF format, the are useful for:

*   Printing your own dot grid paper
*   Templates in apps such as [GoodNotes][] ([iOS][], [macOS][])

Several variations are included:

*   _Orientation:_ portrait or landscape (Landscape available only for US Letter)
*   _Margin:_ top margin or full grid
*   _Color:_ white or "antique"
*	_Paper Size:_ U.S. Letter (`8.5"X11"`), A4(`8.27"X11.7"`), A6(`4.1"X5.8"`), [GoodNotes Essentials Custom Size][](`5.82"X7.42"`)

## Package Contents

*   `dot-grid.sty` - A LaTeX package which defines colors, margins, and a dot grid macro using TikZ.
*   `dot-grid.py` - A Python script which generates the TeX files.

## Usage

1.   Run `dot-grid.py` to produce the `.tex` files directly into the tex directory.
2.   Run `pdflatex` on each `.tex` file as needed.  For example:
```
         for file in tex/*.tex; do pdflatex $file; done;
```
This will create the pdfs in the root directory.Or, simply use the included output files in the `pdf` directory.

## Specifications

*   For templates with a top margin, the first two rows of dots are omitted.
*   Antique color is `rgb(255, 255, 244)` or `#fffff4`.
*   Dot color is `rgb(204, 204, 198)` or `#ccccc6`.
*   Dot radius is 0.01 inches.

[GoodNotes]: http://www.goodnotesapp.com
[GoodNotes Essentials Custom Size]: https://twitter.com/goodnotesapp/status/443678100140720128
[iOS]: https://itunes.apple.com/us/app/goodnotes-4-notes-pdf/id778658393?mt=8&uo=4&at=11l5Vs
[macOS]: https://itunes.apple.com/us/app/goodnotes/id1026566364?mt=12&uo=4&at=11l5Vs
