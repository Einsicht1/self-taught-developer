# 1. 운영체제의 역할
#### 1) User Interface(편리성)
- CUI(Character user interface)
- GUI(Graphical User interface)
- EUCI(End-User comfortable Interface)

#### 2) Resource management(효율성)
- HW Resource(processor, memory, I/O devices, Etc.)
- SW Resource(file, application, message, signal, Etc.)

#### 3) Process and Thread management
#### 4) System management(시스템 보호)
컴퓨터 시스템의 구성
![](https://images.velog.io/images/kpl5672/post/b6ca966e-bc69-441e-be11-37181ac28448/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.27.45.png)
- 커널이 운영체제의 핵심
- 운영체제는 하드위에 위층에 있음
- 유저는 system call Interface를 통해 운영체제와 교류
![](https://images.velog.io/images/kpl5672/post/44719e2f-efb4-4281-8ba8-d132c95c4382/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.29.22.png)
# 2. 운영체제의 구분
#### 1) 동시 사용자 수
- Single-user system
- multi-user system
#### 2) 동시 실행 프로세스 수
- single-tasking system
- multi-tsaking system(Multiprogramming system)
#### 3) 작업 수행 방식(사용자가 느끼는 사용 환경)
- Batch processing system
- Time-sharing system
- Distributed processing system
- Real-time system

### <동시 사용자 수>
#### 단일 사용자(single-user system)
-한 명의 사용자만 시스템 사용 가능
  - 한 명의 사용자가 모든 시스템 자원 독점
  - 자원관리 및 시스템 보호 방식이 간단
- 개인용 장비(PC, mobile)등에 사용
  - Windows, android, MS-DOS 등

#### 다중 사용자
- 동시에 여러 사용자들이 시스템 사용
  - 각종 시스템 자원(파일 등)에 대한 소유 권한 관리 필요
  - 기본적으로 multi-tasking 기능 필요
  - OS 기능 및 구조가 복잡
- 서버, 클러스터(cluster)장비 등에 사용
  - Unix, Linux, Windows server 등

### <동시 실행 프로세스 수>
#### 단일작업(Single-tasking system)
- 시스템 내에 하나의 작업(프로세스)만 존재
  - 하나의 프로그램 실행을 마친 뒤에 다른 프로그램의 실행
  - 운영체제 구조 간단
  - 예) MS-DOS
#### 다중작업(Multi-tasking system)
- 동시에 여러 작업(프로세스)의 수행 가능
  - 작업들 사이의 동시 수행, 동기화 등을 관리해야 함
- 운영체제의 기능 및 구조가 복잡
- 예) Unix/Linux, Windows 등

### <작업 수행 방식>
- Batch processing system(일괄 처리 시스템)
- Time-sharing system(시분할 시스템)
- Distributed processing system(분산 처리 시스템)
- Real-time system(실시간 시스템)

#### 아주 옛날 os가 없던 시절에는 순차 처리 사용했다(~1940s)
- 운영체제 개념 x
- 사용자가 기계어로 직접 프로그램 작성
- 각 작업을 순차적으로 처리함
- 단점: 각 작업에 대한 준비 시간 소요
- 예를 들어 (정말 예일 뿐임) 1번 작업은 java면 java를 위한 준비를 해야됨.<br>
그 후 python작업이 2번이면 이것에 대한 작업을 또 해야됨. 
- 이런 단점을 보안하고자 나온 것이 batch system

#### Batch processing system(일괄 처리 시스템, 1950s~1960s)
- 모든 시스템을 중앙(전사계산소 등)에서 관리 및 운영
- 사용자의 요청 작업(천공카드 등)을 일정 시간 모아 두었다가 한번에 처리
- 시스템 지향적(systme-oriented, 시스템에게 유리한, 유저에게 불리한)
- 장점
  - 많은 사용자가 시스템 자원 공유
  - 처리 효율(throughput)향상
