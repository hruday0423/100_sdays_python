import random
from itertools import filterfalse

from cloudinit.sources.DataSourceMAAS import check_seed_contents
from rich.jupyter import display

word_list =['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop'
 'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power',
 'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism',
 'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider',
 'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language', 'else'
 'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus',
 'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful',
 'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard',
 'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser',
 'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen',
 'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
 'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
 'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph',
 'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'flower'
 'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete', 'wind'
 'brain', 'control', 'prophet', 'freedom', 'harbour', 'confidence', 'positive',
 'harvest', 'hunger', 'woman', 'children', 'stranger', 'garden', 'pleasure',
 'between', 'recognition', 'tomorrow', 'autumn', 'monkey', 'spring', 'winter',
 'classification', 'typewriter', 'success', 'difference', 'acoustics', 'astronomy'
 'agreement', 'sorrow', 'christmas', 'silver', 'birthday', 'championship', 'friend'
 'comfortable', 'diffusion', 'murder', 'policeman', 'science', 'desert', 'basketball'
 'blood', 'funeral', 'silence', 'garment', 'merchant', 'spirit', 'punishment',
 'measurement', 'ocean', 'digital', 'illusion', 'tyrant', 'castle', 'passion',
 'magician', 'remedy', 'knowledge', 'threshold', 'number', 'vision', 'expectation'
 'absence', 'mystery', 'morning', 'device', 'thoughts', 'spirit', 'future',
 'mountain', 'treasure', 'machine', 'whispering', 'eternity', 'reflection',
 'achievement', 'lightning', 'secret', 'environment', 'shepherd', 'confusion',
 'grave', 'promise', 'honour', 'reward', 'temple', 'distance', 'eagle', 'saturn',
 'finger', 'belief', 'crystal', 'fashion', 'direction', 'captain', 'moment', 'important'
 'permission', 'logic', 'analysis', 'password', 'english', 'equalizer', 'simulation'
 'emotion', 'battle', 'expression', 'scissors', 'trousers', 'glasses', 'department'
 'dictionary', 'chemistry', 'induction', 'detail', 'widow', 'wealth', 'health',
 'disaster', 'volcano', 'poverty', 'limitation', 'perfect', 'intelligence', 'infinity'
 'failure', 'ignorance', 'destination', 'source', 'resort', 'satisfaction', 'exam'
 'frequency', 'selection', 'substitution', 'kingdom', 'pattern', 'management',
 'situation', 'multiply', 'treatment', 'dollar', 'intuition', 'chapter', 'magnet'
 'desire', 'command', 'action', 'consciousness', 'enemy', 'security', 'object',
 'happen', 'happiness', 'worry', 'method', 'tolerance', 'error', 'hesitation',
 'record', 'tongue', 'supply', 'vibration', 'stress', 'despair', 'restaurant',
 'television', 'video', 'audio', 'layer', 'mixture', 'doorbell', 'cousin', 'beard'
 'finance', 'production', 'invisible', 'excitement', 'afternoon', 'office', 'alpha'
 'illustration', 'valley', 'apartment', 'necessary', 'shortage', 'almost', 'furnish'
 'blanket', 'suggestion', 'overflow', 'demonstration', 'challenge', 'compact',
 'tower', 'question', 'problem', 'pressure', 'beast', 'encouragement', 'afraid',
 'cavity', 'appearance', 'wonderful', 'matter', 'dimension', 'business', 'doubt',
 'conversation', 'reaction', 'psychology', 'superstition', 'smash', 'horseshoe',
 'surprise', 'nothing', 'ladder', 'opposite', 'reality', 'genius', 'string',
 'destruction', 'expensive', 'painting', 'chicken', 'wishing', 'profession',
 'hatred', 'possession', 'criticism', 'zebra', 'harmony', 'personality', 'overcome'
 'addition', 'subtraction', 'cipher', 'encryption', 'compression', 'extension',
 'blessing', 'meeting', 'difficulty', 'weapon', 'against', 'external', 'internal'
 'legend', 'servant', 'secondary', 'license', 'directory', 'statistics', 'generate'
 'attraction', 'sensitivity', 'magnification', 'someone', 'symptom', 'recipe',
 'service', 'family', 'island', 'planet', 'butterfly', 'diving', 'strength',
 'extreme', 'opportunity', 'illumination', 'cable', 'conflict', 'interference',
 'receiver', 'transmitter', 'channel', 'company', 'grocery', 'devil', 'angel',
 'exactly', 'document', 'tutorial', 'sound', 'voice', 'abbreviation', 'abdomen',
 'abrupt', 'absolute', 'absorption', 'abstract', 'academy', 'acceleration',
 'accident', 'account', 'acidification', 'actress', 'adaptation', 'addiction', 'a'
 'adjustment', 'admiration', 'adoption', 'advanced', 'adventure', 'advertisement'
 'agenda', 'airport', 'algorithm', 'allocation', 'aluminium', 'ambiguity', 'ambit'
 'amphibian', 'anaesthesia', 'analogy', 'anchor', 'animation', 'anode', 'cathode'
 'apparent', 'appendix', 'approval', 'approximation', 'arbitrary', 'architecture'
 'arithmetic', 'arrangement', 'article', 'ascending', 'ashamed', 'asleep',
 'assembly', 'astonishment', 'atmosphere', 'awful', 'bachelor', 'backbone', 'back'
 'bacteria', 'balance', 'balloon', 'banana', 'barbecue', 'baseball', 'beaker',
 'beggar', 'behaviour', 'benefit', 'bidirectional', 'biology', 'blackboard', 'black'
 'bladder', 'bleeding', 'blender', 'bonus', 'bottle', 'bracket', 'branch', 'brill'
 'bubble', 'bucket', 'budget', 'bullet', 'burglar', 'butcher', 'bypass',
 'calculator', 'calibration', 'campaign', 'cancellation', 'candidate', 'candle',
 'carpenter', 'carriage', 'cartoon', 'cascade', 'casual', 'catalyst', 'category',
 'cement', 'ceremony', 'chairman', 'checkout', 'chimney', 'chocolate', 'cigarette'
 'circumference', 'civilization', 'classroom', 'clearance', 'client', 'coconut',
 'coincidence', 'colleague', 'comfortable', 'competition', 'kangaroo', 'kidnap',
 'journal', 'jockey', 'iteration', 'isometric', 'isolation', 'invitation', 'inter'
 'institution', 'injection', 'humanity', 'housekeeper', 'history', 'heaven', 'gui'
 'greenhouse', 'glory', 'foundation', 'formula', 'fluctuation', 'fiction', 'extra'
 'emission', 'elasticity', 'earthquake', 'dynamic', 'doctorate', 'divorce',]

