# 간단한 예제를 통해 깃허브 액션을 알아봅시다.
#### 1. 우선 깃 레포에서 action -> set up a workflow yourself를 클릭합니다.

<img width="1625" alt="스크린샷 2021-05-11 오전 9 37 08" src="https://user-images.githubusercontent.com/70195733/117741146-b0449a80-b23c-11eb-84e2-f41d499e1c28.png">

- 깃허브 엑션에는  파이썬, AWS ECS, Terraform, Ruby, Go 등등 많은 템플릿들이 존재합니다.
- 여기선 간단한 예제를 통해 github action을 사용하는 게 목표이므로 set up a workflow yourself를 통해 사용해보겠습니다.

#### 2. yml파일 만들기
- set up a workflow yourself를 클릭하면 아래의 yml파일 내용이 나옵니다. 하나 하나씩 살펴봅시다.
- name: 원하는 이름을 적어주면 됩니다. (문법적으로 중요한 것은 아님)
- on: trigger를 설정하는 부분입니다. 특정 브랜치에서 push혹은 pr같은 일이 생겼을 때 github_action이 작동하게끔 설정합니다.
- runs-on: githubaction은 말하자면 github에서 컴퓨터를 빌려주고, 그 컴퓨터 위에서 돌아가는 식입니다. runs-on은 컴퓨터의 운영체제를 선택하는 부분입니다.
- steps: 이 안에 이제 실제로 원하는 것들을 정의해줍니다.
- uses: 다른 사람이 만든 action을 사용할 때 적는 것입니다. aws 이미지 고르는 것처럼(제가 이해하기로는) 마켓에서 다른 사람들의 actions를 가져다 쓸 수 있습니다. <br>
runner를 만들면 기본적으로 깡통처럼 빈 상태입니다. `actions/checkout@v2`는 내 프로젝트를 클론하고 거기로 checkout합니다. 말하자면 프로젝트의 루트 디렉토리에서 runner가 실행되는 것입니다.<br>
- name: 원하는 이름을 적어줍니다.(아무거나)
- run: 실제 실행할 명령어를 적어줍니다. `echo`는 파이썬의 print 문과 같습니다.
```
name: action test

on:
  push:
    branches: [ main ]
#   pull_request:
#     branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Run a one-line script
        run: echo Hello, world!

      - name: Run a multi-line script
        run: |
          echo Add other actions to build,
          echo test, and deploy your project.
      
      - name: test ls -al gogo
        run: ls -al
```

#### 3. 위 파일을 커밋하고 실제 action이 실행된 결과물을 봅시다.
<img width="933" alt="스크린샷 2021-05-11 오전 10 05 06" src="https://user-images.githubusercontent.com/60768642/117742802-783f5680-b240-11eb-8f44-0dd185585746.png">
- yml파일에서 정의했던 4개의 run이 실행된 것을 볼 수있습니다.
- 마지막에 ls -al을 한 결과로 프로젝트 루트 디렉토리의 파일들이 출력됐습니다. 이게 가능한 이유는 uses: actions/checkout@v2 명령어를 썼기 떄문입니다.

#### 4. SECRET 환경변수를 저장하고 출력하는 방법에 대해 알아봅시다.
- secret key는 보안상 소스코드에 하드코딩을 하면 안됩니다.
- github action을 사용하다보면 secret key가 필요할 때가 있을탠데 이때 yml파일에 하드코딩 하지 말고, 안전하게 github secret을 사용하면 됩니다.
1. settings -> Secrets -> New repository secret 클릭
<img width="1490" alt="스크린샷 2021-05-11 오전 10 08 38" src="https://user-images.githubusercontent.com/60768642/117743121-221ee300-b241-11eb-85bf-306f407a94a7.png">
2. key-value 형태로 값을 입력. 예제에서는 MY_SUPER_SECURE_SECRET의 값으로 1234를 입력했습니다.
<img width="519" alt="스크린샷 2021-05-11 오전 10 08 52" src="https://user-images.githubusercontent.com/60768642/117743132-25b26a00-b241-11eb-9647-352311ba4966.png">
3. 새로운 secret이 생성된 것을 볼 수 있습니다.
<img width="1336" alt="스크린샷 2021-05-11 오전 10 09 03" src="https://user-images.githubusercontent.com/60768642/117743134-25b26a00-b241-11eb-9234-e24630c30e4c.png">

- 이제 새로운 yml파일을 정의해서 github_action에서 방금 만든 secret 값을 사용해봅시다.
```
name: CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: print secret
        env:
          WEIRD_PASSWORD: ${{ secrets.MY_SUPER_SECURE_SECRET}}
        run: echo my secret is $WEIRD_PASSWORD
```
<img width="1769" alt="스크린샷 2021-05-11 오전 10 17 50" src="https://user-images.githubusercontent.com/60768642/117743771-68287680-b242-11eb-9590-8d2cbf27b3b9.png">

- 결과 화면은 아래와 같습니다. 깃허브 자체에서 secrets 출력시도가 들어오면 별표처리합니다.

<img width="451" alt="스크린샷 2021-05-11 오전 10 20 35" src="https://user-images.githubusercontent.com/60768642/117743898-aa51b800-b242-11eb-87ab-4902fce33a53.png">
