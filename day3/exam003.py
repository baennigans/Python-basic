members ={'홍길동':'010-1111-2222','박길동':'010-3333-4444'}
print(members)

members.setdefault('윤길동','010-5555-6666')
members.setdefault('이길동')
print(members)

members.update(이길동='010-7777-8888')
print(members)
members.update(한길동='010-9999-0000')
print(members)


members.pop('구길동', "없음")
print(members)

members.popitem()
print(members)

value = members.get('홍길동')
print(f'홍길동 : {value}')
print(f'이길동 : {members.get("이길동")}')