hangman =[ r"""
   +--+
   |  |
   O  |
  /|\ |
  / \ |
      |
 =====""", r"""
   +--+
   |  |
   O  |
  /|\ |
  /   |
      |
  =====""",  r"""
   +--+
   |  |
   O  |
  /|\ |
      |
      |
  =====""",  r"""
   +--+
   |  |
   O  |
  /|  |
      |
      |
  =====""",  r"""
   +--+
   |  |
   O  |
   |  |
      |
      |
  =====""",  r"""
   +--+
   |  |
   O  |
      |
      |
      |
  =====""",r"""
   +--+
   |  |
      |
      |
      |
      |
  ====="""
           ]
chosen_word= random.choice(word_list)
print(chosen_word)
lives =6
list=[]
game_over= False
while not game_over:
    guess = input('guess the letter of word:').lower()
    print(guess)
    placeholder = ""
    display=''
    for letter in chosen_word:
         placeholder+='_'
         if letter == guess:
              list.append(letter)
              display+=letter
         elif letter in list:
              display+=letter
         else:
              display+='-'
    if guess not in chosen_word:
        lives-=1
        print('wrong guess you lost a life')
        if lives==0:
            game_over= True
            print('game over,you loose')

    if chosen_word == display:
         game_over = True
    print(display)
    print(hangman[lives])










