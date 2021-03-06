#!/usr/bin/env python3

from xml.etree import ElementTree
from glob import glob
from sys import stderr

py = open('generated.py', 'w')
ini = open('test.ini', 'w')

# these were already manually ported to Spyder
existing = ['emacs', 'idle', 'monokai', 'pydev', 'scintilla',
            'spyder', 'spyder/dark', 'zenburn', 'solarized/light',
            'solarized/dark']
names = []
for filename in sorted(glob('eclipse-color-theme-master/com.github.eclipsecolortheme/themes/*.xml')):
    root = ElementTree.parse(filename).getroot()
    name = root.attrib['name'].lower().replace(' ', '/')
    if name in existing:
        continue
    if name == 'sublime/text/monokai/extended':
        name = 'sublime/te/mo/ex'
    
    names.append(name)

if not names:
    print("Could not find any themes", file=stderr)
    exit(1)

py.write(", '{}'\n\n".format("', '".join(names)))
py.write("              # Generated by https://github.com/PanderMusubi/convert-theme-to-scheme\n")

ini.write("[color_schemes]\n")
ini.write("names = ['{}']\n".format("', '".join(names)))
ini.write("selected = {}\n\n".format(names[0]))
ini.write("# Generated by https://github.com/PanderMusubi/convert-theme-to-scheme\n")
    
