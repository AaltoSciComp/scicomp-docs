# Convert Confluence xml to pseudo-HTML
#
# This is the first step in converting confluence to proper resturctured text.
# It takes an entities.xml file that comes from a confluence XML export, reads
# through and discovers all of the different pages, then writes them out in
# 'source/*.html.  These HTML can be converted to ReStructured Text using
# pandoc (see the Makefile).  The end purpose is to convert a confluence wiki
# to Sphinx ReStructured Text projcet project.
#
# There are quite a few hacks here.  The confluence export isn't really HTML,
# so we have to do some regex hacks to convert it to something that is usuable
# by pandoc.  Before that, though, we have to process all the XML to find the
# pages and proper names.
#
# Usage:
#   mkdir source rst html
#   python3 confuence2html.py entities.xml  # Puts converted files in source
#   make -f allrst                          # converts html to rst
#   make -f allhtml                         # converts rst to html.  For testing
#                                           # to see how good conversion is, but
#                                           # not to be used for anything
#
# Things may go wrong at any point, this is not very well tested!  You have to
# manually copy over the .rst files into the structure you want.  There is no
# automatic linking or putting stuff into the Sphinx tree.

# Richard Darst, 2017.  MIT license


import re
import sys
import xml
import xml.etree.ElementTree

input = open(sys.argv[1]).read()
data = xml.etree.ElementTree.fromstring(input)

def findpage(id_):
    return data.find("*[id='%s']"%id_).find("property[@name='body']").text
    #for page in data.findall("*[@class='BodyContent']"):
    #    if int(page.find('id').text) != int(id):
    #        continue
    #    return page.find("property[@name='body']").text

pages = { }
for object in data:
    cls = object.attrib['class']
    if cls != 'Page':
        #print cls.attrib
        continue

    title = object.find("*[@name='title']").text
    version = int(object.find("property[@name='version']").text)
    page_id = object.find(".property[@class='Page']")
    if page_id:
        page_id = page_id.find('id').text
    #if page_id is not None and int(page_id) in {113905759, None} or page_id is None:
    #    continue
    #print(title, version, page_id)

    if title in pages:
        if version > int(pages[title].find("property[@name='version']").text):
            pages[title] = object
    else:
        pages[title] = object

for title, object in pages.items():
    print(title, int(object.find("property[@name='version']").text))

    body_id = object.findall(".//element[@class='BodyContent']")[0].find('id').text
    body = findpage(body_id)
    open('source/orig.%s'%(title.replace('/','').replace('(','').replace(')','').replace(' ','_')).replace('.',''), 'w').write(body)

    # Includes
    # <ac:structured-macro ac:name="excerpt-include"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><a href="Hardware Distribution">Hardware Distribution</a>
    #body = re.sub(r'<ac:structured-macro[^>]*?name="excerpt-include".*?content-title="([^"]*?)"[^>]*?></ac:structured-macro>', r'\n\n_.. include:: \1\n\n', body, flags=re.M|re.S)


    # <ac:link><ri:page ri:content-title="Getting help" /><ac:plain-text-link-body><pre>contact admins</pre></ac:plain-text-link-body></ac:link>
    #body = re.sub(r'<ac:link><ri:page ri:content-title="(.*?)".?/>.*?<pre>(.*?)</pre></ac:plain-text-link-body></ac:link>', r'<a href="\1">\2</a>', body, flags=re.M|re.S)
    # r <ac:link><ri:page ri:content-title="Getting help" /><ac:plain-text-link-body><![CDATA[local Triton support team member]]></ac:plain-text-link-body></ac:link> and w
    def m(m):
        x = '<a href="%s">%s</a>'
        print(m.group(1), m.group(2), m.group(3))
        if m.group(3): return x%(m.group(1), m.group(3))
        return x%(m.group(1), m.group(1))
    #body = re.sub(r'<ac:link>.*?ri:content-title="(.*?)".*?(CDATA\[|<pre>|>|)(.*?)(]]|</pre>_).*?</ac:link>', m, body, flags=re.M|re.S)
    #body = re.sub(r'<ac:link>.*?ri:content-title="([^"]*?)".*?<pre>([^<]*?)</pre>.*?</ac:link>', r'<a href="LINK/\1">\2</a>', body, flags=re.M|re.S)
    #body = re.sub(r'<ac:link>.*?ri:content-title="([^"]*?)".*?CDATA\[([^]]*?)]].*?</ac:link>', r'<a href="LINK/\1">\2</a>', body, flags=re.M|re.S)
    #body = re.sub(r'<ac:link>.*?ri:content-title="([^"]*?)".?/></ac:link>', r'<a href="LINK/\1">\1</a>', body, flags=re.M|re.S)

    def m(m):
        t = m.group(0)
        t = re.sub(r'<ac:link>.*?ri:content-title="([^"]*?)".*?<pre>([^<]*?)</pre>.*?</ac:link>', r'<a href="LINK/\1">\2</a>', t, flags=re.M|re.S)
        t = re.sub(r'<ac:link>.*?ri:content-title="([^"]*?)".*?CDATA\[([^]]*?)]].*?</ac:link>', r'<a href="LINK/\1">\2</a>', t, flags=re.M|re.S)
        t = re.sub(r'<ac:link>.*?ri:content-title="([^"]*?)".?/></ac:link>', r'<a href="LINK/\1">\1</a>', t, flags=re.M|re.S)
        return t
    body = re.sub(r'<ac:link>.*?</ac:link>', m, body, flags=re.M|re.S)

    body = re.sub(r'<!\[CDATA\[(.*?)]] >', r'<pre>\1</pre>', body, flags=re.M|re.S)
    body = re.sub(r'&nbsp;', r' ', body, flags=re.M|re.S)



    open('source/%s.html'%(title.replace('/','').replace('(','').replace(')','').replace(' ','_')).replace('.',''), 'w').write(body)
    #print(body)
