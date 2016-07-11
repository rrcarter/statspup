#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, nltk.data, string
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

#------------------------------------
# Word Replacements
# Inspired by kittify.herokuapp.com
#------------------------------------
replacements = {'forever':'fur-ever', 'awesome':'pawsome','somebody':'somepawdy',
            'rough':'ruff', 'doppleganger':'doggleganger', 'nuts':'mutts',
            'dark':'bark', 'tone':'bone', 'call':'collie', 'catch':'fetch',
            'goodness':'pugness', 'observations':'pawservations',
            '%':'furrcent', 'thank':'belly scratchies', 'thanks':'belly scratchies',
             'good':'grrreat', 'great':'better than steak', 'network':'barkwork',
             'networks':'barkworks', 'fantastic':'dogtastic', 'no':'BARKBARKBARK no',
             'yes':'RUFFRUFF yes', 'retrieve':'retriever', 'model':'woof-el',
             'models':'woof-els', 'neural':'awoo-al', 'regression':'regrrrrrshun',
             'kernel':'kennel', 'learning':'herding', 'computer':'noisemaker',
             'outputs':'treats', 'output':'treat', 'algorithm': 'algrrrrrrrithym',
             'distribution':'distripooshun', 'classes':'types of bones',
             'learner':'foodgiver', 'clustering':'sheepherding'}
#------------------------------------
# Replace Words
# Code care of inspectorG4dget from stackoverflow
#------------------------------------
with open('raw_statspupsays.txt') as infile, open('statspupsays.txt', 'w') as outfile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        outfile.write(line)

#------------------------------------
# Now Chunk the replacement text
#------------------------------------
# @robincamille
# Split up a text into tweetable chunks. This script
# puts sentences from source text into a TXT file where each sentence
# in a new line.

filename = open('statspupsays.txt','r') #
f = filename.read()
filename.close()

w = open('statspup_chunks.txt','w')

fsent = sent_detector.tokenize(f.strip())

for sent in fsent:
    if len(sent) <= 140:
        w.write(sent)
        w.write("\n")
    elif len(sent) > 141:
        w.write("SPLIT ")
        w.write(sent)
        w.write("/n")
    else:
        pass

print "DONESIES"

w.close()
# If any sentence is over 140 chars, the script marks it as SPLIT.
# This needs to be done manually, but it can be done easily with EMACS