-단점
  - 생산성(productivity) 저하
    - 같은 유형의 작업들이 모이기를 기다려야 함
  - 긴 응답시간(turnaround time)
    - 약 6시간(작업 제출에서 결과 출력까지의 시간)
![](https://images.velog.io/images/kpl5672/post/9d79d39e-0b41-4b29-b28b-f969eb86bb1d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.41.08.png)
#### Time-sharing system(시분할 시스템, 1960s~1970s)
- 여러 사용자가 자원을 동시에 사용
  - OS가 파일 시스템 및 가상 메모리 관리
- 사용자 지향적(User-oriented)
  - 대화형(conversational, interacitve) 시스템 (사용자 입장에서 그렇게 느낌)
  - 단말기(CRT terminal) 사용
- 장점
  - 응답시간 단축(약 5초)
  - 생산성(productivity) 향상
    - 프로세서 유휴 시간 감소
- 단점
  - 통신 비용 증가
    - 통신선 비용, 보안 문제 등
  - 개인 사용자 체감 속도 저하
    - 동시 사용자수 증가 -> 시스템 부하 증가 -> 느려짐 (개인관점에서)
![](https://images.velog.io/images/kpl5672/post/a9b462fc-535f-45c8-bb43-1765aff42574/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.43.13.png)
#### Personal Computing
- 개인이 시스템 전체 독점
- CPU 활용률이 더이상 고려의 대상이 아님(원래는 최대한 컴퓨터를 놀지 않고 일시키는 게 주 관심사였음)
- os가 상대적으로 단순(하지만 다양한 편리한 기능 지원)
- 장점
  - 빠른 응답시간
- 단점
  - 성능이 낮음
 
#### Parallel Processing System
- 단일 시스템 내에서 둘 이상의 프로세서 사용
  - 동시에 둘 이상의 프로세스 지원
- 메모리 등의 자원 공유(Tightly-coupled system)
- 사용 목적
  - 성능 향상
  - 신뢰성 향상(하나가 고장나도 정상 동작 가능)
- 프로세서간 관계 및 역할 관리 필요
![](https://images.velog.io/images/kpl5672/post/208a7336-0b8e-460c-b9b5-4d068305155d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.48.27.png)
#### Distributed processing system(분산 처리 시스템)
- 네트워크를 기반으로 구축된 병렬처리 시스템(Loosely-coupled system)
  - 물리적인 분산, 통신망 이용한 상호 연결
  - 각각 컴퓨터를 노드라고 부름
  - 각각 운영체제 탑재한 다수의 범용 시스템으로 구성
  - 사용자는 분산운영체제를 통해 하나의 프로그램, 자원처럼 사용 가능(은폐성, transparency)
  - 각 구성요소들간의 독립성 유지, 공동작업 가능
  - cluster system, client-server system, P2P 등
- 장점
  - 자원 공유를 통한 높은 성능
  - 고신뢰성, 높은 확정성
- 단점
  - 구축 및 관리가 어려움
![](https://images.velog.io/images/kpl5672/post/eb442976-680e-4cdf-9e35-190f231fcee5/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.50.52.png)
#### Real-time system(실시간 시스템)
- 작업 처리에 dealine을 갖는 시스템
  - 제한 시간 내에 서비스를 제공하는 것이 자원 활용 효율보다 중요
- 작업 종류
  - Hard real-time task
    - 늦으면 큰일나는 거. 
    - 예, 발전소 제어, 무기 제어
  - Soft real-time task
    - 동영상 재생
  - Non real-time task

# 3. 운영체제의 구조
## 1) 커널과 유틸리티
### 커널(Kernel)
- OS의 핵심 부분(메모리 상주, 계속 사용되므로 메모리에 항상 올라가있다는 의미)
  - 가장 빈번하게 사용되는 기능들 담당
    - 시스템 관리(processor, memory, Etc)

### 유틸리티(Utility)
- 비상주 프로그램
- UI등 서비스 프로그램
![](https://images.velog.io/images/kpl5672/post/d563e42b-563c-4630-ac39-2c238c511077/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%204.34.24.png)

## 2) 구조
### 단일 구조
- 장점
  - 커널 내 모듈간 직접 통신
    - 효율적 자원 관리 및 사용
- 단점
  - 커널의 거대화
    - 오류 및 버그, 추가 기능 구현 등 유지보수가 어려움
    - 동일 메모리에 모든 기능이 있어, 한 모듈의 문제가 전체 시스템에 영향(예, 악성 코드 등)
![](https://images.velog.io/images/kpl5672/post/2a2e5663-14a9-4bbe-a794-fe8195d64754/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%204.35.47.png)
### 계층 구조
- 장점
  - 모듈화
    - 계층간 검증 및 수정 용이
  - 설계 및 구현의 단순화
- 단점
  - 단일구조 대비 성능 저하
    - 원하는 기능 수행을 위해 여러 계층을 거쳐야 함.
![](https://images.velog.io/images/kpl5672/post/72065ace-28ae-4191-9621-2c69596c5ee3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%204.39.47.png)

### 마이크로 커널 구조
- 커널의 크기 최소화
  - 필수 기능만 포함
  - 기타 기능은 사용자 영역에서 수행
  ![](https://images.velog.io/images/kpl5672/post/2ebf34df-67f4-4f24-8856-2fd9949e327e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%204.40.55.png)
# 4. 운영체제의 기능
## 요약
- 프로세스 관리
- 프로세서 관리
- 메모리 관리
- 파일 관리
- 입출력 관리
- 보조 기억 장치 및 기타 주변장치 관리


### Process Management
#### 프로세스란?
- 커널에 등록된 실행 단위(실행 중인 프로그램)
- 사용자 요청/프로그램의 수행 주체(entity)
#### OS의 프로세스 관리 기능들
- 생성/삭제, 상태관리
- 자원 할당
- 프로세스 간 통신 및 동기화(synchronization)
- 교착상태(deadlock) 해결
#### 프로세스 정보 관리
- PCB (Process Control Bloc)

### processor Management
#### 프로세서란?
- 중앙 처리 장치(CPU)
  - 프로그램을 실행하는 핵심 자원
- 큰 그림에서는 프로세서=cpu라고 이해해도 크게 문제 되진 않음
#### 프로세스 스케줄링
- 시스템 내의 프로세스 처리 순서 결정
#### 프로세서 할당 관리
- 프로세스들에 대한 프로세서 할당
  - 한 번에 하나의 프로세스만 사용 가능
  
### Memory Management
#### 주기억장치
- 작업을 위한 프로그램 및 데이터를 올려 놓는 공간
#### Multi-user, Multi-tasking 시스템
- 프로세스에 대한 메모리 할당 및 회수
- 메모리 여유 공간 관리
- 각 프로세스의 할당 메모리 영역 접근 보호
#### 메모리 할당 방법(scheme)
(뒷 강의에서 다룰 예정)
- 전체 적재
  - 장점: 구현이 간단 
  - 단점: 제한적 공간
- 일부 적재(virtual memory concept)
  - 프로그램 및 데이터의 일부만 적재
  - 장점: 메모리의 효율적 활용
  - 단점: 보조기억 장치 접근 필요
  
 ### File Management
 -파일: 논리적 데이터 저장 단위
 - 사용자 및 시스템의 파일 관리
 - 디렉토리 구조 지원
 - 파일 관리 기능
   - 파일 및 디렉토리 생성/삭제
   - 파일 접근 및 조작
   - 파일을 물리적 저장 공간으로 사상(mapping)
   - 백업 등

### I/O Management
- 입출력(I/O) 과정
  - OS를 만드시 거쳐야 함
  ![](https://images.velog.io/images/kpl5672/post/566839da-4711-4064-bff3-28596ec68106/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-10%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%204.50.14.png)
  
### Others
- Disk 관리
- networking 관리
- Security and Protection System관리
- Command interpreter system관리
- System call interface관리
  - 응용 프로개름과 os 사이의 인터페이스
  - os가 응용프로그램에 제공하는 서비스
