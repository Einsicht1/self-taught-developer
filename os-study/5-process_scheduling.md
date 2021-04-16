# 1. Process Scheduling
## 목차
- 스케줄링의 목적
- 스케줄링 기준 및 단계
- 스케줄링 정책
- 기본 스케줄링 알고리즘들
- case study

## 1. 스케줄링의 목적
### 1) 다중 프로그래밍(multi-programming)
- 여러 개의 포르세스가 시스템 내에 존재
- 자원을 할당할 프로세스를 선택해야 함. -> 이것이 곧 스케줄링
#### 자원 관리
- 시간 분할(time sharing) 관리
  - 하나의 자원을 여러 스레드들이 번갈아가며 사용
  - 예) Processor
  - ***프로세스 스케줄링***
    - 프로세서 사용시간을 프로세스들에게 분배
- 공간 분할(space sharing) 관리
  - 하나의 자원을 분할하여 동시에 사용
  - 예) 메모리(memory)

### 2) 스케줄링의 목적
- : 시스템 성능(performance) 향상
- 대표적 시스템 성능 지표(index) (뭐를 성능이라고 할 수 있는가)
  - 응답 시간(response time)
    - 작업 요청(submission)으로부터 응답을 받을때까지의 시간
  - 작업 처리량(throughput)
    - 단위 시간 동안 완료된 작업의 수
  - 자원 활용도(resource utilization)
    - 주어진 시간동안 자원이 활용된 시간
- 목적에 맞는 지표를 고려하여 스케줄링 기법을 선택해야 한다.

