import re

         'a5555b',
         'def ghi', 'abc ab']

for item in data:
    m = re.search(r'a.c', item)
    if m:
        print ( m.group() + ' matched in ' + '\'' + item + '\'' )