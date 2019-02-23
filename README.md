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
* apply to confessions dataset 

```python
#In utils.py implement this functions

def inter_measures(): # 5°С, $5, -5, +5   #(DavPapikyan)
def double_measures(): # 5կմ/ժ, 5մ/վ       #(DavQaramyan)
def single_measures(): # 5կմ, 5մ           #(DavPapikyan)

def time(): # 5:23 #(DavQaramyan)
def date(): # 10.16.2000 10/16/2000 10,16,2000 #(DavPapikyan)
def float_numbers(without_first=False): # 2.5 2,5 2/3  #(DavQaramyan)
def float_numbers(without_first=True): # .5 ,0.8 #(DavQaramyan)

def postfix_1(): # 2-3-րդ   #(DavPapikyan)
def postfix_2(): #Դ-30      #(DavPapikyan)
def postfix_3(): #1-ին , 5-ական  #(DavPapikyan)

def email(): # davitkar98@gmail.com #(DavQaramyan)
def urls(): # news.am or www.news.am or https://www.aca.am #(DavPapikyan)
def hashtags(): # @nickname , #hashtag #(DavQaramyan)

def special_names(): #Սայաթ-Նովա ... need vocab #(DavQaramyan)
def abbrivations(): # INC. #(DavQaramyan)

def english_word(): #name #(DavPapikyan)
def armenian_word(): #անուն #(DavQaramyan)
def arm_postfix_word(): #ՀՀԿ-ական #(DavPapikyan)
def arm_non_linear_word(): #հեյ~(հե~յ) #(DavQaramyan)
def russian_word(): #имя #(DavPapikyan)
def dots(): # .... ... #(DavQaramyan)

def all_linear_puncts(): # : , ?  #(DavPapikyan)
def all_non_linear_puncts(): # 'apostrophe', 'shesht','bacakanchakan', 'harcakan' #(DavQaramyan)


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

