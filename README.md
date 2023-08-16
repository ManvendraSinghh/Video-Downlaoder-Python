# Video-Downlaoder-Python

!! Important Note !!
There is a bug in the recent update of PyTube so we have to make slight changes for it to work.
In order to solve the problem of 
" __init__: could not find match for ^\w+\W ", 
you have to edit a line in cipher.py file which is located in

C:\Users\#####\AppData\Local\Programs\Python\Python311\Lib\site-packages\pytube\cipher.py
 
replace the line 30, which is:

var_regex = re.compile(r"^\w+\W")

with this line :

var_regex = re.compile(r"^\$*\w+\W")

It will work again.
