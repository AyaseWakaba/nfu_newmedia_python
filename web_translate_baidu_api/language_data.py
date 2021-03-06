# -*- coding: utf-8 -*- 

class language_from_to (object):

    def __init__(self, fn='data\language_data.tsv'):
       import csv
       with open(fn, 'r', encoding='utf8') as csvfile:
           reader = csv.DictReader(csvfile, fieldnames=['language_from', 'language_to'], delimiter='\t')
           fieldnames = reader.fieldnames

           list_dict_language = []
           for row in reader:
                  list_dict_language.append(dict(row))

           self.from_to = {d['language_from']:d['language_to'] for d in list_dict_language}

    def country_name(self, language_from=''):
        language_to =  self.from_to.get(language_from, None)
        return (language_to)