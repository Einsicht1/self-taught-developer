# class User:
#     count = 0
#
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#         User.count += 1
#
#     def __str__(self):
#         return self.name
#
#     @classmethod
#     def number_of_users(cls):
#         print(f"총 유저수는 {cls.count}입니다.")
#
#     # 정적 메소드
#     @staticmethod
#     def is_valid_email(email_address):
#         return "@" in email_address
#
#
# user1 = User("김", "kim@gmail.com")
# user2 = User("이", "lee@gmail.com")
# user3 = User("박", "park@gmail.com")
#
# print(User.is_valid_email("email"))  # 클래스를 통해 클래스 메서드 호출
# print(user1.is_valid_email("email@email.com"))  # 인스턴스를 통해 클래스 메서드 호출

#
# user2.count = 10
# print(User.count)
# print(user1.count)
# print(user2.count)
# print(user3.count)


#
# def add_print_to(original):
#     def wrapper():
#         print("함수 시작")
#         original()
#         print("함수 끝")
#     return wrapper
#
# @add_print_to
# def print_hello():
#     print("안녕")
#
# print_hello()


# print("aa".zfill(10))

# help(list)
#
# name: str = "kim"


class Mom:
    pass


class Son(Mom):
    pass


son = Son()

# print(issubclass(Son, Mom))
# print(issubclass(Son, object))
# print(issubclass(Son, list))

#
# class Employee:
#     """직원 클래스"""
#     company_name = "코드잇 버거"
#     raise_percentage = 1.03
#
#     def __init__(self, name, wage):
#         """인스턴스 변수 설정"""
#         self.name = name
#         self.wage = wage
#
#
# class DeliveryMan(Employee):
#     """배달원 클래스"""
#
#     def __init__(self, name, wage, on_standby):
#         super().__init__(name, wage)
#         self.on_standby = on_standby
#
#
#
# taeho = DeliveryMan("성태호", 7000, True)


class A:
    def __init__(self, a):
        self.a = a


class B:
    def __init__(self, b):
        self.b = b


class C(A, B):
    pass

