# Unit 1: 객체 지향 프로그래밍이란?
- Chapter 1: 객체 지향 프로그래밍 시작하기
- Chapter 2: 객체를 만드는 법
- Chapter 3: 미리 알고가야 할 것들
- Chapter 4: 객체 만들기 연습
- Chapter 5: 객체 지향 프로그래밍 직접 해보기
## Chapter 1: 객체 지향 프로그래밍 시작하기
### 객체란?
- '속성'과 '행동'으로 이루어진 것.
- 예: 자동차는 바퀴 4개, 색깔, 의자, 핸들 등의 속성과 전진, 후진 등의 행동을 가진 객체
- '속성'과 '행동'을 떠올릴 수 있는 것이라면, 그것이 현실에 존재하던 가상에 존재하던 모두 객가 될 수 있다.
- 파이썬에서 속성은 변수로, 행동은 함수로 나타낸다.
### 객체지향 프로그래밍이란?
: 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 접근법이다.
: 프로그램을 객체들 간의 소통으로 바라보는 것.
#### 객체 지향 프로그래밍으로 프로그램을 만들려면?
- 프로그램에 어떤 객체들이 필요할지 정한다.
- 객체들의 속성과 행동을 정한다.
- 객체들이 서로 어떻게 소통할지 정한다.
## Chapter 2: 객체를 만드는 법
#### 인스턴스 변수 정의하기
  - 인스턴스 이름.속성이름(인스턴스 변수) = "속성값"
예시
```
class User:
    pass

user1.name = "김"
user1.email = "kim@gmail.com"

user2.name = "이"
user2.email = "lee@gmail.com"
```
#### 인스턴스 메서드 정의하기
예시
```
class User:
def say_hello(some_user):
    print(f"안녕, 나는 {some_user.name}이야!")
    pass

user1.name = "김"
user1.email = "kim@gmail.com"

user2.name = "이"
user2.email = "lee@gmail.com"

User.say_hello(user1) # 클래스에서 메서드 호출
user1.say_hello()  # 인스턴스에서 메서드 호출

결과:
안녕, 나는 김이야!
안녕, 나는 김이야!
```
user1.say_hello()에 user1을 인자로 넘기지 않아도 호출이 된다.
넘기는 순간 에러가 발생한다. <br>
인스턴스가 메서드를 호출할 때는 자기 자신이 첫 번째 인자로 넘어간다! <br>
#### self를 사용하자.
인스턴스가 메서드를 호출할 때는 자기 자신이 첫 번째 인자로 넘어간다! <br>
이를 명시해주기 위해 파이썬에서는 인스턴스 메서드의 첫 파라미터로 "self"를 사용한다.
이렇게 안해도 에러가 나는건 아니지만, 이건 파이썬 쓰는 사람들끼리의 규칙이다.

#### `__init__`
- 언더바 두개에 쌓여있는 메서드를 magic method, 특수 메소드라고 부른다. 
- magic method는 특정 상황에서 자동으로 호출되는 메소드다.
- `__init__`메서드는 클래스 생성시 자동으로 호출된다.
```
class User:
    def initialize(self, name, email):
        self.name = name
        self.email = email

user1 = User()
user1.initialize("김코딩", "hi@gmail.com")
```
`__init__`메서드 없이는 객체 속성을 지정하기 위해 위처럼 해야한다. <br>
`__init__`메서드는 객체를 생성할 때 인자를 넘겨주면 되므로 훨씬 간다해진다.
아래 예시를 보자.
```
class User:
   def __init__(self, name, email):
        self.name = name
        self.email = email

user1 = User("김코딩", "kim@gmail.com")
```
`user1 = User("김코딩", "kim@gmail.com") 요 코드 한 줄이 실행되면
1) User의 인스턴스 하나가 생성됨
2) `__init__` 메서드가 호출됨
한 번에 객체를 생성하고 속성을 지정해줄 수 있다는 장점 때문에 보통 클래스를 만들땐 항상 `__init__`메서드가 같이 호출된다.

#### `__str__`
위 코드에서 `print(user1)`을 해보면 `<__main__.User object at 0x7fc9ab5c9670>`이런 값이 나온다. 
인스턴스를 프린트 했을 때 원하는 값이 나오게 하려면 `__str__`을 오버라이드 하면 된다.
```
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def __str__(self):
        return self.name

user1 = User("김코딩", "kim@gmail.com")

print(user1)
결과: 김코딩
```

#### 클래스 변수
-클래스 변수는 class 정의 부분 바로 아래 변수를 정의해주면 된다.
예시를 보자.
```
class User:
    count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name

User.count = 1
print(User.count)
결과: 1
```
- 그렇다면 count변수가 User인스턴스의 총 개수 품게 하려면 어떠게 할까?
- User인스턴스가 생성될 때 마다 count +=1을 해주면 된다.
- User인스턴스가 생성될 때마다 `__init__`메서드가 호출되므로 거기에 더해주면 된다.
```
class User:
    count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email

        User.count += 1

    def __str__(self):
        return self.name


