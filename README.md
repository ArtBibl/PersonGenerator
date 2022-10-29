# Person generator
Class for generating a person.

<hr>

<h4>This class can be used for test seeding the database.<br>
So far, this class can produce only Ukrainians. <br>
And also create a funny person.</h4>

<h4>For example:</h4>

<h6>...   from person_generator import Person<br>
... person = Person()<br>
... print(person.get_person_in_list())</h6>

<h4>You get a list of personas with all possible characteristics:</h4>

['Сербин', 'Явдоха', 'Хотянівна', '47', 'Жіноча', 'Технік-технолог (електротехніка)', 'Новогродівка', 'Вакцинована', 'Ні', 'Відсутня вища освіта', 'Публій Овідій Назон. «Метаморфози»']
<hr>
<h4>Also you can generate only concrete info.<br>
You must specify which characteristics you want to get.<br>
For example:</h4>

<h6>...   from person_generator import Person<br>
... person = Person()<br>
... print(person.get_person_in_list(order_=<u>"sn, n, pn")</u>)</h6>

<h4>Now you will get (for example):</h4>
['Драган', 'Раїна', 'Володарівна']

<h4>Description of pointers:</h4>
<ul>
<li><a>n - name</a></li>
<li><a>sn - second name</a></li>
<li><a>pn - patronymic name</a></li>
<li><a>a - age of person</a></li>
<li><a>s - sex of person</a></li>
<li><a>pro - profession</a></li>
<li><a>cb - city</a></li>
<li><a>v - vaccine status</a></li>
<li><a>p - pets</a></li>
<li><a>he - higher education</a></li>
<li><a>bb - favorite book (best book)</a></li>
</ul>

Some data is accidentally retrieved from .txt files.<br>
Now we are using options that were taken from the wiki pages.
<hr>

<h4>Also you can generate person in string.<br>
You should call method 'get_person_in_string()'<br>
For example:</h4>

<h6>...   from person_generator import Person<br>
... person = Person()<br>
... print(person.get_person_in_string(order_=<u>"sn, n, pn, a, cb"</u>))</h6>

<h4>Now you will get (for example):</h4>
Никоненко, Еммануїла, Судимирівна, 63, Донецьк
<hr>
