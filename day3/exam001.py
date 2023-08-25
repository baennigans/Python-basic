str = "Hello, World"
print(str, str.upper(), str.lower())
print()

strList = str.split(',')
print(strList)
print()

str2 = '/'.join(strList)
print(str2)
print(f'[{strList[1].lstrip()}]')
print()

str = '    Hello World     '
print(f'str : [{str}]')
print(f'lstrip() : [{str.lstrip(" !")}]')
print(f'rstrip() : [{str.rstrip()}]')
print(f'strip() : [{str.strip("! ")}]')
print()

str = 'hello'
print(f'str : [{str}]')
print(f'str : [{str.center(11)}]')
print(f'str : [{str.center(10)}]')
print(f'str : [{str.ljust(10)}]')
print(f'str : [{str.ljust(10)}]')
print(f'str : [{str.rjust(10)}]')
print(f'str : [{str.zfill(10)}]')
print()

str = 'Hello World'
print(f'"o" 위치 : {str.index("o")}')
print(f'"o" 위치 : {str.index("o",6)}')
print(f'"o" 위치 : {str.find("o",6)}')
print(f'"o" 위치 : {str.index("o")}') # 문자열이 없는 경우 예외발생
print(f'"o" 위치 : {str.find("o")}')  # 문자열이 없는 경우 -1 반환
print(f'"o" 위치 : {str.rfind("o")}')
print(f'"l" 개수 : {str.count("l")}')
print(f'"l" => "rr" 변환 : {str.replace("l", "rr")}')
