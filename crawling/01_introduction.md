# Introduction
-requests, BeautifulSoup은 대규모 프로젝트엔 부적절하다.
-scrapy는 1분에 960페이지를 크롤링 할 수 있다.
-scpray에는 5가지 컴포넌트가 있다
1)SPIDERS
2)PIPELINES
3)MIDDLEWARES
4)ENGINE
5)SCHEDULER

-spiders에선 내가 뭘 스크래핑 할건지 정의한다. scrapy.Spider, CrawlSpider, XMLFeedSpider, CSVFeedSpider, SitemapSpider이렇게 5가지 클래스가 있다.
이 수업에선  scrapy.Spider, CrawlSpider 두개를 사용한다.

-pipelines은 'cleaning the data', 'remove duplication', storing data'등을 한다.

-middlewares는 'Request/Response', 'Injecting custom headers', 'Proxying' 등을 담당한다.

-Engine은 다른 컴포넌드들의 기저에서 작동한다?. 컨트롤 타워 같다.
-scheduler은 아직 이해가 잘 안된다.
![](https://images.velog.io/images/kpl5672/post/c322c66a-2349-4993-983a-c7497264595d/Screen%20Shot%202020-12-10%20at%209.21.17%20PM.png)

### robots.txt
User-Agent, Allow, Disallow를 알면 된다.
User-Agent는 대상, allow, disallow는 단어 그대로의 뜻이다.


### 환경설정
-conda 가상환경
`conda install -c conda-forge scrapy pylint autopep8`
특이한 점은, pip install이 권장되지 않는다는 것이다.
위 명령어로 세개를 설치해준다(나머지 뒤엔 python 코드 정렬 위한 도구들)


### scrapy fundamental
`scrapy`: scrapy로 할 수 있는 명령어들을 출력한다.(이외에 다른것들도 출력)
`scrapy bench`: Run quick benchmark test
이명령어를 치면 길게 결과화면이 뜬다.
그 중 아래 한 줄이, bench가 실제로 시작하는 부분이다.
`2020-12-10 21:40:39 [scrapy.core.engine] INFO: Spider opened`
로컬에 있는 어떤 페이지를 크롤링하기 시작한다.
맨 아래에선 크롤링이 끝나고 해당 크롤링에 대해 총체적 정보를 볼 수 있다.
```
{'downloader/request_bytes': 344120,
 'downloader/request_count': 744,
 'downloader/request_method_count/GET': 744,
 'downloader/response_bytes': 2402606,
 'downloader/response_count': 744,
 'downloader/response_status_count/200': 744,
 'elapsed_time_seconds': 10.504343,
 'finish_reason': 'closespider_timeout',
 'finish_time': datetime.datetime(2020, 12, 10, 12, 40, 50, 116448),
 'log_count/INFO': 20,
 'memusage/max': 53133312,
 'memusage/startup': 53133312,
 'request_depth_max': 24,
 'response_received_count': 744,
 'scheduler/dequeued': 744,
 'scheduler/dequeued/memory': 744,
 'scheduler/enqueued': 14878,
 'scheduler/enqueued/memory': 14878,
 'start_time': datetime.datetime(2020, 12, 10, 12, 40, 39, 612105)}
```

`scrapy fetch`: 위에 url을 적으면 해당 페이지의 html을 가져온다.
예시: `scray fetch https://naver.com`

#### spider
spider은 웹에서 데이터 긁어오는 컴포넌트다. 구글도 자기네 스파이더가 있다.

`scrapy settings`: 스크래피 세팅 출력
`scrapy shell`:  Interactive scraping console
`startproject`:  Create new project
`version`:       Print Scrapy version
`view`:          Open URL in browser, as seen by Scrapy

