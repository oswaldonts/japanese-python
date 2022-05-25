verbs = [
  {
    'verb': '飲む',
    'stem': '飲',
    'suffix': 'む',
    'type': '五段',
  },
  {
    'verb': '食べる',
    'stem': '食べ',
    'suffix': '',
    'type': '一段',
  },
  {
    'verb': '帰える',
    'stem': '帰え',
    'suffix': 'る',
    'type': '五段',
  },
  {
    'verb': '死ぬ',
    'stem': '死',
    'suffix': 'ぬ',
    'type': '五段',
  },
  {
    'verb': '乗る',
    'stem': '乗',
    'suffix': 'る',
    'type': '五段',
  },
  # {
  #   'verb': 'する',
  #   'stem': 'し',
  #   'suffix': '',
  #   'type': '不規則',
  # },
  # {
  #   'verb': '来る',
  #   'stem': '来',
  #   'suffix': '',
  #   'type': '不規則',
  # },
]


def inflection(verb, inflection_type):
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
      'う': 'あ',
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
  
  inflected = suffix_inflection[inflection_type][verb['suffix']]

  def form(*args, **kwargs):
    form = args[0]
    stem = verb['stem']
    suffix = verb['suffix']
    
    if verb['type'] == '五段':
      stem = stem + inflected

    if inflection_type == 't' and (suffix == 'ぬ' or suffix == 'む'):
      if form == 'て':
        form = 'で'
      elif form == 'た':
        form = 'だ'

    return stem + form

  return form


def sentence():
  pass
  subject = '私'
  object = 'プログラマー'


def run():
  for verb in verbs:
    form = inflection(verb, 'i')
    masu_form = form('ます')
    masen_form = form('ません')

    form = inflection(verb, 'a')
    nai_form = form('ない')

    form = inflection(verb, 't')
    te_form = form('て')
    ta_form = form('た')
    
    print(f'{masu_form}\t{masen_form}\t{nai_form}\t{te_form}\t{ta_form}')


if __name__ == '__main__':
  run()
