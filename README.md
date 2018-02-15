# WordSearch
## A Word Search Generator for python.
------------------------------------------------------------------------------------------------------------------------------
## How to use the ***Word Search Genarator***
------------------------------------------------------------------------------------------------------------------------------
#### How to import the ***the word search Generator***

```
from WordSearch import WordSearch
```
### How to initialize the WordSearch Object
```
# words = a variable with all the words, which are all seperated by a comma.
# Note : the variable which contains all words mustn't be called words.
words = ("Hello,Blah,Sperhero")
x = 40
x = 40
# x & y indicate the size of the word search.
# Note: When you take a look at our code, you will see 'grid' (a list).
#Grid is a a list which contains lists(columns) which contain letters (strings). 
w = WordSearch(words,x,y)
```
## What can a Word search object do?
------------------------------------------------------------------------------------------------------------------------------
### Methods
> ``` WordSearch.letter(row, column) ```
 Discription: it returns a letter (string) in the defined parameters
 ### Propeties
 > ```WordSearch.Grid``` 
 Discription: It is the WordSearch Grid where all letters are stored.
 > ```WordSearch.maxX```
 Discription: The "x" value you defined at the start of generating the object.
 > ``` WordSearch.maxY
 Discription: The "y" value you defined at the start of generating the object.
 
