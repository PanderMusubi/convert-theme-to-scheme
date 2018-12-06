#!/usr/bin/env python3

from xml.etree import ElementTree
from glob import glob
from sys import stderr

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
        name = 'sublime/text/monokai/ext'
    
    names.append(name)

print(", '{}'".format("', '".join(names)))
print()
    
errors = []
for filename in sorted(glob('eclipse-color-theme-master/com.github.eclipsecolortheme/themes/*.xml')):
    root = ElementTree.parse(filename).getroot()
    fullname = root.attrib['name']
    name = fullname.lower().replace(' ', '/')
    if name in existing:
        continue
    if name == 'sublime/text/monokai/extended':
        name = 'sublime/text/monokai/ext'

    background = None
    currentline = None
    occurence = None
    ctrlclick = None
    sideareas = None
    matched_p = None
    unmatched_p = None

    normal = None
    keyword = None
    builtin = None
    definition = None
    comment = None
    string = None
    number = None
    instance = None
    
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
        if color.tag.lower() == 'background'.lower():
            background = color.attrib['color'].lower() # same
            sideareas = color.attrib['color'].lower() # mapped
        elif color.tag.lower() == 'currentLine'.lower():
            currentline = color.attrib['color'].lower() # same
        elif color.tag.lower() == 'searchResultIndication'.lower():
            occurence = color.attrib['color'].lower() # mapped
        elif color.tag.lower() == 'javadocLink'.lower():
            ctrlclick = color.attrib['color'].lower() # custom mapped
        elif color.tag.lower() == 'occurrenceIndication'.lower():
            matched_p = color.attrib['color'].lower() # custom mapped
        elif color.tag.lower() == 'selectionBackground'.lower():
            unmatched_p = color.attrib['color'].lower() # custom mapped
            
        elif color.tag.lower() == 'foreground'.lower():
            normal = color.attrib['color'].lower() # mapped
            if 'bold' in color.attrib and color.attrib['bold'].lower() == 'true':
                normal_bold = True
            if 'italic' in color.attrib and color.attrib['italic'].lower() == 'true':
                normal_italic = True
            instance = color.attrib['color'].lower() # mapped
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
        elif color.tag.lower() == 'enum'.lower():
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
        
    if occurence == None:
        occurence = currentline # fallback
    if builtin == None:
        builtin = currentline # fallback
    if ctrlclick == None:
        ctrlclick = currentline # fallback

    if background == None:
        errors.append('ERROR: Missing background for {}'.format(name))
    if currentline == None:
        errors.append('ERROR: Missing currentline for {}'.format(name))
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
    print("              # ---- {} (converted Eclipse color theme) ----".format(fullname))
    print("              {a: <{b}} \"{c}\",".format(a="'{}/name':".format(name), b=w, c=fullname))
    print("              #      Name       {a: <{b}}Color     Bold  Italic".format(a=' ', b=w-15))

    print("              {a: <{b}} \"{c}\",".format(a="'{}/background':".format(name), b=w, c=background))
    print("              {a: <{b}} \"{c}\",".format(a="'{}/currentline':".format(name), b=w, c=currentline))
    print("              {a: <{b}} \"{c}\",".format(a="'{}/occurence':".format(name), b=w, c=occurence))
    print("              {a: <{b}} \"{c}\",".format(a="'{}/ctrlclick':".format(name), b=w, c=ctrlclick))
    print("              {a: <{b}} \"{c}\",".format(a="'{}/sideareas':".format(name), b=w, c=sideareas))
    print("              {a: <{b}} \"{c}\",".format(a="'{}/matched_p':".format(name), b=w, c=matched_p))
    print("              {a: <{b}} \"{c}\",".format(a="'{}/unmatched_p':".format(name), b=w, c=unmatched_p))
    
    print("              {a: <{b}}('{c}', {d}, {e}),".format(a="'{}/normal':".format(name), b=w, c=normal, d=normal_bold, e=normal_italic))
    print("              {a: <{b}}('{c}', {d}, {e}),".format(a="'{}/keyword':".format(name), b=w, c=keyword, d=keyword_bold, e=keyword_italic))
    print("              {a: <{b}}('{c}', {d}, {e}),".format(a="'{}/builtin':".format(name), b=w, c=builtin, d=builtin_bold, e=builtin_italic))
    print("              {a: <{b}}('{c}', {d}, {e}),".format(a="'{}/definition':".format(name), b=w, c=definition, d=definition_bold, e=definition_italic))
    print("              {a: <{b}}('{c}', {d}, {e}),".format(a="'{}/comment':".format(name), b=w, c=comment, d=comment_bold, e=comment_italic))
    print("              {a: <{b}}('{c}', {d}, {e}),".format(a="'{}/string':".format(name), b=w, c=string, d=string_bold, e=string_italic))
    print("              {a: <{b}}('{c}', {d}, {e}),".format(a="'{}/number':".format(name), b=w, c=number, d=number_bold, e=number_italic))
    print("              {a: <{b}}('{c}', {d}, {e}),".format(a="'{}/instance':".format(name), b=w, c=instance, d=instance_bold, e=instance_italic))
    
for error in errors:
    print(error, file=stderr)
if errors:
    exit(1)
