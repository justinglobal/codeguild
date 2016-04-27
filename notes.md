

ideas for final project

shirt factory - design

shirt factory - auto-generate pattern

analysis - examine news article text and make visualization of data….



python class

Day 1

3/16

Download Python

download atom text editor

Terminal - bash

Commands

	•	pwd - ‘print working directory’ shows where you are
	•
	•	ls - shows all folders/files
	•
	•	mkdir - makes directory
	•
	•	cd - change directory
	•
	•	cd .. - goes up one directory
	•
	•	cd ~ - goes to home directory
	•
	•	touch - makes a file

*how to run a python file from a directory in Terminal*

go to the directory with the file

type “Python3 [filename.ext]”

file will run in terminal

storing data

value

data types -
	•
	•	Integer
	•	Float
	•	Strings - python strings are in ‘ ‘

operators

python operators: +, -, *, /,  *see cheat sheet for all operators*


Snake Case

uses underscore or CamelCase

Assignment Statements

can be value or expression using other values/variables

miles = 400

or

miles_driven = day_total + running_total

Order of operations

Need to assign variable before you use it…

> name = ‘David’
> greeting = ‘Hello.’ + name
> [will print ‘Hello David’]

comment character is #

Function
‘call’ a function

ex:
> min(5, 30)

gives minimum of two numbers

Input functions

gets input from user

print()

-prints value as string

input()

-waits for typing on keyboard
gives string

example:

> input(‘Name’)
> name [computer will wait for input]
> [whatever is input will be assigned to the variable ’Name’]

> print(‘What is your name?’)
>name = input()

‘Justin’

[will print that string]
[computer waits for user input]
[user input data will be printed]

Important 4 steps to programming

1. Initialize/Defin

2. Input

3. Transform data

4. Output

boolean operators

True and False

Operators and what they do

examples… > < != ==, etc

combo - assign value and operator at same time

> apples_left = apples_left -1

[subtracts one from value and re-assigns)

**can combine assignment and operator**  check this!!!

> apples_left -= apples_left

will subtract

Casting  - changing data type

> str(5)

changes int to string

print(‘I have ‘ + str(5) + ‘ apples’)
[will print integer (5) as a string]

cast integers to float

> float(5)
5.0

int / int = floating point number

casting does not round, it truncates

Branch

if operator

if [boolean value]:
	block

Blocks and Conditions
define with 4 spaces (or tab)

else - last can be catch all

elif - alternate value

Loops

when to loop: do something 3 times…write one line, then loop to it 3x

while

while [boolean value]:
	[code block] - must update the boolean or program will loop


Standard Library

comes with python…has docs

modules - name for grouping of code

can import modules into other code

example: ‘Random’ module - generates random number

> import random

random.rand int(1, 10) - this will make a random number between 1 and 10

. after ‘random’ is like a possessive…means ‘go inside’

see class projects 3, 4 and 5

more Boolean

boolean operators - not, and, or

Git

Source control - controls source code among many coders
	tracks changes in a *directory*

runs from Terminal command prompt
saves into a special directory called *Repository*

how to ‘run’ Git: type ‘Git’ into Terminal prompt

Features:
	> History - compare versions
	> Merge 2 coder’s work on same portion
	> Multitasking
	> Back everything up

Git stores “Commits”
	> Commit = changes to a directory
	> Commit builds upon each other
	> branch = Label for a ‘commit’

Terms: Directory, Commit, Branch, Repository

*Terminal commands occur in working directory*

*** Make Repository: > git init

startup config:

git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

3 Git concepts

	•	> Wording Directory (WD)
	•
	•	-	 Add a file to WD
	⁃	> git add file [filename.ext]

		Remove file from index
		> git reset file
	•
	•	> Index - staging ground before saved “changes to be committed”
	•
	⁃	- Make added file into ‘commit’
	⁃	> git commit
	•
	•	> HEAD - label always points to most recent

	*NEW STEP*

	git push - pushes history to githup, do all other steps

git add {list files separated by space}
	this adds all the files

git add -A
	this sets up everything in the directory


Check what is happening:

> git status