user1 = User("김", "kim@gmail.com")
user2 = User("이", "lee@gmail.com")
user3 = User("박", "park@gmail.com")

print(User.count)
결과: 3
```
클래스 변수를 출력하고 할당하는 방법에 대해 좀 더 살펴보자.
```
...생략....
user1 = User("김", "kim@gmail.com")
user2 = User("이", "lee@gmail.com")
user3 = User("박", "park@gmail.com")

user2.count = 10
print(User.count)
print(user1.count)
print(user2.count)
print(user3.count)

결과
3
3
10
3
```
- user2.count를 새로 정의한 부분때문에 그것만 10값이 나왔다.
- 그런데 user2.count=10은 인스턴스 변수를 할당해준 것이지, 클래스 변수를 할당한게 아니다.
- 즉 같은 이름을 가진 클래스 변수와 인스턴스 변수가 존재하는 것이고, 이때는 인스턴스 변수가 선행한다.
- 결론: ***클래스 변수와 같은 이름의 인스턴스 변수는 만들지 않는다!***

#### 데코레이터
: 함수를 인자로 받아 꾸며진 함수를 리턴하는 함수
```
def print_hello():
    print("안녕")


def add_print_to(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper

add_print_to(print_hello)()

결과값
함수 시작
안녕
함수 끝
```
- 어떤 함수를 데코레이터 함수에 넣으려면 @를 사용하면 된다.
```
def add_print_to(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper

@add_print_to
def print_hello():
    print("안녕")

print_hello()

결과값
함수 시작
안녕
함수 끝
```

#### 클래스 메소드
- 클래스 메소드는 메소드 위에 @classmethod 데코레이터를 달아주면 된다.
- 클래스 메소드 첫 인자는 self가 아닌 ***cls***를 사용한다. (약속임. 안한다고 에러가 나진 않지만)
- 클래스 메소드는 클래스를 통해 호출할 수도 있고, 인스턴스를 통해 할 수도 있다.
```
class User:
    count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email

        User.count += 1

    def __str__(self):
        return self.name

    @classmethod
    def number_of_users(cls):
        print(f"총 유저수는 {cls.count}입니다.")


user1 = User("김", "kim@gmail.com")
user2 = User("이", "lee@gmail.com")
user3 = User("박", "park@gmail.com")

User.number_of_users()  # 클래스를 통해 클래스 메서드 호출
user1.number_of_users()  # 인스턴스를 통해 클래스 메서드 호출

결과
총 유저수는 3입니다.
총 유저수는 3입니다.
```

#### 인스턴스 메소드 vs 클래스 메소드
- 인스턴스 메소드: `User.say_hello(user1)` 또는 `user1.say_hello()`
- 클래스 메소드: `User.number_of_users()` 또는 `user1.number_of_users()`
- 클래스 메소드는 클래스가 첫 인자로 자동 전달된다.
- 이렇게 될 수 있는 이유는 @classmethod 데코레이터 떄문이다.

#### 언제 각 메소드를 사용해야 할까?
- 위에서 정의한 classmethod는 사실 instance method 만들어도 문제는 없다.
- 언제 어떤 메소드를 쓰냐의 기준은 어떤 변수를 쓰냐에 달렸다.
- 클래스 변수를 사용한다면 클래스 메서드, 인스턴스 변수를 사용한다면 인스턴스 메서드를 사용하자.
- 만약 클래스 변수, 인스턴스 변수 둘 다 사용한다면 -> 인스턴스 메소드를 사용해라!
- 인스턴스 메서드는 인스턴스, 클래스 변수 둘 다 사용 가능하지만, 클래스 메서드는 인스턴스 변수를 사용 못하기 때문.
- 인스턴스가 하나도 없을 때에도 사용될 가능성이 있는 메서드라면 클래스 메서드를 사용하자!

#### 정적 메소드(static method)
- 인스턴스 변수나 클래스 변수 중 아무것도 사용하지 않을 때 static method사용.
- static method는 첫 인자로 self, cls 중 어느것도 자동으로 넘어가지 않는다.
```
...생략...
    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address


user1 = User("김", "kim@gmail.com")
user2 = User("이", "lee@gmail.com")
user3 = User("박", "park@gmail.com")

print(User.is_valid_email("email"))  # 클래스를 통해 클래스 메서드 호출
print(user1.is_valid_email("email@email.com")) 

결과값
False
True
```
## Chapter 3: 미리 알고가야 할 것들
### 1) 파이썬은 순수 객체 지향 언어다 = 모든 것이 객체다
```
print(type(1))
print(type("a"))
print(type([]))
print(type({}))
print(type(()))

결과값
<class 'int'>
<class 'str'>
<class 'list'>
<class 'dict'>
<class 'tuple'>
```
파이썬은 모든 것이 클래스이다.
### 2) 파이썬 가변 타입 vs 불변타입
- 직접 작성하는 클래스는 가변타입이다.
- 내장 클래스 가변/불변 여부
 ![](https://images.velog.io/images/kpl5672/post/6684de78-9b66-49b3-b6d0-a76a5943d661/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.26.40.png)
 
### 3) 절차지향 vs 객체지향
- 객체지향 개념이 등장하기 이전에 절차지향이있었다.
- 절차지향에는 객체 개념이 없는 대신 '함수'개념이 쓰인다.
![](https://images.velog.io/images/kpl5672/post/d6681b35-91f3-4e00-908e-4a415c9af549/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.30.01.png)

### 4) tenary expression
![](https://images.velog.io/images/kpl5672/post/c68ba69c-02aa-45d7-b0de-753531c6b939/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.32.15.png)

### 5) zfill method
![](https://images.velog.io/images/kpl5672/post/241c91f9-1af9-424d-9306-96c4d6e29c91/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.33.27.png)

## Chapter 4: 객체 만들기 연습
## Chapter 5: 객체 지향 프로그래밍 직접 해보기


# Unit 2: 객체 지향 프로그래밍의 4가지 기둥
- Chapter 1: 추상화(Abstraction)
- Chapter 2: 캡슐화(Encapsulation)
- Chapter 3: 상속(Inheritance)
- Chapter 4: 다형성(Polymorphism
## Chapter 1: 추상화(Abstraction)
#### 추상화란?
- 특정 코드를 사용할 때 필수적인 정보를 제외한 세부사항을 가리는 것.
- 커피 머신 내부 작동 원리를 몰라도 커피 머신을 쓸 수 있다. 이게 추상화의 원리
- 변수에 값을 할당하는 것도 추상화다.
- 함수를 사용하는 것도 추상화다.
- 클래스를 사용하는 것도 추상화다.
- 예를 들어 list.append(값) 뒷단에서 돌아가는 클래스 내부 로직을 몰라서 append를 사용할 수 있다.

#### 추상화를 잘 하려면 이름을 잘 지어야 한다!
- 변수명에 의미를 잘 담아 짓자.
#### 추상화를 잘 하려면 문서화를 잘 해야 한다.
- 변수명 잘짓기에도 한계가 있으니 docstring(문서화 문자열)을 잘 활용하자.
-`help(class_name)` 을 사용하면 해당 클래스의 모든 docstring이 출력된다.
- 예: help(list)
#### docstring 스타일 3개
1). Google docstring
```
"""유저에게 추천할 영상을 찾아준다
Parameters:
  number_of_suggestions (int): 추천하고 싶은 영상 수
    (기본값은 5)
    
Returns:
  list: 추천할 영상 주소가 담긴 리스트
"""
```
2). ReStructuredText(파이썬 공식 문서화 기준)
```
"""유저에게 추천할 영상을 찾아준다
    
:param number_of_suggestions: 추천하고 싶은 영상 수
  (기본값은 5)
:type number_of_suggestions: int
:returns: 추천할 영상 주소가 담긴 리스트
:rtype: list
"""
```
3). NumPy/SciPy (통계, 과학 분야에서 쓰이는 Python 라이브러리)
```
"""유저에게 추천할 영상을 찾아준다
    
Parameters
----------
number_of_suggestions: int
  추천하고 싶은 영상 수 (기본값은 5)
    
Returns
-------
list 
  추천할 영상 주소가 담긴 리스트
"""
```
#### 파이썬은 동적 타입 언어이다.
- type 지정을 해주지 않아도 된다.
- 반대 말인 정적 타입 언어는 변수를 선언할  꼭 타입을 지정해주어야 한다.때
#### type hinting
- 무슨 타입인지 설명해주는 코드를 작성할 수 있다.
- 방법은 `변수명: type명`이다.
- 예시: name: str = "kim"
![](https://images.velog.io/images/kpl5672/post/baab04c1-aaeb-4157-8ea2-d07a47894d09/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.52.05.png)
- type hinting대로 작성하지 않아도 에러가 나진 않는다.
- python 3.5 이후부터만 사용 가능.
## Chapter 2: 캡슐화(Encapsulation)
### 캡슐화 정의
- 객체의 일부 구현 내용에 대한 외부로부터의 ***직접적인 액세스를 차단***하는 것.
- 객체의 ***속성과 그것을 사용하는 행동을 하나로*** 묶는 것.
### 외부 접근 차단하는 법:
- 변수나 메서드 이름 앞에 언더바 두개('__')를 붙여준다.
```
class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.set_age(age)                   
        self.__resident_id = resident_id
    
    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.__resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drinking_age      

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.__age) + "살입니다!"

    def get_age(self):
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        return self.__age

    def set_age(self, value):
        """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드"""
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다")
            self.__age = 0
        else:
            self.__age = value

# 주민 인스턴스 생성
young = Citizen("younghoon kang", 18, "87654321")

print(young.__str__()) # 출력: younghoon kang씨는 18살입니다!
print(young.__authenticate("87654321")) # 에러가 난다!!!
```
#### `__`가 붙은 변수에 접근하는 메서드
- can_drink메서드는 self.__age를 사용한다.
- 이처럼 __가 붙은 변수는 외부에서 사용 불가능하지만, 내부 메서드에선 접근이 가능하다.
- 이것이 바로 캡슐화의 두 번쨰 정의인 "객체의 ***속성과 그것을 사용하는 행동을 하나로*** 묶는 것." 에 해당하는 내용이다.

#### getter, setter
캡술화된 변수의 값을 읽어주는 메서드는 getter, 할당해 주는 메서드를 setter라고 한다.

#### 캡슐화 정리
![](https://images.velog.io/images/kpl5672/post/c36d7ecf-d08f-4d1c-a707-4131221e49cb/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.10.18.png)

### 파이썬의 캡슐화와 캡슐화 문화
![](https://images.velog.io/images/kpl5672/post/98e8ca6e-2072-4846-8331-ce572fa394b8/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.13.51.png)
![](https://images.velog.io/images/kpl5672/post/ebdecf4a-c805-4bae-818c-257e8062305b/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.13.56.png)
![](https://images.velog.io/images/kpl5672/post/3734eb81-5367-4cd2-b1e5-c38a2c920b7a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.14.02.png)
![](https://images.velog.io/images/kpl5672/post/1bafeab9-5dac-4387-8d1c-4ae005fc7f6d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.14.08.png)
#### 파이썬의 캡슐화 약속: _한개
- 파이썬 개발자들은 캡슐화를 위해 변수나 메소드 앞에 언더바를 하나만 붙인다.
- 이렇게 하면 외부에서 해당 데이터에 직접 접근하지 말라는 경고다.
- 물론 언더바 하나 더한 것 자체는 어떤 기능도 없다. 그냥 서로에게 주는 싸인일 뿐이다.
- 여하튼 앞으로 ***캡슐화르 할 땐 언더바 하나를 앞에 붙이자***. 결론!

#### @property, @age.setter
- 클래스에 _age라는 변수가 있다 치자.
- 이 변수는 캡슐화되어 외부에서 접근하지 말라는 뜻을 담고 있다.
- 이 변수의 getter, setter 메서드를 @property, @age.setter를 통해 만들 수 있다.
![](https://images.velog.io/images/kpl5672/post/e4f20b8c-be9b-4024-9c1b-2e87846f275d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-12%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.34.30.png)
- 이 데코레이터를 통해 실제 _age를 사용할 때 age라고 쓰면서 사용할 수 있다.
- 예시 코드에서 `print(young.age)` 이 실행되면 데코레이터에 덕에 @property가 달려있는 age 메서드(getter)가 실행된다.
- 예시 코드에서 `young.age = 30`이 실행되면 데코레이터 덕에 @age.setter가 자동으로 실행된다.
- 즉, _변수명의 변수가 있을 경우 변수명으로 함수를 만들고 그 위에 @property, @변수명.setter를 만들어주면 된다.

#### 객체를 사용할 땐 최대한 메소드로
- 변수에 직접 접근하는 코드가 많을수록 유지보수 하기가 어렵다.
- 메서드로 변수에 접근하고, 그 메서드를 다른데서 가져가 쓰는 것이 제일 좋다.

## Chapter 3: 상속(Inheritance)
### 1) 상속이란?
- 두 클래스 사이에 부모-자식 관계를 설정하는 것.
- 벤츠-자동차 관계에서 벤츠는 자동차지만 자동차는 벤츠가 아니다. 
- 자동차는 벤츠의 부모다. 
- 벤츠는 자동차를 상속받는다.
- 상속은 반복을 줄여준다.

### 2) mro, isinstance, issubclass 함수
#### mro(Method resolution order)
- mro함수는 어떤 클래스의 상속 관계를 보여준다.
- 아래 결과를 보면 Son -> Mom -> object로 가는 상속 관계를 보여준다.
- object는 보다시피 모든 클래스의 조상이다.
- 참고로 help(class_name)으로도 상속 관계를 볼 수 있다.
```
class Mom:
    pass


class Son(Mom):
    pass

print(Son.mro())

결과값:
[<class '__main__.Son'>, <class '__main__.Mom'>, <class 'object'>]
```

#### isinstance
- 이 함수는 어떤 인스턴스가 주어진 클래스의 인스턴스인지 알려준다.
- 첫 파라미터로 검사할 인스턴스 이름, 
- 두 번째 파라미터로 기준 클래스의 이름을 넘겨준다.을
- 리턴값은 Boolean
```
class Mom:
    pass


class Son(Mom):
    pass


son = Son()

print(isinstance(son, Mom))
print(isinstance(son, object))
print(isinstance(son, list))

결과값:
True
True
False
```
#### issubclass
- 어떤 클래스가 다른 클래스의 자식 클래스인지 알려주는 함수다.
- 첫 번째 파라미터로 검사할 클래스의 이름을,
- 두 번째 파라미터로 기준이 되는 클래스의 이름을 넘겨준다.
- 리턴값은 Boolean
```
class Mom:
    pass


class Son(Mom):
    pass


son = Son()

print(issubclass(Son, Mom))
print(issubclass(Son, object))
print(issubclass(Son, list))

결과값:
True
True
False
```
### 3) overring
- 부모의 변수를 오버라이드 하려면 똑같은 변수명으로 오버라이드 하면 된다. (아래의 DeliveryMan의 raise_percentage처럼)
- super().`__init__`(똑같은 인자 념겨주기)로 상속을 명시할 수 있다. (이렇게 안해도 자동으로 상속은 된다.)

```
class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage


class DeliveryMan(Employee):
    """배달원 클래스"""
    raise_percentage = 1.1

    def __init__(self, name, wage, on_standby):
        super().__init__(name, wage)
        self.on_standby = on_standby

```
#### 상속의 원리
- 부모와 자식이 같은 이름의 메서드를 갖고 있다면 mro에서 제일 빠른 순번의 것이 먼저 호출된다.
- 즉 자식에서 오버라이딩 한 메서드가 호출된다. 이런 원리를 통해서 오버라이딩이 가능한 것이다.

### 4) 다중상속
#### 파이썬은 다중상속이 가능하다 (Java같은 언어는 상속 딱 하나만 가능)
#### 방법
- 아래 예시의 C 클래스는 A, B를 다중상속 받았다.
```
class A:
    def __init__(self, a):
        self.a = a


class B:
    def __init__(self, b):
        self.b = b


class C(A, B):
```
- 그런데 만약 C에서 `super().__init__`을 실행하면 A, B 중 어떤 클래스의 메서드가 실행되는 걸까?
- 이런 점이 모호 하기 때문에 다중상속의 경우 super대신 부모 클래스의 이름을 명시해주거나 메소드 자체를 오버라이드 한다.
- 부모 클래스의 이름을 명시해주는 예제
```
class C(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)

```
- 메소드 오버라이드 하는 예시
```
class C(A, B):
    def __init__(self, a, b):
        self.a = a
        self.b = b

```
- 다중상속은 위험한 면이 있다. 그래서 어떤 언어들은 다중상속 자체를 지원 안한다.
- 이런 위험성을 해결하기 위해 아래 두가지 솔루션을 제시한다.
#### 다중상속 문제 해결 솔루션
- 부모클래스끼리 같은 이름의 메소드 갖지 않기
- 같은 이름의 메소드는 자식클래스에서 오라이딩

## Chapter 4: 다형성(Polymorphism)

# Unit 3: 견고한 객체 지향 프로그래밍: SOLID 원칙
## 목차 
- Chapter 1: 단일 책임 원칙 (Single Responsibility Principle)
- Chapter 2: 개방 폐쇄 원칙 (Open-closed Principle)
- Chapter 3: 리스코프 치환 원칙 (Liskov Substitution Principle)
- Chapter 4: 인터페이스 분리 원칙 (Interface Segregation Principle)
- Chapter 5: 의존 관계 역전 원칙 (Dependency Inversion Principle)차

## 개요
- SOLID원칙은 Robert C. Martin이라는 유명한 개발자가 2000년도에 처음 소개한 객체 설계의 기본 원칙이다.
- 객체 지향 프로그래밍에서 사실상 표준 규칙처럼 알려져 있다.
## Chapter 1: 단일 책임 원칙 (Single Responsibility Principle)
#### 정의: 모든 클래스는 단 한가지의 책임만 갖고, 클래스 안에 정의되어 있는 모든 기능은 이 하나의 책임을 수행하는데 집중되어 있어야 한다.
- 하나의 클래스로 너무 많은 일을 하지 말라는 뜻임.
- 물론 어디까지가 한 가지 책임이라고 할 수 있는지는, 사람들마다 생각이 다르고, 상황에 따라서도 다르다.
- 같이 수정해야 할 것들은 묶고, 따로 수정해야 하는 것들은 분리하기.
- 중요한 것은 코드를 작성할 때, 내가 단일 책임 원칙을 지키고 있는지 신경쓰는 것
- 너무 많은 기능을 수행하는 클래스는 GOD Object라고 하기도 한다(물론 안좋은 뜻이다.)
- 아래 Ship클래스가 그 예시다. 연료, 물자, 선원, 엔진 이 모든 것을 책임지는 클래스다보니 너무 크고 유지보수가 어렵다.
```
class Ship:
    """배 클래스"""
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        """연료량, 시간당 연료 소비량, 물자량, 선원 수를 인스턴스 변수로 갖는다"""
        self.fuel = fuel
        self.fuel_per_hour = fuel_per_hour
        self.supplies = supplies
        self.num_crew = num_crew

    def report_fuel(self):
        """연료량 보고 메소드"""
        print("현재 연료는 {}l 남아 있습니다".format(self.fuel))

    def load_fuel(self, amount):
        """연료 충전 메소드"""
        self.fuel += amount

    def report_supplies(self):
        """물자량 보고 메소드"""
        print("현재 물자는 {}명분이 남아 있습니다".format(self.supplies))

    def load_supplies(self, amount):
        """물자 보급 메소드"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """물자 배분 메소드"""
        if self.supplies >= self.num_crew:
            self.supplies -= self.num_crew
            return True
        print("물자가 부족하기 때문에 배분할 수 없습니다")
        return False

    def report_crew(self):
        """선원 수 보고 메소드"""
        print("현재 선원 {}명이 있습니다".format(self.num_crew))

    def load_crew(self, number):
        """선원 승선 메소드"""
        self.num_crew += number

    def run_engine_for_hours(self, hours):
        """엔진 작동 메소드"""
        if self.fuel > self.fuel_per_hour * hours:
            self.fuel -= self.fuel_per_hour * hours
            print("엔진을 {}시간 동안 돌립니다!".format(hours))
        else:
            print("연료가 부족하기 때문에 엔진 작동을 시작할 수 없습니다")
```
- 위 클래스는 연료, 선원, 물자, 엔진 총 4가지 클래스로 분리해보자.
```
class Ship:
    """배 클래스"""
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        self.fuel_tank = FuelTank(fuel)
        self.crew_manager = CrewManager(num_crew)
        self.supply_hold = SupplyHold(supplies, self.crew_manager)
        self.engine = Engine(self.fuel_tank, fuel_per_hour)


class FuelTank:
    """연료 탱크 클래스"""
    def __init__(self, fuel):
        """연료 탱크에 저장된 연료량을 인스턴스 변수로 갖는다"""
        self.fuel = fuel

    def load_fuel(self, amount):
        """연료 충전 메소드"""
        self.fuel += amount

    def use_fuel(self, amount):
        """연료 사용 메소드"""
        if self.fuel - amount >= 0:
            self.fuel -= amount
            return True
        print("연료가 부족합니다!")
        return False

    def report_fuel(self):
        """연료량 보고 메소드"""
        print("현재 연료는 {}l 남아 있습니다".format(self.fuel))


class Engine:
    """엔진 클래스"""
    def __init__(self, fuel_tank, fuel_per_hour):
        """연료 탱크 인스턴스와 시간당 연료 소비량을 인스턴스 변수로 갖는다"""
        self.fuel_tank = fuel_tank
        self.fuel_per_hour = fuel_per_hour

    def run_for_hours(self, hours):
        """엔진 작동 메소드, 연료 탱크 인스턴스를 사용한다"""
        if self.fuel_tank.use_fuel(self.fuel_per_hour * hours):
            print("엔진을 {}시간 동안 돌립니다!".format(hours))
            return True
        print("연료가 부족하기 때문에 엔진 작동을 시작할 수 없습니다")
        return False


class CrewManager:
    """선원 관리 클래스"""
    def __init__(self, num_crew):
        """승선한 선원 수를 인스턴스 변수로 갖는다"""
        self.num_crew = num_crew

    def load_crew(self, number):
        """선원 승선 메소드"""
        self.num_crew += number

    def report_crew(self):
        """선원 수 보고 메소드"""
        print("현재 선원 {}명이 있습니다".format(self.num_crew))


class SupplyHold:
    """물자 창고 클래스"""
    def __init__(self, supplies, crew_manager):
        """물자량과 선원 관리 인스턴스를 인스턴스 변수로 갖는다"""
        self.supplies = supplies
        self.crew_manager = crew_manager

    def load_supplies(self, amount):
        """물자 충전 메소드"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """물자 배분 메소드, 각 선원들에게 동일한 양의 물자를 배분한다"""
        if self.supplies >= self.crew_manager.num_crew:
            self.supplies -= self.crew_manager.num_crew
            return True
        print("물자가 부족하기 때문에 배분할 수 없습니다")
        return False

    def report_supplies(self):
        """물자량 보고 메소드"""
        print("현재 물자는 {}명분이 남아 있습니다".format(self.supplies))
```
## Chapter 2: 개방 폐쇄 원칙 (Open-closed Principle)
#### 정의: 클래스는 확장에 열려 있어야하며, 수정에는 닫혀 있어야한다.
- 확장에 열리다: 기존 기능을 확장할 수 있어야 함.
- 수정에 닫히다: 한 번 작성한 코드를 바꾸지 않아도 되야함.
- 어떤 클래스의 코드를 수정하지 않아도 기존 기능을 확장할 수 있어야 한다.
- 이를 위해 추상 클래스와 추상 메서드를 정의하고 이를 상속받게 해서 사용하는 것이 좋다.
## Chapter 3: 리스코프 치환 원칙 (Liskov Substitution Principle)
- 이 챕터의 결론: ***부모 클래스의 행동 규약을 준수하는 자식 클래스를 만들자!***
  - 메서드 파라미터 타입과 개수, 리턴값의 타입과 개수, 변수의 타입과 개수를 일치시키자.
- 컴퓨터 과학자 Barbara Liskov의 이름을 따서 만들어진 법칙.
- 부모 클래스의 인스턴스를 사용하는 위치에 자식 클래스의 인스턴스를 대신 사용했을 때 코드가 원래 의도대로 작동해야 한다.
- 이 말이 무슨 말일까?
- 자식 클래스의 인스턴스는 부모 클래스의 인스턴스이기도 하기 때문에, isinstance(자식클래스 인스턴스, 부모 클래스)에 넣으면 True가 리턴된다.
- 자식 클래스가 부모 클래스의 행동 규약을 어기면 안된다는 법칙이다.
- 그렇다면 자식 클래스가 부모 클래스 행동 규약을 어긴다는 것은 구체적으로 무슨 뜻일까?
- 자식 클래스가 부모 클래스의 변수와 메소드를 잘못 오버라이딩 하면 이런 문제가 발생한다.
- 잘못 오버라이딩 한다는 것은 아래 두가지의 경우다.
  - (1) 자식 클래스가 부모 클래스의 변수 타입을 바꾸거나 메소드의 파라미터 또는 리턴값이 타입 or 갯수를 바꾸는 경우
  - (2) 자식 클래스가 부모 클래스의 의도와 다르게 메소드를 오버라이딩 하는 경우
  
####  자식 클래스가 부모 클래스의 변수 타입을 바꾸거나 메소드의 파라미터 또는 리턴값이 타입 or 갯수를 바꾸는 경우
- 부모 Employee클래스의 raise_pay 메서드는 파라미터를 받지 않고, wage메서드는 숫자를 리턴하는 반면,<br>
 자식 Cashier클래스는 raise_pay메서드에 파라미터를 하나 추가로 받고, wage메서드에서 str을 리턴한다.
 이게 잘못된 예시이다.
```
class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    """리스코프 치환 원칙을 지키지 않는 계산대 직원 클래스"""
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def raise_pay(self, raise_amount):
        """직원 시급을 인상하는 메소드"""
        self.wage += self.raise_amount

    @property
    def wage(self):
        return "시급 정보를 알려줄 수 없습니다"

```
#### 자식 클래스가 부모 클래스의 의도와 다르게 메소드를 오버라이딩 하는 경우
- sqaure 클래스의 width, height메서드는 부모 클래스와 다르게 작동한다.
- 사실 정사각형은 직사각형의 행동 규약을 따르기 어렵기 때문에 애초에 상속을 안하는게 맞다.
- 아래 코드를 옳게 고칠 땐 상속 관계를 제거한다.
```
class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        """세로와 가로"""
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산 메소드"""
        return self.width * self.height

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._height = value if value > 0 else 1


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1
```

## Chapter 4: 인터페이스 분리 원칙 (Interface Segregation Principle)
### 1. 인터페이스란?
- 추상 클래스 중에서 추상 메소드만 있고 일반 메소드는 없는 것을 인터페이스라 부른다.
- 파이썬에는 없는 개념.
- 클래스가 사용하지 않을 메소드에 의존할 것을 강요하면 안 된다. = 클래스가 나중에 사용하지도 않을 메소드를 가지도록 강제하지 말라는 
- 이미 공부했다시피 추상클래스를 상속받으면 자식 클래스는 추상 메소드들을 반드시 오버라이딩해야 한다.
- 어떤 인터페이스(추상 클래스)를 상속받았을 때 사용하지 않을 메서드가 있다면 인터페이스 분리 원칙 위반이다.
- 인터페이스 분리 원칙을 위반하지 않기 위해서는 인터페이스를 작게 분리해야 한다. (뚱뚱한 인터페이스를 만들지 말자.)
- ***인터페이스를 정의할 땐 항상 더 작게 쪼갤 수 있을지 고민해야 한다.***
- 그렇다고 인터페이스 하나당 메서드 하나만 있을 정도로 잘게 쪼개라는 것은 아니다.
- 같은 기능이나 역할로 묶어서 인터페이스를 잘 만들어야 한다.
<img width="689" alt="스크린샷 2021-04-17 오후 5 51 02" src="https://user-images.githubusercontent.com/70195733/115107378-871a4c80-9fa5-11eb-8971-1c249af91d55.png">
- 아래 코드에서 IMessage를 상속받는 Memo 클래스가 생긴다고 해보자.
- 메모는 Email, TextMessage클래스들과 달리 send기능이 없어야 하는데 IMessage를 상속받았다는 이유로 send메서드를 꼭 갖게 된다.
- 이게 바로 인터페이스 분리 원칙 위반이다.
- 이를 해결하기 위해 IMessage인터페이스를 IText(content, edit_content 메서드 소유)와 ISendable(send메서드 소유)로 분리하고, 메모는 IText만 상속받게 한다.
```
from abc import ABC, abstractmethod


class IMessage(ABC):
    @property
    @abstractmethod
    def content(self):
        """추상 getter 메소드"""
        pass

    @abstractmethod
    def edit_content(self, new_content: str) -> None:
        """작성한 메시지를 수정하는 메소드"""
        pass

    @abstractmethod
    def send(self, destination: str) -> bool:
        """작성한 메시지를 전송하는 메소드"""
        pass


class Email(IMessage):
    def __init__(self, content, owner_email):
        """이메일은 그 내용과 보낸 사람의 이메일 주소를 인스턴스 변수로 가짐"""
        self._content = content
        self.owner_email = owner_email

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """이메일 내용 수정 메소드"""
        self._content = self.owner_email + "님의 메일\n" + new_content

    def send(self, destination):
        """이메일 전송 메소드"""
        print("{}에서 {}로 이메일 전송!\n내용: {}").format(self.owner_email, destination, self._content)
        return True


class TextMessage(IMessage):
    def __init__(self, content):
        """문자 메시지는 그 내용을 인스턴스 변수로 가짐"""
        self._content = content

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """문자 메시지 내용 수정 메소드"""
        self._content = new_content

    def send(self, destination):
        """문자 메시지 전송 메소드"""
        print("{}로 문자 메시지 전송!\n내용: {}").format(destination, self._content)


class TextReader:
    """인스턴스의 텍스트 내용을 읽어주는 클래스"""

    def __init__(self):
        self.texts = []

    def add_text(self, text: IMessage):
        """인스턴스 추가 메소드, 파라미터는 IMessage 인터페이스를 상속받을 것"""
        self.texts.append(text)

    def read_all_texts(self):
        """인스턴스 안에 있는 모든 텍스트 내용 출력"""
        for text in self.texts:
            print(text.content)
```
## Chapter 5: 의존 관계 역전 원칙 (Dependency Inversion Principle)
#### 정의
- 상위 모듈은 하위 모듈의 구현 내용에 의존하면 안 된다.
- 상위 모듈과 하위 모듈 모두 추상화된 내용에 의존해야 한다.
- 두 클래스 A, B가 있을 때 A가 B를 사용하면 A는 상위모듈, B는 하위모듈이다.
- 아래 코드에서 GameCharacter의 attack메소드가 Sword클래스를 사용하므로 GameCharacter는 상위 모듈, Sword클래스는 하위모듈이다.
- 그리고 아래 코드는 의존 관계 역전 원칙을 위반했는데 이유는 attack에서 sowrd의 slash메소드를 의존하기 떄문이다.
- 만약 Sword의 slash메소드의 이름이 do_slash로 바뀐다 치면 상위 모듈의 attack메소드는 정상실행되지 않고, 똑같이 내용을 바꿔줘야 한다.
<img width="871" alt="스크린샷 2021-04-17 오후 6 23 37" src="https://user-images.githubusercontent.com/70195733/115108243-4f61d380-9faa-11eb-8e0d-f48bff392ee3.png">
```
이에 대한 해결책은  추상 클래스로 상위 모듈과 하위 모듈 사이에 추상화 레이어를 만드는 것입니다. 이렇게 되면
1. 상위 모듈에는 추상 클래스의 자식 클래스의 인스턴스를 사용한다는 가정 하에 그 하위 모듈을 사용하는 코드를 작성해두면 되고,
2. 하위 모듈은 추상 클래스의 추상 메소드들을 구현(오버라이딩)만 하면 됩니다.
```

```
class Sword:
    """검 클래스"""
    def __init__(self, damage):
        self.damage = damage

    def slash(self, other_character):
        """검 사용 메소드"""
        other_character.get_damage(self.damage)


class GameCharacter:
    """게임 캐릭터 클래스"""
    def __init__(self, name, hp, sword: Sword):
        self.name = name
        self.hp = hp
        self.sword = sword

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.sword.slash(other_character)
`        else:
`            print(self.name + "님은 사망해서 공격할 수 없습니다.")

    def change_sword(self, new_sword):
        """검을 바꾸는 메소드"""
        self.sword = new_sword

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 사망했습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        """남은 체력을 문자열로 리턴하는 메소드"""
        return self.name + "님은 hp: {}이(가) 남았습니다.".format(self.hp)

```
- 위 문제에 대한 해결책으로 IWeapon이라는 인터페이스를 만들고 Sword 클래스가 이것을 상속받게 한다.

<img width="343" alt="스크린샷 2021-04-17 오후 6 33 03" src="https://user-images.githubusercontent.com/70195733/115108429-5ccb8d80-9fab-11eb-84ca-25fde83d74f7.png">