### 3) 대기시간, 응답시간, 반환시간
![스크린샷 2021-04-16 오후 10 10 29](https://user-images.githubusercontent.com/70195733/115029084-92676c80-9f00-11eb-89ef-28703ac3a97a.png)

## 2. 스케줄링 기준(Criteria) 및 단계
### 1) 개요
: 스케줄링 기법이 고려하는 항목들을 살펴보는 챕터
- 프로세스 특성
  - I/O -bounded or compute-bounded
- 시스템 특성
  - batch system or interactive system
- 프로세스의 긴급성(urgency)
  - Hard, soft, non real time system
- 프로세스 우선순위(priority)
- 프로세스 총 실행 시간(total service time)
- 등등.....

### 2) CPU burst vs I/O burst
- 프로세스 수행은 CPU 사용 + I/O 대기로 이루어진다.
- cpu작업 -> I/O 대기 -> cpu 작업 -> I/O대기 ...무한반복
- CPU burst란?
  - CPU 사용 단계
- I/O burst란?
  - I/O 대기 단계
- Burst time은 스케줄링의 중요한 기준 중 하나이다.

### 3) 스케줄링의 단계(Level)
- 스케줄링 단계란 발생하는 빈도 및 할당 자원에 따른 구분으로 총 3가지로 나뉜다.
  - Long-term scheduling
    - Job scheduling
  - Mid-term scheduling
    - Memory allocation
  - Short-term scheduling 
    - Process scheduling

#### Long-term scheduling
- Job scheduling이다.
  - 시스템에 제출할(kernel에 등록할) 작업(Job) 결정
    - Admission scheduling, High-level scheduling
- 다중 프로그래밍 정도(degree) 결정
  - 시스템 내에 프로세스 수 조절
- I/O-bounded와 compute-bounded프로세스들을 잘 섞어서 선택해야 함.
  - 이유는? 둘중 하나에 작업이 너무 몰리면 나머지 하나는 너무 놀게됨
- 시분할 시스템에서는 모든 작업을 시스템에 등록하기 때문에 long-term 스케줄링이 별로 안중요하다.
![스크린샷 2021-04-16 오후 10 20 34](https://user-images.githubusercontent.com/70195733/115030373-fd657300-9f01-11eb-8eff-be553d835760.png)
#### Mid-term scheduling
- 메모리 할당 결정(memory allocation)
  - Intermediate-level scheduling
  - Swapping (swap-in/swap-out)
![스크린샷 2021-04-16 오후 10 21 39](https://user-images.githubusercontent.com/70195733/115030510-2128b900-9f02-11eb-8cab-f4c40aa7ba04.png)
#### Short-term scheduling 
- Process scheduling
  - Low-level scheduling
  - Processor를 할당할 process를 결정
    - Processor scheduler, dispatcher
- 가장 빈번하게 발생
  - Interrupt, block(I/O), time-out, Etc.
  - 매우 빨라야 한다.
  ![스크린샷 2021-04-16 오후 10 22 58](https://user-images.githubusercontent.com/70195733/115030674-50d7c100-9f02-11eb-8b61-8be494645902.png)
![스크린샷 2021-04-16 오후 10 23 27](https://user-images.githubusercontent.com/70195733/115030736-6351fa80-9f02-11eb-8092-a2cb3889726d.png)
## 3. 스케줄링 정책
- 선점(Preemptive) vs 비선점(Non-preemptive)
- 우선순위(Priority)
###  선점(Preemptive) vs 비선점(Non-preemptive)
#### Non-preemptive scheduling
- 할당 받은 자원을 스스로 반납할 때까지 사용
  - 예) system call  I/O, Etc.
- 장점
  - context switch overhead가 적음
- 단점
  - 잦은 우선순위 역전, 평균 응답 시간 증가
#### Preemptive scheduling
- 다른 작업에 의해 자원을 뺏길 수 있음
  - 예) 할다 ㅇ시간 종료, 우선순위가 높은 프로세스 등장
- context swtich overhead가 큼
- Time-sharing, real-time system에 적합

### Priority
- : 프로세스의 중요도
#### Static priority(정적 우선순위)
- 프로세스 생성시 결정된 우선순위가 계속 유지됨.
- 구현이 쉽고 overhead가 적음
- 시스템 환경 변화에 대한 대응이 어려움
#### Dynamic priority(동적 우선순위)
- 프로세스의 상태 변화에 따라 priority 변경
- 구현이 복잡, priority 재계산 overhead가 큼
- 시스템 환경 변화에 유연한 대응 가능.

## 요약
![스크린샷 2021-04-16 오후 10 31 22](https://user-images.githubusercontent.com/70195733/115031762-7f09d080-9f03-11eb-8141-2810ae67e077.png)
## 4. 기본 스케줄링 알고리즘들
- FCFS(First-Come-First-Service)
- RR(Round-Robin)
- SPN(Shortest-Process-Next)
- SRTN(Shortest-Ramining time Next)
- HRRN(High-Response-Ratio Next)
- MLQ (Multi-level Queue)
- MFQ (multi-level Feedback Queue)

### FCFS(First-Come-First-Service)
- Non-preemptive scheduling
- scheduling criteria(기준)
  - ***도착 시간*** (ready queue 기준) 
  - 먼저 도착한 프로세스를 먼저 처리
- 자원을 효율적으로 사용 가능
- Batch system에 적합, interactive system에 부적함
- 단점
  - convoy effect
    - 하나의 수행시간이 긴 프로세스에 의해 뒤에 들어온 다른 프로세스들이 긴 대기시간을 갖게 되는 현상(대기시간 > 실행 시간)
  - 긴 평균 응답시간(response time)
![스크린샷 2021-04-16 오후 10 48 18](https://user-images.githubusercontent.com/70195733/115033847-da3cc280-9f05-11eb-9797-1210027d1316.png)
### RR(Round-Robin)
- Preemptive scheduling
- scheduling criteria
  - ***도착시간*** (ready queue 기준)
  - 먼저 도착한 프로세스를 먼저 처리
- 자원 사용 제한 시간(time quantum)이 있음
  - System parameter
  - 프로세스는 할당된 시간이 지나면 자원 반납(timer-runout)
  - 특정 프로세스의 자원 monopoly 방지
  - context switch overhead가 큼
  - 대화형, 시분할 시스템에 적합
#### Time quantum
- 시스템 성능을 결정하는 핵심 요소
- 한 텀에 주어지는 시간을 의미
- 너무 크면? -> 사실상 FCFS가 된다.
- 너무 작으면? -> processor sharing이 된다.
  - 사용자는 모든 프로세스가 각각의 프로세서 위에서 실행되는 것처럼 느낀다.
    - 첵마 프로세서 속도 - 실제 프로세서 성능의 1/n
  - High context switch overhead
![스크린샷 2021-04-16 오후 10 52 55](https://user-images.githubusercontent.com/70195733/115034468-8088c800-9f06-11eb-99a9-0036823df881.png)
  
  

### SPN(Shortest-Process-Next)
### SRTN(Shortest-Ramining time Next)
### HRRN(High-Response-Ratio Next)
### MLQ (Multi-level Queue)
### MFQ (multi-level Feedback Queue)
## 5. case study
