# miniAd
 
Реализована основная часть задания, а именно 3 метода работа API
Вот пример адресов для взаимодействия:
http://127.0.0.1:800/api/advertisements/1 - для получения первой страницы объявлений
  для сортировки нужно использовать параметр sort. В него передаём поле по которому сортируем
http://127.0.0.1:800/api/advertisement/1 - для получения объявления с ИД 1
  fields - для вывода дополнителььных полей, указывать через запятую
  photos - нужно множество фото или 1
http://127.0.0.1:800/api/advertisement -  - для получения создания нового объявления

Рассмотрим поподробнее:

![Просмотре списка без параметров](https://github.com/andru196/miniAd/blob/master/screenshots/1.png)
![Просмотре списка с сортировкой](https://github.com/andru196/miniAd/blob/master/screenshots/3.png)
![Просмотре объявления с заданным списком доп.полей и параметром отображения множества ссылок](https://github.com/andru196/miniAd/blob/master/screenshots/2.png)
![Отправляем POST запрос для добавления объявления, внизу ввидно ответ](https://github.com/andru196/miniAd/blob/master/screenshots/4.png)
![Убеждаемся что всё сработало](https://github.com/andru196/miniAd/blob/master/screenshots/5.png)
