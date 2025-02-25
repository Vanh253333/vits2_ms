# from .symbols import symbols
# from . import cleaners
# import re

from viphoneme import syms, vi2IPA_split, vi2IPA

symbols = syms

_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}



def sequence_to_text(sequence):
    
    result = ''
    for symbol_id in sequence:
        if symbol_id in _id_to_symbol:
            result += _id_to_symbol[symbol_id]     
    return result

def text_to_sequence(text):

    '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
        Args:
        text: string to convert to a sequence
        cleaner_names: names of the cleaner functions to run the text through
        Returns:
        List of integers corresponding to the symbols in the text
    '''
    sequence = []
    text = text.replace('\s+',' ').lower()
    phon = vi2IPA_split(text,"/")
    phon = phon.split("/")[1:]
    eol = -1
    for i,p in reversed(list(enumerate(phon))):
        if p not in ["..",""," ",".","  "]:
            eol = i
            break

    phones = phon[:eol+1]+[" ","."]
    # print(phones)
    phones_id =[]
    for i in phones:
        if i in _symbol_to_id:
            phones_id.append(_symbol_to_id[i])
            #phones_id = [_symbol_to_id[i] for i in phones]
    sequence.extend(phones_id)  

    return sequence


def cleaned_text_to_sequence(cleaned_text):
    '''Converts a string of phonems_split with / to a sequence of IDs corresponding to the symbols in the text.
        Args:
        text: string of phonems_split to convert to a sequence
        cleaner_names: names of the cleaner functions to run the text through
        Returns:
        List of integers corresponding to the symbols in the text
    '''
    sequence = []
    phon = vi2IPA_split(cleaned_text,"/")
    phon = phon.split("/")[1:]
    eol = -1
    for i,p in reversed(list(enumerate(phon))):
        if p not in ["..",""," ",".","  "]:
            eol = i
            break

    phones = phon[:eol+1]+[" ","."]
    phones_id =[]
    for i in phones:
        if i in _symbol_to_id:
            phones_id.append(_symbol_to_id[i])
            #phones_id = [_symbol_to_id[i] for i in phones]
    sequence.extend(phones_id)

    return sequence

def _clean_text(text):
    text = text.replace('\s+',' ').lower()    
    phon = vi2IPA(text)
    # print(phon)
    eol = -1
    for i,p in reversed(list(enumerate(phon))):
        if p not in ["..",""," ",".","  "]:
            eol = i
            break
    phones = phon[:eol+1]+" ."
    return phones
