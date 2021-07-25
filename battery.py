class Car: #Car클래스로 시작함. 자식클래스를 만들때는 부모클래스가 반드시 현재파일에 있어야 하며 반드시 자식클래스보가 앞에 있어야  함.
     """자동차를 나타내는 코드"""
     def __init__(self, make, model, year):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
     def get_descriptive_name(self):#get_descriptive_name 메서드에서 자동차를 설명하는 읽기쉬운 문자열로 변환.
        """알아보기 쉬운 이름 변환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
     def read_odometer(self):
         print(f"This car has {self.odometer_reading} miles on it.")
     def update_odometer(self, mileage):
         if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
         else:
             print("You can't roll back an odometer!")
     def increment_odometer(self, miles):
         self.odometer_reading += miles
class Battery:
        """전기자동차의 배터리를 모델화하려는 단순한 시도"""
        def __init__(self, battery_size=75):
            """배터리의 속성 초기화"""
            self.battery_size = battery_size
        def describe_battery(self):
            """배터리의 크기 설명하는 문장 출력"""
            print(f"This car has a {self.battery_size}-kwh battery.")
class ElectricCar(Car): #자식클래스 ElectricCar를 정의함. 자식클래스를 정의할 때는 반드시 부모클래스 이름을 괄호안에 써야 함.
        """전기 자동차에만 해당하는 특징을 나타냅니다"""

        def __init__(self, make, model, year): #super()함수는 부모클래스를 호출할 수 있게하는 특별한 함수오 파이썬이 Car 클래스에서 __init__메서드를 호출하여 ElectricCar인스턴스에 이 메서드에서 정의된 속성을 모두 전달하게 함. super라는 이름은 부모클래스를 슈퍼클래스 자식클래스를 서브 클래스라고 부르는 명명큐칙에서 왔음.
            """부모 클래스의 속성을 초기화 한 다음 전기자동차에만 해당하는 속성을 초기화합니다"""
            super(). __init__(make, model, year)
            self.battery = Battery() #self.battery_size속성을 추가하고 초깃값을 75로 정함. 이 속성은 ElectricCar클래스에서 생성한 모든 인스턴스와 연결되지만 Car의 인스턴스와 연결되지는 않음.

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
