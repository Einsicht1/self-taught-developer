# part 2
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

