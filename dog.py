class Dog:    #Dog 클래스 정
     """개를 모형화"""
     def __init__(self, name, age):#클래스에 속한 함수는 method. init method는 새 인스턴스를 만드는 특별 함
       """name과 age 속성 초기화"""
       self.name = name#접두사 self가 붙은 변수는 클래스의 모든 method에 접근가능
       self.age = age
     def sit(self): #sit()과 roll_over()method속성을 정의. 이름, 나이 등 추가정보가 필요없으므로 self매개변수 하나만 받도록 정의
        """명령에 따라 앉는 개"""
        print(f"{self.name} is now sitting.")
     def roll_over(self):
        """명령에 따라 구르는 개"""
        print(f"{self.name} rolled over!")
my_dog = Dog('Willie', 6) #클래스에서 인스턴스 만들기 이름이 Willie인 6살 먹은  만들기. 이 행을 읽고 파이썬은 Dog의 __init__()메서드 호출
print(f"My dog's name is {my_dog.name}.")#속성에 접근할 때에는 점 표기법 사용.
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()#메서드호출할 때에는 인스턴스 이름(my_dog)을 쓰고 점을 쓴 다음 호출할 메서드 이름을 쓴다.
my_dog.roll_over()
your_dog = Dog('Lucy', 3)#인스턴스 여러개 만들기 두번째 개 your_dog
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
