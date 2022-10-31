def reverse_for(string):
   rstring=''
   for x in string:
    rstring=x+string
   return rstring
string="1234abcd" 
print('original string:',string)
print('reverse string:',reverse_for(string))