# Классификатор отзывов IBDM.
Приложение с моделью машинного обучения, готовое к размещению на pythonanywhere.com<br/>
<br/>
Для размещения необходимо выполнить следующее:<br/>
1. В репозитории в django_project/settings.py уже записано ALLOWED_HOSTS = ['*'] .<br/>
2. В репозитории уже создан requirements.txt .<br/>
3. Пройти регистрацию на pythonanywhere.com и открыть bash .<br/>
4. Клонировать репозиторий git clone https://github.com/Sergey-Misyura/django_project .<br/>
5. Настроить переменные среды:<br/>
python3 -m venv env --system-site-packages #для доступа к имеющимся библиотекам сервера<br/>
source env/bin/activate <br/>
cd deploy_on_pythonanywhere <br/>
pip install -r requirements.txt <br/>
6. Получить путь для env:<br/>
cd<br/>
ls<br/>
pwd     (Выглядит как: /home/*user_name*/env) <br/> 
7. На вкладке Web выполнить add a new web app. <br/> 
В качестве фреймворка выбрать Django, потом нажать далее, выбрать последнюю версию python.
8. В разделе Web открыть файл конфигурации WSGI:
заменить mysite на django_project в строках project_home и os.environ['DJANGO_SETTINGS_MODULE'] .
9. На вкладке Web в разделе virtualenv записать путь полученный ранее в bash /home/*user_name*/env .
10. На вкладке Web в разделе Static files указать адрес /home/SergeyM/django_project/static .
11. На вкладке Web нажать перезагрузить и перейти по ссылке.
 <br/> 
P.S.: При возможных ошибках пути указывать прямой путь вместо относительного.