errors = []
for filename in sorted(glob('eclipse-color-theme-master/com.github.eclipsecolortheme/themes/*.xml')):
    root = ElementTree.parse(filename).getroot()
    fullname = root.attrib['name'].title()
    fullname = fullname.replace('Recogneyes', 'RecognEyes').replace('Nightlion', 'NightLion') 
    name = fullname.lower().replace(' ', '/')
    if name in existing:
        continue
    print("Converting {}...".format(fullname))
    if name == 'sublime/text/monokai/extended':
        name = 'sublime/te/mo/ex'

    # background colors
    background = None # Background
    currentline = None # Current line
    currentcell = None # Current cell
    occurence = None # Occurrence
    ctrlclick = None # Link
    sideareas = None # Side areas
    matched_p = None # Matched parens
    unmatched_p = None # Unmatched parens

    # foreground colors
    normal = None # Normal text
    keyword = None # Keyword
    builtin = None # Builtin
    definition = None # Definition
    comment = None # Comment
    string = None # String
    number = None # Number
    instance = None # Instance
    
    normal_bold = False
    keyword_bold = False
    builtin_bold = False
    definition_bold = False
    comment_bold = False
    string_bold = False
    number_bold = False
    instance_bold = False

    normal_italic = False
    keyword_italic = False
    builtin_italic = False
    definition_italic = False
    comment_italic = False
    string_italic = False
    number_italic = False
    instance_italic = False
    
    for color in root:
        # background colors
        if color.tag.lower() == 'background'.lower():
            background = color.attrib['color'].lower() # same
            currentcell = color.attrib['color'].lower() # custom mapped
        elif color.tag.lower() == 'currentLine'.lower():
            currentline = color.attrib['color'].lower() # same
            sideareas = color.attrib['color'].lower() # custom mapped
        elif color.tag.lower() == 'occurrenceIndication'.lower():
            occurence = color.attrib['color'].lower() # same
        elif color.tag.lower() == 'javadoc'.lower():
            ctrlclick = color.attrib['color'].lower() # custom mapped
        elif color.tag.lower() == 'selectionBackground'.lower():
            unmatched_p = color.attrib['color'].lower() # custom mapped
            
        # foreground colors
        elif color.tag.lower() == 'foreground'.lower():
            normal = color.attrib['color'].lower() # mapped
            if 'bold' in color.attrib and color.attrib['bold'].lower() == 'true':
                normal_bold = True
            if 'italic' in color.attrib and color.attrib['italic'].lower() == 'true':
                normal_italic = True
            matched_p = color.attrib['color'].lower() # custom mapped
        elif color.tag.lower() == 'field'.lower():
            instance = color.attrib['color'].lower() # custom mapped
            if 'bold' in color.attrib and color.attrib['bold'].lower() == 'true':
                instance_bold = True
            if 'italic' in color.attrib and color.attrib['italic'].lower() == 'true':
                instance_italic = True
        elif color.tag.lower() == 'keyword'.lower():
            keyword = color.attrib['color'].lower() # same
            if 'bold' in color.attrib and color.attrib['bold'].lower() == 'true':
                keyword_bold = True
            if 'italic' in color.attrib and color.attrib['italic'].lower() == 'true':
                keyword_italic = True
        elif color.tag.lower() == 'class'.lower():
            builtin = color.attrib['color'].lower() # custom mapped
            if 'bold' in color.attrib and color.attrib['bold'].lower() == 'true':
                builtin_bold = True
            if 'italic' in color.attrib and color.attrib['italic'].lower() == 'true':
                builtin_italic = True
        elif color.tag.lower() == 'method'.lower():
            definition = color.attrib['color'].lower() # custom mapped
            if 'bold' in color.attrib and color.attrib['bold'].lower() == 'true':
                definition_bold = True
            if 'italic' in color.attrib and color.attrib['italic'].lower() == 'true':
                definition_italic = True
        elif color.tag.lower() == 'singleLineComment'.lower():
            comment = color.attrib['color'].lower() # same
            if 'bold' in color.attrib and color.attrib['bold'].lower() == 'true':
                comment_bold = True
            if 'italic' in color.attrib and color.attrib['italic'].lower() == 'true':
                comment_italic = True
        elif color.tag.lower() == 'string'.lower():
            string = color.attrib['color'].lower() # same
            if 'bold' in color.attrib and color.attrib['bold'].lower() == 'true':
                string_bold = True
            if 'italic' in color.attrib and color.attrib['italic'].lower() == 'true':
                string_italic = True
        elif color.tag.lower() == 'number'.lower():
            number = color.attrib['color'].lower() # same
            if 'bold' in color.attrib and color.attrib['bold'].lower() == 'true':
                number_bold = True
            if 'italic' in color.attrib and color.attrib['italic'].lower() == 'true':
                number_italic = True
        
    if ctrlclick == None:
        ctrlclick = background # fallback

    if instance == None:
        instance = normal # fallback

    if background == None:
        errors.append('ERROR: Missing background for {}'.format(name))
    if currentline == None:
        errors.append('ERROR: Missing currentline for {}'.format(name))
    if currentcell == None:
        errors.append('ERROR: Missing currentcell for {}'.format(name))
    if occurence == None:
        errors.append('ERROR: Missing occurence for {}'.format(name))
    if ctrlclick == None:
        errors.append('ERROR: Missing ctrlclick for {}'.format(name))
    if sideareas == None:
        errors.append('ERROR: Missing sideareas for {}'.format(name))
    if matched_p == None:
        errors.append('ERROR: Missing matched_p for {}'.format(name))
    if unmatched_p == None:
        errors.append('ERROR: Missing unmatched_p for {}'.format(name))
    if normal == None:
        errors.append('ERROR: Missing normal for {}'.format(name))
    if keyword == None:
        errors.append('ERROR: Missing keyword for {}'.format(name))
    if builtin == None:
        errors.append('ERROR: Missing builtin for {}'.format(name))
    if definition == None:
        errors.append('ERROR: Missing definition for {}'.format(name))
    if comment == None:
        errors.append('ERROR: Missing comment for {}'.format(name))
    if string == None:
        errors.append('ERROR: Missing string for {}'.format(name))
    if number == None:
        errors.append('ERROR: Missing number for {}'.format(name))
    if instance == None:
        errors.append('ERROR: Missing instance for {}'.format(name))

    w = len(name) + 15
    py.write("              # ---- {} (Eclipse color theme) ----\n".format(fullname))
    py.write("              {a: <{b}} \"{c}\",\n".format(a="'{}/name':".format(name), b=w, c=fullname))
    py.write("              #      Name       {a: <{b}}Color     Bold  Italic\n".format(a=' ', b=w-15))

    py.write("              {a: <{b}} \"{c}\",\n".format(a="'{}/background':".format(name), b=w, c=background))
    py.write("              {a: <{b}} \"{c}\",\n".format(a="'{}/currentline':".format(name), b=w, c=currentline))
    py.write("              {a: <{b}} \"{c}\",\n".format(a="'{}/currentcell':".format(name), b=w, c=currentcell))
    py.write("              {a: <{b}} \"{c}\",\n".format(a="'{}/occurence':".format(name), b=w, c=occurence))
    py.write("              {a: <{b}} \"{c}\",\n".format(a="'{}/ctrlclick':".format(name), b=w, c=ctrlclick))
    py.write("              {a: <{b}} \"{c}\",\n".format(a="'{}/sideareas':".format(name), b=w, c=sideareas))
    py.write("              {a: <{b}} \"{c}\",\n".format(a="'{}/matched_p':".format(name), b=w, c=matched_p))
    py.write("              {a: <{b}} \"{c}\",\n".format(a="'{}/unmatched_p':".format(name), b=w, c=unmatched_p))
    
    py.write("              {a: <{b}}('{c}', {d}, {e}),\n".format(a="'{}/normal':".format(name), b=w, c=normal, d=normal_bold, e=normal_italic))
    py.write("              {a: <{b}}('{c}', {d}, {e}),\n".format(a="'{}/keyword':".format(name), b=w, c=keyword, d=keyword_bold, e=keyword_italic))
    py.write("              {a: <{b}}('{c}', {d}, {e}),\n".format(a="'{}/builtin':".format(name), b=w, c=builtin, d=builtin_bold, e=builtin_italic))
    py.write("              {a: <{b}}('{c}', {d}, {e}),\n".format(a="'{}/definition':".format(name), b=w, c=definition, d=definition_bold, e=definition_italic))
    py.write("              {a: <{b}}('{c}', {d}, {e}),\n".format(a="'{}/comment':".format(name), b=w, c=comment, d=comment_bold, e=comment_italic))
    py.write("              {a: <{b}}('{c}', {d}, {e}),\n".format(a="'{}/string':".format(name), b=w, c=string, d=string_bold, e=string_italic))
    py.write("              {a: <{b}}('{c}', {d}, {e}),\n".format(a="'{}/number':".format(name), b=w, c=number, d=number_bold, e=number_italic))
    py.write("              {a: <{b}}('{c}', {d}, {e}),\n".format(a="'{}/instance':".format(name), b=w, c=instance, d=instance_bold, e=instance_italic))
    
    ini.write("{}/name = {}\n".format(name, fullname))

    ini.write("{}/background = {}\n".format(name, background))
    ini.write("{}/currentline = {}\n".format(name, currentline))
    ini.write("{}/currentcell = {}\n".format(name, currentcell))
    ini.write("{}/occurence = {}\n".format(name, occurence))
    ini.write("{}/ctrlclick = {}\n".format(name, ctrlclick))
    ini.write("{}/sideareas = {}\n".format(name, sideareas))
    ini.write("{}/matched_p = {}\n".format(name, matched_p))
    ini.write("{}/unmatched_p = {}\n".format(name, unmatched_p))
    
    ini.write("{}/normal = ('{}', {}, {})\n".format(name, normal, normal_bold, normal_italic))
    ini.write("{}/keyword = ('{}', {}, {})\n".format(name, keyword, keyword_bold, keyword_italic))
    ini.write("{}/builtin = ('{}', {}, {})\n".format(name, builtin, builtin_bold, builtin_italic))
    ini.write("{}/definition = ('{}', {}, {})\n".format(name, definition, definition_bold, definition_italic))
    ini.write("{}/comment = ('{}', {}, {})\n".format(name, comment, comment_bold, comment_italic))
    ini.write("{}/string = ('{}', {}, {})\n".format(name, string, string_bold, string_italic))
    ini.write("{}/number = ('{}', {}, {})\n".format(name, number, number_bold, number_italic))
    ini.write("{}/instance = ('{}', {}, {})\n".format(name, instance, instance_bold, instance_italic))
    
for error in errors:
    print(error, file=stderr)
if errors:
    exit(1)
