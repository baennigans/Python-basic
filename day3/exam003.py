'''
    setdefult   새데이터삽입
    update      key 없으면 데이터삽입, key 있으면 데이터수정
    pop         데이터삭제
'''

members ={'홍길동':'010-1111-2222','박길동':'010-3333-4444'}
print(members)

members.setdefault('윤길동','010-5555-6666')
members.setdefault('이길동')
print(members)
print()

members.update(이길동='010-7777-8888')     # 새데이터 삽입O, 기존데이터 수정X
print(members)
members.update(한길동='010-9999-0000')
print(members)
members.update({2023082501:'010-2345-6789'})
members.update([[2023082502, '010-1234-5678'], ['고길동', '010-4566-2345']])
members.update(zip(['park', '이길동'],['8282', None]))
print(members)
print()

value = members.pop('이길동')
print(f'pop("이길동") : {value}')
members.pop('구길동', "없음")
print(members)
members.popitem()
print(members)
print()

value = members.get('홍길동')
print(f'홍길동 : {value}')
print(f'이길동 : {members.get("이길동")}')
