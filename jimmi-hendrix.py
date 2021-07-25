def get_formatted_name(first_name, last_name): #get_formatted_name함수가 성과이름을 매개변수로 받도록 정의함
    """풀네임 반환"""
    full_name = f"{first_name} {last_name}" #함수는 성과 이름 사이에 공백을 두고 결합해서 full_name에 할
    return full_name.title() #full_name의 첫ㄱ르자를 대문자로 바꿔 함수를 호출, 반
musician = get_formatted_name('jimmi', 'hendrix') 
print(musician)
