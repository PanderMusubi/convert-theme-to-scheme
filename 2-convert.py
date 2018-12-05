#!/usr/bin/env python3

from xml.etree import ElementTree
from glob import glob
from sys import stderr

print("[color_schemes]")
names = []
for filename in sorted(glob('eclipse-color-theme-master/com.github.eclipsecolortheme/themes/*.xml')):
    root = ElementTree.parse(filename).getroot()
    names.append(root.attrib['name'].lower().replace(' ', '/'))
print("names = ['{}']".format("', '".join(names)))
print("selected = {}".format(names[0]))
    
errors = []
for filename in sorted(glob('eclipse-color-theme-master/com.github.eclipsecolortheme/themes/*.xml')):
    root = ElementTree.parse(filename).getroot()
    fullname = root.attrib['name']
    name = fullname.lower().replace(' ', '/')

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

    print("{}/name = {}".format(name, fullname))
    print("{}/background = {}".format(name, background))
    print("{}/currentline = {}".format(name, currentline))
    print("{}/occurence = {}".format(name, occurence))
    print("{}/ctrlclick = {}".format(name, ctrlclick))
    print("{}/sideareas = {}".format(name, sideareas))
    print("{}/matched_p = {}".format(name, matched_p))
    print("{}/unmatched_p = {}".format(name, unmatched_p))
    
    print("{}/normal = ('{}', {}, {})".format(name, normal, normal_bold, normal_italic))
    print("{}/keyword = ('{}', {}, {})".format(name, keyword, keyword_bold, keyword_italic))
    print("{}/builtin = ('{}', {}, {})".format(name, builtin, builtin_bold, builtin_italic))
    print("{}/definition = ('{}', {}, {})".format(name, definition, definition_bold, definition_italic))
    print("{}/comment = ('{}', {}, {})".format(name, comment, comment_bold, comment_italic))
    print("{}/string = ('{}', {}, {})".format(name, string, string_bold, string_italic))
    print("{}/number = ('{}', {}, {})".format(name, number, number_bold, number_italic))
    print("{}/instance = ('{}', {}, {})".format(name, instance, instance_bold, instance_italic))
    
for error in errors:
    print(error, file=stderr)
if errors:
    exit(1)
