#!/usr/bin/python
papertypes = ['portrait', 'landscape',
              'a4paper', 'a6paper', 'gnessentialsportrait']
colors = ['white', 'antique']
styles = ['full', 'margin']

for papertype in papertypes:
    for color in colors:
        for style in styles:
            fn = 'tex/dot.grid.%s.%s.%s.tex' % (papertype, color, style)
            print('Generating %s...' % fn)
            f = open(fn, 'w+')
            f.write('\\documentclass[%s]{article}\n' % (papertype))
            if papertype is 'gnessentialsportrait':
                f.write(
                    '\\usepackage[paperwidth=5.82in,paperheight=7.42in]{geometry}\n')
            f.write('\\usepackage[dot%s]{dot-grid}\n' % style)
            f.write('\\pagecolor{%s}\n' % color)
            f.write('\\begin{document}\n')
            f.write('\\dotgrid\n')
            f.write('\\end{document}\n')
            f.close()
