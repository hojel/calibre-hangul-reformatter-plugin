#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from PyQt5.Qt import QWidget, QHBoxLayout, QVBoxLayout, QCheckBox, QLabel, QComboBox

from calibre.utils.config import JSONConfig

# This is where all preferences for this plugin will be stored
# Remember that this name (i.e. plugins/htxtreformat) is also
# in a global namespace, so make it as unique as possible.
# You should always prefix your config file name with plugins/,
# so as to ensure you dont accidentally clobber a calibre config file
prefs = JSONConfig('plugins/htxtreformat')

# Set defaults
prefs.defaults['reformat'] = True
prefs.defaults['pretty_line'] = True
prefs.defaults['pretty_quote'] = True
prefs.defaults['correct_word_break'] = 'None'
prefs.defaults['guess_chapter'] = True
prefs.defaults['insert_empty_paragraph'] = True

class ConfigWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.l = QVBoxLayout()
        self.setLayout(self.l)

        self.cbox1 = QCheckBox('Reformatting')
        self.cbox1.setChecked(prefs['reformat'])
        self.l.addWidget(self.cbox1)

        self.cbox2 = QCheckBox('Line break by Special char')
        self.cbox2.setChecked(prefs['pretty_line'])
        self.l.addWidget(self.cbox2)

        self.cbox2 = QCheckBox('Pretty Quote char')
        self.cbox2.setChecked(prefs['pretty_quote'])
        self.l.addWidget(self.cbox2)

        self.cbox3 = QCheckBox('Guess Chapter')
        self.cbox3.setChecked(prefs['guess_chapter'])
        self.l.addWidget(self.cbox3)

        self.cbox4 = QCheckBox('Allow Empty Paragraph')
        self.cbox4.setChecked(prefs['insert_empty_paragraph'])
        self.l.addWidget(self.cbox4)

        cl = QHBoxLayout()
        cl.addWidget(QLabel('Broken Word over lines'))
        self.combo1 = QComboBox()
        wbrk_list = ['None', 'Pattern', 'Naver']
        self.combo1.addItems(wbrk_list)
        self.combo1.setCurrentIndex(wbrk_list.index(prefs['correct_word_break']))
        cl.addWidget(self.combo1)
        self.l.addLayout(cl)

    def save_settings(self):
        prefs['reformat'] = self.cbox1.isChecked()
        prefs['pretty_quote'] = self.cbox2.isChecked()
        prefs['guess_chapter'] = self.cbox3.isChecked()
        prefs['insert_empty_paragraph'] = self.cbox4.isChecked()
        prefs['correct_word_break'] = str(self.combo1.currentText())
