def build_person(first_name, last_name):
    """사람에 대한 정보 딕셔너리 반환"""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimmi', 'hendrix')
print(musician)
