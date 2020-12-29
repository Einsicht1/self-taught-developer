#part 2
`scrapy startproject worldometers`

위 명령어 실행 시 worldometers라는 프로젝트가 만들어진다.
그 안엔 다시 1) scrapy.cfg, 2)worldometers 폴더가 만들어진다.

scrapy.cfg파일은 스파이더를 실행시킬 떄 중요한 파일이다.

-worldometers 폴더 안에 들어가면 spiders라는 dir이 있다.
여기에 모든 spider가 모인다.

-items.py는 데이터를 분류, 정리한다.

-middlewares.py에서는 request,response관련된 것을 처리한다.

-pipelines.py는 scraping한 데이터를 db에 저장한다.
-settings.py는 이름 그대로 셋팅 설정하는 곳이다.

`scrapy genspider naver https://www.naver.com/`
위 명령어에서 두 가지를 바꿔야 한다.
1) scrapy는 맨 뒤에 자동으로 '/'를 붙여주기에 제거해야 한다.
2) scrapy는 자동으로 https://를 써주기에 이것도 지워야 한다.
결과:
`scrapy genspider naver www.naver.com`
위 명령어를 치면 spiders dir에 naver.py라는 파일이 생긴다.

주의사항
-하나의 프로젝트에 여러 스파이더를 만들 수 있다.
and each spider must have a unique name 
`scrapy genspider`명령어는 프로젝트 디렉토리 안에서(cfg파일 있는 곳) 치자!

새로 생긴 spider파일에 대해 알아보자.
-allowed_domains엔 http://같은걸 붙여선 안된다.
-strat_urls는 크롤링하고자 하는 url이다. http가 디폴트라서 https로 바꿔주자.


# part 3
`conda install ipython`   
`scrapy shell`

아래처럼 쉘에 접속 가능하다. 
```
s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x113bb0df0>
[s]   item       {}
[s]   settings   <scrapy.settings.Settings object at 0x113bb0730>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
2020-12-12 12:26:56 [asyncio] DEBUG: Using selector: KqueueSelector
```

아래 명렁어로 url에 fetch를 해보자.
`fetch("https://www.worldometers.info/world-population/population-by-country/")`
결과는 아래와 같다.
robots.txt는 못찾았고(404), 타겟 사이트는 200 OK다.
```
2020-12-12 12:30:12 [scrapy.core.engine] INFO: Spider opened
2020-12-12 12:30:13 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://www.worldometers.info/robots.txt> (referer: None)
2020-12-12 12:30:13 [protego] DEBUG: Rule at line 2 without any user agent to enforce it on.
2020-12-12 12:30:13 [protego] DEBUG: Rule at line 10 without any user agent to enforce it on.
2020-12-12 12:30:13 [protego] DEBUG: Rule at line 12 without any user agent to enforce it on.
2020-12-12 12:30:13 [protego] DEBUG: Rule at line 14 without any user agent to enforce it on.
2020-12-12 12:30:13 [protego] DEBUG: Rule at line 16 without any user agent to enforce it on.
2020-12-12 12:30:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.worldometers.info/world-population/population-by-country/> (referer: None)
```

Reuqest는 scrapy에서 객체고, url과 몇몇 argument를 인자로 받는다.
`r = scrapy.Request(url="https://www.worldometers.info/world-population/population-by-country/")`
`fetch(r)`
이렇게 해도 결과는 같다.
request객체를 fetch한 것이기 때문.

타겟 사이트의 html을 얻으려면 다음처럼 하면 된다.
`response.body`

`view(response)`
이 명령어는 response를 파일로 보여준다. 화면 창이 열리면서 결과화면을 보여준다.
이 화면은 또한 spider가 보는 화면이다.
참고로 spider는 자바스크립트를 못본다. 이게 클로링할때 문제가 되기도 한다.  

### text 가져오기

h1 태그를 xpath로 가져오려면 아래처럼 하면 된다.  

`response.xpath("//h1")`  

이제 텍스트를 가져오는 예시를 보자. 예시에서는 xpath, css두 가지 방법을 보여준다.

<img width="832" alt="Screen Shot 2020-12-21 at 4 34 51 PM" src="https://user-images.githubusercontent.com/60768642/102751135-79afd580-43aa-11eb-8f7b-3aafa78ecdf6.png">

-예시를 자세히 보면, css를 써도 xpath selector를 사용해 데이터를 가져오는 것을 볼 수 있다.
그래서 이 강의자는 xpath를 주로 쓴다고 한다. 성능상에도 이게 유리하다고 한다.  
-css selector로 text만 출력하려면 `h1::text` 요렇게 해주면 된다.

### 모든 country 이름 가져오기
td테그 안에 있는 a테그를 x path로 가져오려면 `//td/a` 이렇게 해주면 된다.
이렇게 해서 모든 country 이름을 가져와보자.

```
countries = response.xpath("//td/a/text()")
contries.get()
'China'
```
어랏, 딱 한개만 출력된다.
여러개를 출력하려면 `getall()`을 사용해야 한다.

`countries = response.xpath("//td/a/text()").getall()`
countries를 출력해보면 페이지에 있는 국가명이 출력됨을 확인할 수 있다.

<img width="231" alt="Screen Shot 2020-12-21 at 4 41 13 PM" src="https://user-images.githubusercontent.com/60768642/102751559-5afe0e80-43ab-11eb-9650-e601ad7445f7.png">

같은 과정을 css selector를 활용해서 해보자.
`response.css("td a::text").getall()`  


#### 같은 과정을 shell이 아닌 프로젝트 상에서 해보자.
-우선 이미 worldometers/spiders/countries.py를 만들었었다.
이 파일을 작성해준다.
```
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/world-population/population-by-country']
    start_urls = ['http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a/text()").getall()

        yield {
            'title': title,
            'countries': countries
        }

```

- scrapy에선 항상 dict형태로 data를 return 해야 한다.  
- 프로젝트 명령어를 칠 땐 항상 config파일이 있는 곳에서 해야한다.  
- `scrapy crawl countries(스파이더 이름)` 으로 작성한 spider를 실행시킨다.  
결과화면

<img width="844" alt="Screen Shot 2020-12-21 at 5 54 28 PM" src="https://user-images.githubusercontent.com/60768642/102758138-a2899800-43b5-11eb-8204-ddd23293af32.png">
![Uploading Screen Shot 2020-12-21 at 5.54.28 PM.png…]()

