class Car:
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
my_new_car = Car('audi', 'a4', 2019)#Car 클래스에서 인스턴스를 새로 만들고 my_new_car 변수에 할당.
print(my_new_car.get_descriptive_name())
