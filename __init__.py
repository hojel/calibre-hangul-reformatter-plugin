#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import, print_function)

__license__ = 'GPL v3'
__copyright__ = '2013, Hojel<hojelei@gmail.com>'
__docformat__ = 'restructuredtext ko'

import os
from calibre.ebooks.chardet import force_encoding
from calibre.customize import FileTypePlugin
from calibre_plugins.htxtreformat.config import prefs

class hTxtReformat(FileTypePlugin):

    name                = 'Hangul Text Reformat' # Name of the plugin
    description         = 'Reformat ugly Hangul text and get pretty one'
    supported_platforms = ['windows', 'osx', 'linux'] # Platforms this plugin will run on
    author              = 'hojel' # The author of this plugin
    version             = (1, 1, 1)   # The version number of this plugin
    file_types          = set(['txt']) # The file types that this plugin will be applied to
    #on_import          = True # not working
    on_preprocess       = True # Run this plugin before text import
    priority            = 100
    minimum_calibre_version = (2, 0, 0)

    def run(self, path_to_ebook):
        print("reformatter: "+path_to_ebook)
        f = open(path_to_ebook, 'r')
        raw = f.read()
        encoding = force_encoding(raw, True)
        print("Detected encoding: ", encoding)
        txt = unicode(raw, encoding, errors='replace')
        # reformat
        if prefs['reformat']:
            print("reformatting...")
            from ptxt2ftxt import ptxt2ftxt, ftxtclean
            from ftxt2markdown import ftxt2markdown
            txt = ptxt2ftxt(txt, pretty_quote=prefs['pretty_quote'])
            txt = ftxtclean(txt, pretty_quote=prefs['pretty_quote'], correct_word_break=prefs['correct_word_break'])
            txt = ftxt2markdown(txt, guessChapter=prefs['guess_chapter'], guessParaSep=prefs['insert_empty_paragraph'])
        # save as temporary file
        tempfile = self.temporary_file('.txt')
        tempfile.write( txt.encode('utf-8') )
        tempfile.close()
        print("save as ", tempfile.name)
        return tempfile.name

    def is_customizable(self):
        return True
    def config_widget(self):
        from calibre_plugins.htxtreformat.config import ConfigWidget
        return ConfigWidget()
    def save_settings(self, config_widget):
        config_widget.save_settings()
