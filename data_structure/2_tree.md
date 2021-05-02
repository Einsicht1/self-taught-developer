# 1. 트리
### 1) 트리란?
- 데이터의 상-하 관계를 저장하는 자료 구조

#### 계층적 관계
- 회사 조직도, 컴퓨터 폴더 구조, 클래스 상속 관계가 계층적 관계의 예시다.
<img width="715" alt="스크린샷 2021-05-02 오후 4 12 54" src="https://user-images.githubusercontent.com/70195733/116805396-51f32a00-ab61-11eb-9ed9-d4f29224c63d.png">
<img width="831" alt="스크린샷 2021-05-02 오후 4 12 58" src="https://user-images.githubusercontent.com/70195733/116805399-5586b100-ab61-11eb-930c-b164c56386b1.png">

- 리스트, 딕셔너리 등은 계층적 관계를 표현하기 어렵다.
- 트리의 맨 위 노드를 root 노드라 한다.
- 트리 주요 용어 설명
<img width="871" alt="스크린샷 2021-05-02 오후 4 16 26" src="https://user-images.githubusercontent.com/70195733/116805473-d6de4380-ab61-11eb-80e3-30469eb894be.png">

```
root 노드(뿌리 노드): 트리의 시작 노드, 뿌리가 되는 노드를 말합니다. 보통 트리를 표현할 때 위 그림처럼 가장 위에 root 노드를 놓는 방식으로 나타냅니다.
부모 노드: 특정 노드의 직속 상위 노드입니다. 노드 G, J, K가 있는 노란색 박스를 살펴보면 G가 J와 K의 부모 노드입니다.
자식 노드: 특정 노드의 직속 하위 노드입니다. 부모 노드와 반대되는 개념인데요. 노드 G, J, K가 있는 노란색 박스를 살펴보면 J와 K가 G의 자식 노드입니다.
형제 노드: 같은 부모를 갖는 노드입니다. D와 E는 둘다 그 부모가 B죠? 이럴 때 D와 E는 서로 형제 노드입니다.
leaf 노드 (잎/말단 노드): 자식 노드를 갖고 있지 않은, 가장 말단에 있는 노드입니다. 트리의 끝에 있다고 해서 root(뿌리) 노드와 반대되는 표현으로 leaf(잎) 노드라고 부릅니다. 
위 그림에서 노란색 박스로 둘러싼 F가 leaf 노드입니다. F뿐만 아니라 D, H, I, J, K 모두 leaf 노드입니다.
깊이: 특정 노드가 root 노드에서 떨어져 있는 거리입니다. 깊이는 해당 노드로 가기 위해서 root 노드에서 몇 번 아래로 내려와야 하는지를 나타냅니다. 
예를 들어 위 그림에서 root 노드의 자식 노드인 B와 C는 깊이가 1입니다. D, E, F, G는 깊이가 2이고, H, I, J, K는 깊이가 3입니다. 
결국 깊이라는 건 특정 노드가 root 노드로부터 얼마나 멀리 떨어져 있는지를 나타냅니다.
레벨: 깊이 + 1. 깊이랑 거의 똑같은 개념입니다. 그냥 깊이에 1을 더한 값이죠. 레벨 1에 있는 노드들, 레벨 2에 있는 노드들… 이런식으로 특정 깊이인 노드들을 묶어서 표현할 때 사용하는 용어입니다.
높이: 트리에서 가장 깊이 있는 노드의 깊이입니다. 위 그림의 트리에서는 H, I, J, K가 가장 깊이 있는 노드들이고 그 깊이는 모두 3입니다. 그래서 트리의 높이는 3입니다.


부분 트리 (sub-tree): 현재 트리의 일부분을 이루고 있는 더 작은 트리를 말합니다. 
위 그림의 트리는 root 노드가 A인 트리입니다. 그런데 이 트리를 좀더 작은 단위로 쪼개보면 더 작은 부분 트리들을 발견할 수 있습니다. 
예를 들어 위 그림의 노란색 큰 박스 안을 보세요. 노란색 큰 박스 안에는 ‘C가 root 노드인 트리’가 있는데요. 
이런 걸 바로 부분 트리라고 합니다. 지금 C가 A의 오른쪽 자식이죠?
그래서 노란색 큰 박스 안에 있는 부분 트리를 A의 “오른쪽 부분 트리”라고 합니다. 
특정 노드를 root 노드라고 생각하고 바라본다면 여러 가지 부분 트리들을 발견할 수 있습니다. 
하나의 전체 트리에 여러 부분 트리들이 존재하는 겁니다.
```
### 2) 트리의 활용
- 계층적 관계가 있는 데이터를 컴퓨터에서 사용
- 컴퓨터 과학의 다양한 문제를 기발하게 해결(예. 정렬, 압축)
- 흔히 사용하는 여러 추상 자료형 구현


### 3) 이진트리
- 자식의 최대 수가 2인 트리.
- 왼쪽 자식과 오른쪽 자식으로 나눠 관리

###  4) 이진트리의 종류
#### 정 이진 트리(Full Binary Tree)
- 모든 노드가 2개 또는 0개의 자식을 갖는 이진 트리
<img width="798" alt="스크린샷 2021-05-02 오후 4 29 03" src="https://user-images.githubusercontent.com/70195733/116805796-bca56500-ab63-11eb-9507-f1c0b44f9394.png">
#### 완전 이진 트리(complete Binary Tree)
- 마지막 레벨 직전의 레벨까지는 모든 노드들이 다 채워진 트리
- 왼쪽부터 오른쪽 방향으로 노드들이 채워져야 함.
- 완전 이진 트리 안에 저장된 노드가 n개라고 할 때, 높이는 항상 lg(n)에 비례한다.
<img width="792" alt="스크린샷 2021-05-02 오후 4 29 59" src="https://user-images.githubusercontent.com/70195733/116805800-c0d18280-ab63-11eb-8433-46bbdb6319da.png">
<img width="823" alt="스크린샷 2021-05-02 오후 4 30 27" src="https://user-images.githubusercontent.com/70195733/116805803-c29b4600-ab63-11eb-9226-b7028d97d32c.png">
#### 포화 이진 트리(Perfect Binary Tree)
- 모든 레벨이 완벽하게 다 채워져 있는 트리
<img width="802" alt="스크린샷 2021-05-02 오후 4 31 35" src="https://user-images.githubusercontent.com/70195733/116805820-e5c5f580-ab63-11eb-8da6-dd5798600acf.png">
<img width="802" alt="스크린샷 2021-05-02 오후 4 32 37" src="https://user-images.githubusercontent.com/70195733/116805838-055d1e00-ab64-11eb-9ff3-3cb121d32d31.png">







# 2. 힙
#### 힙이란?
# 3. 이진 탐색 트리
#### 이진 탐색 트리란?