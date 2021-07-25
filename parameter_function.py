def describe_pet(animal_type, pet_name):
    #반려동물 정보
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry') #함수호춣 위치형 매개변수
describe_pet('dog', 'willie')  #함수 여러번 호출하기
describe_pet(pet_name='harry', animal_type='hamster') #키워드 매개변수 
