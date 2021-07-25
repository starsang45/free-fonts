def full_name (first_name, last_name):
    """이름 full name 반환"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = full_name ('jimmi', 'hendrix')
print(musician)
