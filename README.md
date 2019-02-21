# ArmTokenizer
Tokenizer for Armenian Language

## Usage
```python
#import Tokenizer
>>> from tokenizer import Tokenizer
>>> line = "Խուզարկությամբ հայտնաբերվեց տնկված 208 հատ, մինչ 4մ բարձրության կանեփի թուփ:"
>>> tokenizer = Tokenizer()
>>> tokenizer.tokenize(line)
>>> tokenizer.tokens()

['Խուզարկությամբ', 'հայտնաբերվեց', 'տնկված', '208', 'հատ', ',', 'մինչ', '4', 'մ', 'բարձրության', 'կանեփի', 'թուփ', ':']

```
See  https://github.com/gorarakelyan/Hy-Tokenizer for more information


## Task (Regex)
* need to implement small functions for finding patterns
* need to implement testing functions to validate regexs
* need to parallelize tasks and at the end merge branches

```python
#In utils.py implement this functions

def inter_measures(): # 5°С, $5, -5, +5
def double_measures(): # 5կմ/ժ, 5մ/վ
def single_measures(): # 5կմ, 5մ

def time(): # 5:23
def date(): # 10.16.2000 10/16/2000 10,16,2000
def float_numbers(without_first=False): # 2.5 2,5 2/3
def float_numbers(without_first=True): # .5 ,0.8

def postfix_1(): # 2-3-րդ
def postfix_2(): #Դ-30
def postfix_3(): #1-ին , 5-ական

def email(): # davitkar98@gmail.com
def urls(): # news.am or www.news.am or https://www.aca.am
def hashtags(): # @nickname , #hashtag

def special_names(): #Սայաթ-Նովա ... need vocab
def abbrivations(): # INC.

def english_word(): #name
def armenian_word(): #անուն
def arm_postfix_word(): #ՀՀԿ-ական
def arm_non_linear_word(): #հեյ~(հե~յ)
def russian_word(): #имя
def dots(): # .... ...

def all_linear_puncts(): # : , ?
def all_non_linear_puncts(): # 'apostrophe', 'shesht','bacakanchakan', 'harcakan'


#Hints
#Punct.inter()              <----- '+|-|?|!|%|°С|$|€|₩|¥|₦|₽|£'
#Punct.metric(double=False) <----- 'կմ|մ|սմ|մմ|ժ|վ|ր|մվ|կգ|գ|մգ|տ|ց|ք'
#Punct.metric(double=True)  <----- 'կմ/մ|կմ/սմ|կմ/մմ|կմ/ժ|կմ/վ|կմ/ր|կմ/մվ|կմ/կգ|...'
#Punct.all(linear=True)     <----- ''։|։|:|\\.\\.\\.\\.|\\.\\.\\.|\\.|.|\\.|,|,|,|՝|՝|`|֊|֊|«|«|»|»|...'
#Punct.all(linear=False)    <----- '՚|՚|՛|՛|՜|՜|~|՞|՞'
#
#Punct('gtcik').regex()     <----- '—|—|_'
#also insted of 'gtcik' you can use any of below mentioned keywords,
#Non Linear Punctuations <----> ['apostrophe', 'shesht','bacakanchakan', 'harcakan']
#Linear Punctuations <----> ['verjaket','4bazmaket' ,'3bazmaket','mijaket','storaket','but', 
#                            'hyphen', 'b_chakert','p_chakert','gtcik' ,'aliq', 'quote1',
#                            'quote2','dram', 'b_pakagitc','p_pakagitc', 'b_dzevavor','p_dzevavor',
#                            'b_qarakusi','p_qarakusi', 'slesh']
#
```
