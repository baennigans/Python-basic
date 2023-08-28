# quit가 나올때까지 문자열을 입력받아 test02.txt 저장한 후
# test02.txt에 저장된 모든 문자열 읽어서 모니터에 출력

# with open('test02.txt', 'w') as file:
#     print('문자열을 입력하세요. quit 입력시 종료')
#     while True:
#         msg = input()
#         if msg == 'quit':
#             break
#         #file.write('{0}\n'.format(msg))
#         file.write(f'{msg}\n')
#
# print('파일 저장 완료...')

with open('test02.txt', 'r') as file:
    lines = file.readlines()

print('< 읽어온 데이터 출력 >')
for line in lines:
    print(line.rstrip('\n'))
    line.isl