Compare working directory to Index
> git diff
	- shows changes
	- [>git diff {hash] compares changes - can use first part of long hash number


Compare index to HEAD
> git diff -- cached

Compare WD to HEAD
> git diff HEAD


Commit info
	- timestamp
	- message (tells what is changed in commit)
	- hash (unique ID)

** use [git commit -m ‘describe changes.’]

git log
	- shows info on changes
	- hash numbers, etc

git reset
	- takes everything back to WD

comparing versions, look back

git diff [hash from thing you want to compare to WD]

‘Q’ takes you back to the prompt

**help - to quit: ‘escape’ + ‘:q!’ at prompt


git remote -v lists local push/fetch repos


git branching
	see note ‘gitbranching.md’ from david’s code guild

	branching stays in one repo, forking makes new repo with same history

	use ‘git checkout -b [filename.ext]’

	merge - do in master
		makes a ‘commit’ requires a -m ‘message’

		delete branch after you merge

GitHub

justinglobal
akqj1000

Git Remotes

link local repo to GitHub

“Push” - remote stores local

	“Pull” - remote gets stored local

make github repo first, then clone to local directory:

code: pythonClass admin$ git clone https://github.com/justinglobal/shirt_factory.git


Python functions part 2

> max(a, b) finds max of two numbers

Type-specific functions

	- lives inside type

	like modules
	ex: import random
	random.randint(a, b)

Type methods (aka type-fucntions)

	> str.upper(‘hello’)
		makes all upper case
	> float.is_integer(3.0)
		‘True’
		- tells if number is integer
****
can call on value

str.upper(‘Hello’)

can be shorthanded

‘Hello’.upper()

ex:
>>> str.upper('Justin')
'JUSTIN'
>>> 'Justin'.upper()
'JUSTIN'
>>> float.is_integer(3.4)
False

Values - with multiple data points

3 types of values
	List
	Set
	Dictionary

when to use:
	List - line, order, queue -
	Set - bag, unique only, is value in?
	Dictionary - map, lookup, table

List - ordered sequence of values
	- 0-indexed….counting starts at zero

	Literals -
		ex: [‘justin’ , ‘matt’ , ‘david’]
		[1, 23, 24]
		empty = []
	can be nested - [[2,5], [4,5]]  list of lists!

in function

5 in [2,5]
>>>false

collection index

collection[number you want]

[‘a’, ‘b’, ‘c’][2]
>>>’c’

List

Lists are *mutable*

Assign data point to specific place in ordered list:

example:
>>> ages = [41, 16, 22]
>>> ages
[41, 16, 22]
>>> ages[0]=37
>>> ages
[37, 16, 22]
>>>

.index(v) - tells where item is in ordered list, finds value

.count(v) - counts # of values

.pop(i) - remove specified index in ordered list

.append - makes an operation on each item in a list

make str into a list use: list()

	example:
	>>> name = 'david'
	>>> list(name)
		['d', 'a', 'v', 'i', 'd']

Dictionary - unordered mapping mapping between *keys* and any *value*

	ex: word > definition …each word has one entry, word is like a key, definition is value

	dictionary uses curly brackets {}

	Add to dictionary to list

	Literal: {‘apple’:0.99 , ‘coke’:1.50, ‘joint’:5.00}

	key must bee unique
		key: ‘apple’
		value: ‘0.99’

	key can be int, str, False

	nested lists {‘ferrari’:{‘topSpeed’:90, ‘modelyear’:1977}}

	Operators

	keyvalue == , in,

	look up in dictionary
		dictionary[key]

	dict[key] = value

	Methods for dictionaries

	.keys() - lists keys in a dictionary

	.values() - lists values of dictionary

	.pop(k) - removes value according to what key you use, returns value it is removing

	.get(k, default) - returns value for key, if none exists, will return ‘default’

	adding item to dictionary
		phone numbers = {‘david’: ’5032242222’}
		phone numbers = [‘Jeff’] = ’5032244444’


Dictionary example:

>>> shopping = {'apple': 0.99, 'coke': 1.50, 'diet coke': 1.50}
>>> print(shopping)
{'diet coke': 1.5, 'coke': 1.5, 'apple': 0.99}
>>> shopping['broccoi'] = 3.00
>>> shopping.pop('coke')
1.5
>>> print(shopping)
{'diet coke': 1.5, 'broccoi': 3.0, 'apple': 0.99}
>>> shopping.keys()
dict_keys(['diet coke', 'broccoi', 'apple'])
>>> print(shopping['cake']
lkj

SyntaxError: invalid syntax
>>> print(shopping['cake'])
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    print(shopping['cake'])
KeyError: 'cake'
>>> print(shopping.get('apple'))
0.99
>>>

see this site for how to get highest value and/or key for a dict: http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary


Set
	- unordered collection of unique values

	- pile of values

	curly braces{}

	no colon {1,3, 34, 53, 2}

	empty set - set()
	>>nothing = set() - empty set

	set operators ==, ‘in’

		*value* in *set* returns boolean

	& compares difference between two sets

		& *set* & *set*
			- returns new set with all values that are in both
	| - pipe union

		returns set of all values in both, no duplicates
		{1,2} | {2,4}
			> 1, 2, 4

	variableName = {1,2} | {2,4}
		assigns | the variable name

	- minus operator
		returns difference of two sets,


Data structures and functions tips and tricks

Accessing LIST items:

Do a thing to all times in list - declare variable (ex: fruit) and do what yo want

>>> for fruit in ['apple' , 'pear']:
	print('eat ' + fruit)

eat apple
eat pear


Accessing Items in *SET*

get range operator

>>> ages = [37, 16, 22]
>>> ages[1:2]
[16]
>>> ages[1:]
[16, 22]
>>> ages[:]
[37, 16, 22]

get range works on strings

>>> sentence = 'Hi mom'

>>> sentence[0 : -1]
'Hi mo'

get operators *use negative* counts from the end, backwards

String Methods

**USE THEsE to manipulate user input**

.split - splits  string by ‘white space’

>>> 'Hi mom'.split()
['Hi', 'mom']

	can split by other delimiters besides ‘space’

.join - call on something (usually empty space0 and put list in parenth

>>> ''.join(['Hi' , 'mom'])
'Himom'
>>>

.append - makes an operation on each item in a list

example:

ages = [32, 16, 22]

new_ages = []

for age in ages:
        updated_age = age +1
        new_ages.append(updated_age)

print(new_ages)

.format - use braces {} in a string as empty places, call ‘.format’ on that string, and put arguments, arguments will be placed where the braces are

>>> 'I have {} {}'.format('3' , 'bananas')
'I have 3 bananas'
>>>

max - more with max

	can call on multiple arguments

sum - more with sum

	can sum a list >sum[1,2] -> 3
	can tell it what position to start sum  > >sum([1,2] , 1) -> 2
	can tell it specifically sum(start=1 , iterable=[1,2]) -> 2

sorted - return a new sorted list from the items in iterable

>>> ages = [32, 16, 22]
>>> sorted(ages)
[16, 22, 32]
>>> print(sorted(ages))
[16, 22, 32]

>>> print(sorted(ages, reverse=True))
[32, 22, 16]


day 4

Functions

will make our own funcitons

why use functions

1. Structure - label operations, complex

2. Re-use - make an operation over and over easily

3. Parameterization - if you can generalize the idea, you can make  function of it and use it anywhere

4. Interface - it just works…don’t need to understand - trust code to do what it does


How to write function

> def function_name(argument , list):
	*code block*
	return variable_name

return is output value
argument list is list of values, arguments, w/e

making a function does not call the function

example function

making a function ‘calc_time’ will find time given miles traveled and mph

> def calc_time(miles, mph):
	time = mils / mph
	return time

> travel_time = calc_time(100 , 50)



Scope - STAY IN YOUR SCOPE!!
	variables assigned in a scope *ONLY* guaranteed to be defined within that scope.

	scope is a block of code operations

	if statement does not define scope

	defining function *will* define scope

	shadowing - when a defined variable inside the defining function (def), variable will take def 	definition
		then variable can be defined and will be different

		example:

		name = 'Helen'
		def set_name():
    			name = 'David'
    			print(name) #will print ‘David’

		set_name()
		print_name()
				#will print ‘Helen’

why define functions for each step?

	1. Code explains itself

	2. Test parts in isolation

	3. Can re-use code


naming hints

	1. be unambiguous
	⁃
	2. units - use them
	⁃
	3. mirror structure type
	⁃
	4. type hints if necessary


3 hints for naming functions

verbs + nouns

	1. unambiguous

	2. reference return variable

	3. identify arguments


**Describing a function you define

use “”” some description “””

explicit description of what function does - see example below:

*how to print function description:

	>def should_keep_guessing(assessment):
    		"""Return if the program should keep prompting for guesses as a bool."""
    		return assessment != 'Correct!'

	>print(should_keep_guessing.__doc__)

day 5

Tuple

	Tuple: *immutable* list
		literal
		()
		>(1, 2, 3)
		> one item (1,) , empty tuple()

	operators ==, cannot do [ ] =

		make tuple from list
		> nums = [1, 2, 3]
		> tuple(nums) -> (1, 2, 3)

		hashable = immutable

	Uses of Tuples

	1.	multiples value w/ different meanings
	⁃	.items and .partition return tuples
	⁃	partition example >
	2.

Transforming Data

price_pair = (‘apple’ , 0.99)
item , price = price_pair
returns same as ——>
item = price_pair[0]
price = price_pair[1]

for item, price in item_to_price.items()  - use this to call on both variables



list comprehension in python

***see file seqtest.py

can use on any data structure

prices_dollars = [1.50, 0.75]
prices_cents = []
for dollar_val in prices_dollars:
    cents_val = dollars_val * 100
    prices_cents.append(cents.val)

****above code is done shorter with the code below****

prices_cents = [dollar_val * 100 for dollar_val in prices_dollars]

#code below finds all upper case in list
words_in_document = {'the' , 'cat' , 'hat', 'Justin'}
uppercase_words_in_document = {word.upper() for word in words_in_document}

#below uses operation on a dictionary
item_to_price_cents = {
  'apple': 99,
  'pear': 150
}

product_to_price_dollars = {
    product: prices_cents / 100
    for product, prices_cents
    in product_to_price_cents.items()
}


built in functions for sequences

len() - displays length or # of entries
reversed() - reverses order
sorted() - numerical order

can CAST one data type to another and back
	⁃	set(on a list or tuple)
	⁃	list
	⁃	tuple
	⁃	list -> dict and back, list must be two tuples

example of working with dicts and using .items
	dict(somedict.items()) == somedict

	opposite of dict.items = dict([(‘apple’, 99), (‘pear’, 150)])

enumerate( [ ] ) - gives an order to a list

zip - takes two lists of different type, puts them in tuple

range - gives range
	allows you to define range for an operation

None - value used to set up other values
	variable_name = None

	use instead of variable_name = ‘ ‘

	return None

day 6

files

characteristics of files

	•	Files are persistent
	•	Can communicate between instances of a program running
	•	Files are a source of data

Python can make an object called “file”

Open a file in Python

>open(‘filename.txt’)

Need to close file object - use a ‘with’ assignment statement

>with open(‘phonebook.txt’) as phone_book_file:
	do_something_with(phone_book_file)

does stuff, cleans up and ‘saves’

Can input and output strings in file, numbers must be converted back/forth to strings

READ file

Lines in a file are deliniated with *newlines* ex: \n

>with open(‘phonebook.txt’) as phone_book_file:
	phone_book_file.readlines()

.readlines - prints out lines straight no breaks

	can’t call ‘readlines’ twice, or for loop

for line in data_in_phonebook:
	name, number = ine.strip().split()

WRITE TO file

Second argument is what you want to do with the file. Enable writing with “w”

w = erases entire file

example:

>import random

>with open ('google-10000-english-usa.txt') as dictionary:
    all_words = dictionary.readlines()
    #opens, reads lines, then closes

>selected_word = ''
>while len(selected_word >=4:)
    selected_word = random.choice(all_words).strip()

>print(selected_word)

see slack example

Day 7

Sorting

how to

sorted() sorts w/e list is in parent, list of lists will be sorted by first value, 2nd value will be tie breaker

**note** can pass functions as values

sorted by function

can use function as key

use .get

max() and min() can key
	>print(max(names, key=names_to_ages))

see sorttest.py

#this is a code hint i got from google that I want to remember
#it removes a character from each str item in a list of str's
# mylist = [("aaaa8"),("bb8"),("ccc8"),("dddddd8")]
# mylist = ' '.join(mylist).replace('8','').split()
# print mylist


Day 9

more list sorting

how to sort list and print as columns…have to do it by hand

see slack example

dictionary comprehension
	like list comps, use curly braces

interleaving - combine list by variable - interleave

uninterleave - reverse

splat operator = *
	use in list comprehensions
	value in variable
	gives value for each item in list

this code is an example but doesn’t work:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, False]

interleaved = list(zip(list1, list2, list3))
uninterleaeved = list(zip(*interleaved)

print (interleaved)

print (uninterleaved)

encode and decode

ex:

>>> b'hello'.decode('utf-8')
'hello'


Classes

Classes - group together functions that work in the shared scope of the class
	Defining of class creates a **type**


Class is a collection of functions.
Instance of a class/object is a bag of variables.

Encapsulation

	classes version of functions being contracts

	One person can work on implementation. One person can work on use.
	They agree on contract, they don’t need to worry directly abut each other’s work.

	The functions in a class can define contract.

	The person that uses the functions doesn’t care how they are made.

	Short form of class method calling is cool…you don’t have to know the exact class the instance has.


Pycharm IDE

from pycharm website

‘project’ is a directory/folder

new project>code guild directory

hot tips

Module

.py files are Modules

	It’s like copying the module code at the top of your code

in the target .py file you can import any top level item using the name of the Python film without the .py

	modules can be nested
	__init__.py allows directory to be module
		then you can > import directory_name.module_name
Using PyCharm tools
test file: in PyCharm must be configured, including test path, which is the name of these file you are making

when test program uses *Class* methods to test =
	import unittest
	class TestName(unittest.TestCase):



Note: check out Kyle’s rain animation in this file: https://github.com/bizzcat/codeguild/blob/master/final_rainfall.py


‘magic methods’
	__getitem__

	zip makes an object that acts like a list

Into. Web Applications

3 parts
	1. Database

		Where data is persistently stored.

		It is another program that has a very generic interface that lets you save and fetch 		data.

		We will probably use PostgreSQL

	2. Back-End

		Web server - **business logic** - what happens

		Dynamically generates web pages.
		When a person goes to yourwebsite.com/ponies it will figure out what’s on ‘/ponies’ 		might fetch database and return content associated with it for display

		Web framework - figure out how to generate output *content* from an input *path*

	3. Front-End

		HTML/CSS/JS

		HTML - actual structured content
		CSS describes the presentation of the content
		JS is code for the user’s web browser to run to enable complex interactions with user.


**Interfact Principles**

Basic HTML/CSS/JS

HTML - structures existing text
CSS - specifies how things are displayed

Mozilla developer tutorial: http://apps.timwhitlock.info/emoji/tables/unicode

Tags - open and close element
Element - entities tags produce
Attributes - live inside single tag

Basic structure every website will have:

<!DOCTYPE html>
<html lang="en">
<head>
  <title>A tiny document</title>
</head>
<body>
  <h1>Main heading in my document</h1>
  <!-- Note that it is "h" + "1", not "h" + the letters "one" -->
  <p>Look Ma, I am coding <abbr title="Hyper Text Markup Language">HTML</abbr>.</p>
</body>
</html>

10 important Tags

<!DOCTYPE html>

<html lang="en"> ... </html>
**head is meta data**
<head>
  <title>My webpage is awesome!</head>
</head>
<body>
  <header> Header is top of page, usually stays static </header>
**header is part of what page displays**
  <h1> headings, 6 sizes </h1>

  <nav> sidebar navigation </nav>

  anchor element <a>
  makes a link
  <a href="http://justinepperly.com">My personal website</a> is awesome.

  <section> **where you put content**
    <p> **like a paragraph**

  <div> most basic tag for a section of a page...

*SEE NOTES file htmlintro.html*
use web inspector

*Forms <form>*

See Mozilla tutorial: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/My_first_HTML_form

Groups multiple inputs from user together
Machine readable output from user input

<form></form>
<label>
  uses 'for'= <input id> and the text of the label
<input>
  uses 'type' and 'id' operations
  closes itself, like img tag
<button>
  3 types, 'submit' 'reset' or 'button'
<select>
  makes a drop-down
  <option> makes an option...use text
    in <option> value="" specifies an ID for the data

example:
			<form action="/my-handling-form-page" method="post">
			    <div>
			        <label for="name">Name:</label>
			        <input type="text" id="name" />
			    </div>
			    <div>
			        <label for="mail">E-mail:</label>
			        <input type="email" id="mail" />
			    </div>
			    <div>
			        <label for="msg">Message:</label>
			        <textarea id="msg"></textarea>
			    </div>
			    <div>
			      <label for="format">Format:</label>
			      <select id="format">
			        <option value="email">Email</option>
			        <option value="telegram">Telegram</option>
			        <option value="letter">Snail Mail</option>
			    </div>
			    <div class="button">
			        <button type="submit">Send your message</button>
			    </div>
			</form>
**CSS**

can apply multiple classes

p {color: red;}

selector {property: value;}

4 main selector types
	1. element (in css file)
	2. id=
	3. class= (.classname)
	4. heirarchy

declare source in <head>
<head>
	<link href="basicstyle.css" rel="stylesheet">
</head>

selecting HTML - can select any element of a type ex p {} or one ID
	ID
		#[IDhere]
		<header id="coolsec">
		#coolsec{
		  color: blue
		}
CSS class selectors - can apply to a group
see guide: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference
	use . operator instead of #
	use class="class names sep by space"

	<header class="spicy hot">

	.hot {
		color: red;
	}

	.spicy {
		font-size: 30px;
	}

ul > li {
	text-shadow: 1px 1px 1px gray;
}
<!--  only match li's in ul-->

*css conflicts*
	whatever is 'deeper' & more specific wins in this order class, id, elementtag

*fun with css*
example css:
#shadow {
	text-shadow: 1px 1px 10px gray;
}
	color, parameters
	{color: rgb(128, 0, 0)}
	-or- transparency
	{color: rgba(128, 0, 0, .5)}
		a = 'alpha' from 0-1
	-or- via hue
	{color: hsl(360, 100%, 100%)}

lengths em's px and %
	1em is about 14pt
		ex:
		p {
			font-size: 1.0em;
		}
*how to use classes on specific elements...see .box p from https://developer.mozilla.org/en-US/docs/Web/CSS/border-left*
**<div class='box'>
  <p>This box has a border on the left side.</p>
</div>
CSS

.box {
  background-color: #ffaabb;
  border-left: 4px solid #000;
  height: 100px;
  width: 100px;
}

.box p {
  font-weight: bold;
  text-align: center;
}**

*CSS LAYOUT*

Element types
1. Block - arranged vertically, take up as much apace as possible by default.
2. In line - flow like words, wrap inside parent element

**Box model**

Every element has:
1. W & H - core size of inner content
2. Padding - extra space between core and border
3. Border - visible outline of defined thickness
4. Margin - extra space between border and neighboring elements

Margins overlap
Width and Height are just big enough to contain elements, can change w/ fixed width

#floats

Causes element to be fixed to the upper-left of the parent element

float right on img under text causes img to always be right of text

see online for examples

**Flex Box**

top level container is flex Box
use for collums

<article> is parent container
css:
article {
	display:flex;
}
section {
	flex-basis: 200px;
	flex-grow: 1;
}

learnlayout.com and other posted by David flexboxin5.com

# CSS values

percentages are relative to the _parent element_
	if <section> is width 75%, an element in that <section> at 75% will be 75% of parent,
		which is 75%, so 75% of 75%

Ems are relative to _current text size_
1.0em in an 'h1'b/c 'h1'

Use ems for padding around textual elements, typographic measurements.

Ems, not comparable across document. Do not use for borders, backgrounds, or LAYOUT
	spacing, etc. use pixels.

	if font is 100px, 2ems the ems for font size 50px, 2ems will be smaller.

CSS .classes and element interactions

p.classname

#JAVASCRIPT

; - end statement
{} define Blocks
"use strict"
function() {
	var i = 1;
	i = i + 1;
}


see jsbasics.md from david

double quotes

booleans are true and false lowercase

uses null instead of None

"undefined" uninitialized variable

Objects are like dictionaries in Python

	map properties to values

#Objects and Arrays

Objects are like dictionaries
can use dict["property"];
	> value
property can be variable or property

#or

can use dot operators
	ex: dict.property;
	> value

if you know your property before, use dot syntax

## Arrays
List, uses []

can have property

# Basic operators

same as python

can use advanced operators +=

++ and -- decriment

##Comparison

=== is the same as ==
!== is !=

##Boolean

&& is and
|| is or
! is not

#Control Statements
#if Statements
	like python

#For loops and For-in Loops

python for loop - do not use for Arrays

see notes: for loops for dictionaries and arrays are different


#Functions and calling

functions are called like python

functions use var

var addTwo - function(x) {
	var two = 2;
	return x + two;
}

#Prototype Methods
similar to python...look it up

# Data transformations

similar to list comprehension, Js Uses **map**

var priceInCents = [100, 150, 400]

#Debug output

'console.log()' to print things to the browser console

js
var name = 'david'

#JS in browser

must make baby html page to run JS in browser
