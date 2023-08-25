str = "Hello World"
print(str, str.upper(), str.lower())
print()

strList = str.split()
print(strList)
print()

str2 = '/'.join(strList)
print(str2)
print(f'[{strList[1].lstrip()}]')

str = '    Hello World     '
print(f'str : [{str}]')
print(f'lstrip() : [{str.lstrip()}]')
print(f'rstrip() : [{str.rstrip()}]')
print(f'strip() : [{str.strip("! ")}]')

str = 'hello'
print(f'str : [{str}]')
print(f'str : [{str.center(11)}]')


str = 'Hello World'
print(f'"o"위치 : {str.index("o")}')
print(f'"o"위치 : {str.index("o",6)}')
print(f'"o"위치 : {str.find("o",6)}')


