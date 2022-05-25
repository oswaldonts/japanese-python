import math
from random import random

from subjects import subjects
from objects import objects
from verbs import verbs
from forms import forms

def irregular_verb(verb_dict):
  if verb_dict['verb'] == 'する':
    pass
  return 0


def conjugation(verb_dict, form_dict):
  suffix_inflection = {
    'i': {
      'う': 'い',
      'く': 'き',
      'す': 'し',
      'つ': 'ち',
      'ぬ': 'に',
      'む': 'み',
      'る': 'り',
      '': '',
    },
    'a': {
      'う': 'わ',
      'く': 'か',
      'す': 'さ',
      'つ': 'た',
      'ぬ': 'な',
      'む': 'ま',
      'る': 'ら',
      '': '',
    },
    't': {
      'う': 'っ',
      'く': 'い',
      'す': 'し',
      'つ': 'っ',
      'ぬ': 'ん',
      'む': 'ん',
      'る': 'っ',
      '': '',
    }
  }

  stem = verb_dict['stem']
  suffix = verb_dict['suffix']
  inflection = form_dict['inflection']
  form = form_dict['form']

  if form == 'る':
    return verb_dict['verb']

  inflected = suffix_inflection[inflection][suffix]
  
  if verb_dict['type'] == '五段':
    stem = stem + inflected

  if inflection == 't' and (suffix == 'ぬ' or suffix == 'む'):
    if form == 'て':
      form = 'で'
    elif form == 'た':
      form = 'だ'

  return stem + form


def sentence():
  subject_dict = subjects[math.floor(random() * len(subjects))]

  particle_subject = subject_dict['particles'][math.floor(random() * len(subject_dict['particles']))]
  
  verb_dict = verbs[math.floor(random() * len(verbs))]
  
  particle_verb = verb_dict['particles'][math.floor(random() * len(verb_dict['particles']))]
  
  objects_dict = []

  for object in objects:
    for use in object['uses']:
      if particle_verb in use['particles'] and verb_dict['verb'] == use['verb']:
        objects_dict.append(object)

  object_dict = objects_dict[math.floor(random() * len(objects_dict))]
  
  form_dict = forms[math.floor(random() * len(forms))]

  if form_dict['form'] == 'ましょう':
    subject_dict['subject'] = '一緒に'
    particle_subject = ''

  print(subject_dict['subject'] + particle_subject + object_dict['object'] + particle_verb + conjugation(verb_dict, form_dict))


def run():
  for i in range(0,10):
    sentence()
  # for verb in verbs:
  #   masu_form = form(verb, 'i', '')
  #   masen_form = form(verb, 'i', '')
  #   masen_form = form(verb, 'i', '')

  #   mashita_form = form(verb, 'i', '')
  #   masendeshita_form = form(verb, 'i', '')
  #   mashou_form = form(verb, 'i', '')

  #   nai_form = form(verb, 'a', '')

  #   te_form = form(verb, 't', '')
  #   ta_form = form(verb, 't', '')

  #   plain_form = form(verb, '', '')
    
  #   print(f'{masu_form}\t{masen_form}\t{mashita_form}\t{masendeshita_form}\t{mashou_form}\t{nai_form}\t{te_form}\t{ta_form}\t{plain_form}')


if __name__ == '__main__':
  run()

