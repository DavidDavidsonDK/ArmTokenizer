import re
from punct import Punct

def inter_measures(): 
    measures = Punct.inter()
    measures = '\\'+ measures[:4] + '\\' + measures[4:13] + '\\' + measures[13:]
    return r'{}'.format(measures)

def single_measures(): 
    measures = Punct.metric(double=False)
    return r'{}'.format(measures)

def date(): 
    # dd mm yyyy
    return r'(?:^|\s)(\d{1,2}(?:\.|/|,){1}\d{1,2}(?:\.|/|,){1}\d{4})(?:$|\s)'

def postfix_1(): 
    dash = Punct('gtcik').regex() + '|-'
    return r'{}'.format('(?:^|\s)\d+(?:' + dash + ')\d+(?:' + dash + ')?(?:[ա-ֆԱ-Ֆևև]+)?(?:$|\s)')

def postfix_2(): 
    dash = Punct('gtcik').regex() + '|-'
    return r'{}'.format('(?:^|\s)[ա-ֆԱ-Ֆևa-z](?:' + dash + ')\d+(?:$|\s)')

def postfix_3(): 
    dash = Punct('gtcik').regex() + '|-'
    return r'{}'.format('(?:^|\s)\d+(?:' + dash + ')[ա-ֆԱ-Ֆև]+(?:$|\s)')

def urls(): 
    return r'{}'.format('(?:^|\s)(https?:\/\/(?:www\.)?[\w@\.\?%&-_\/\+:=!]+\.(?:[a-zA-Z]+){2,}|(?:www\.)[\w@\.\?%&-_\/\+:=!]+\.(?:[a-zA-Z]+){2,}|[\w@\.\?%&-_\/\+:=!]+\.(?:[a-zA-Z]+){2,})(?:$|\s)')

def english_word():
    dash = (Punct('gtcik').regex() + '|-').replace('|','')
    return r'{}'.format('(?:^|\s)([a-zA-Z' + dash + ']+)(?:$|\s)')

def arm_postfix_word(): 
    dash = (Punct('gtcik').regex() + '|-').replace('|','')
    return '{}'.format('(?:^|\s)([ա-ֆԱ-Ֆև]+[' + dash + '][ա-ֆԱ-Ֆև]+)(?:$|\s)')

def russian_word(): 
    dash = (Punct('gtcik').regex() + '|-').replace('|','')
    return r'{}'.format('(?:^|\s)([а-яА-ЯЁё' + dash + ']+)(?:$|\s)')               

def all_linear_puncts(): 
    return r'{}'.format('(?:^|\s)([' + Punct.all() + ']{1})(?:$|\s)')
