code for lecture 11
```
<!DOCTYPE html>
<html lang="en">

<head>
    <title>XPath and CSS Selectors</title>
</head>

<body>
    <h1>CSS Selectors simplified</h1>
    <div class="intro">
        <p>
            I'm paragraph within a div with a class set to intro
            <span id="location">I'm a span with ID set to location and i'm within a paragraph</span>
        </p>
        <p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p>
    </div>
    <p>Hi i'm placed immediately after a div with a class set to intro</p>
    <span class='intro'>Div with a class attribute set to intro</span>

    <ul id="items">
        <li data-identifier="7">Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
        <li>Item 4</li>
    </ul>

    <a href="https://www.google.com">Google</a>
    <a href="http://www.google.fr">Google France</a>

    <p class='bold italic'>Hi, I have two classes</p>
    <p class='bold'>Hi i'm bold</p>
</body>

</html>
```

Q1)위 코드에서 a 테그 중 href 속성을 가지면서 https인 것만 가져오려면 어떻게 해야할까?  
A1) `a[href^='https']`
이렇게 하면 된다. 
[]이 안에는 먼저 속성이 들어간다. [href] 이런 식으로.
^뒤에는 ~로 시작하는 걸 찾겠다는 의미가 생긴다.

Q2) a태그 중 href속성을 가지면서 fr로 끝나는 것만 가져오려면?    
A2) `a[href$='fr']`

Q3) a태그 중 href속성 중 중간에 google이라는 문자가 들어간 것을 가져오고 싶다면?
A3) `a[href*='google']`

```
    <a href="https://www.google.com">Google</a>
    <a href="http://www.google.fr">Google France</a>
```
code for lecture 14
```
<!DOCTYPE html>
<html lang="en">

<head>
    <title>XPath and CSS Selectors</title>
</head>

<body>
    <h1>XPath Selectors simplified</h1>

    <div class="intro">
        <p>
            I'm paragraph within a div with a class set to intro
            <span id="location">I'm a span with ID set to location and i'm within a paragraph</span>
        </p>
        <p id="outside">I'm a paragraph with ID set to outside and i'm within a div with a class set to intro</p>
    </div>

    <div class="outro">
        <p id="unique">I'm in a div with a class attribute set to outro</p>
    </div>

    <p>Hi i'm placed immediately after a div</p>

    <span class='intro'>Div with a class attribute set to intro</span>

    <ul id="items">
        <li data-identifier="7">Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
        <li>Item 4</li>
    </ul>

    <a href="https://www.google.com">Google</a>
    <a href="http://www.google.fr">Google France</a>
</body>

</html>
```
