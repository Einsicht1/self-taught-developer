# 1. A Simple Start


```
package main

import "fmt" //must be double quotation mark

func main() {
	fmt.Println("Hi there!") //must be double quotation mark
}
```
### Go CLI
![스크린샷 2021-04-30 오후 10 03 50](https://user-images.githubusercontent.com/70195733/116698961-fb220f00-a9ff-11eb-8590-178f101c9898.png)
- `go build`: code를 compile한다.
- `go run`: code를 compile, execute한다.
- main.go가 있는 상태에서 `go build main.go`명령어를 치면 main이라는 파일이 생긴다. 이 파일은 `./main`명령어로 실행 가능하다.
- `go install`, `go get`은 dependancy에 관한 명령어다.

#### 1. How do we run the code inside our project?
`go run <file_name>`
#### 2. What does "package main" mean?
- package는 proejct 혹은 workspace다. 코드들의 집합.
- package는 관련된 여러 파일들로 이루어짐.
![스크린샷 2021-04-30 오후 10 11 50](https://user-images.githubusercontent.com/70195733/116699890-15a8b800-aa01-11eb-90ff-3214ba4d8565.png)
![스크린샷 2021-04-30 오후 10 12 32](https://user-images.githubusercontent.com/70195733/116699966-2eb16900-aa01-11eb-98b6-41eb904a4d1f.png)
![스크린샷 2021-04-30 오후 10 13 22](https://user-images.githubusercontent.com/70195733/116700052-4b4da100-aa01-11eb-9ef2-86ccc658eb8b.png)
- executable로 만들려면 package 이름이 꼭 main이어야 한다는 것 같다.
#### 3. what does 'import fmt' mean?
- fmt 는 go의 standard library다.
- golang.org/pkg/ 에서 go의 패키지들 정보 볼 수 있다.
#### 4. what's that 'func' thing?
- func른 다른 언어의 함수와 같은 개념이다.
![스크린샷 2021-04-30 오후 10 18 45](https://user-images.githubusercontent.com/70195733/116700711-0bd38480-aa02-11eb-8077-e7f890cf19f1.png)
#### 5. How is the main.go file organized?
![스크린샷 2021-04-30 오후 10 19 54](https://user-images.githubusercontent.com/70195733/116700888-44735e00-aa02-11eb-9129-51e933470493.png)