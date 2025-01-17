# ModrinthMultiDownloader
Эта программа позволяет загружать сразу несколько модов из Modrinth благодаря своему API.

**ПРЕДУПРЕЖДЕНИЕ**: В связи с тем, что эта программа в настоящее время находится в стадии разработки, в процессе ее работы могут возникать ошибки.
Пожалуйста, сообщайте обо всех ошибках по электронной почте: kirhit135@gmail.com (*обязательно укажите хэштег #MRMBug, неважно, в тексте письма или в его заголовке.*)

*Если вы хотите загрузить изменённый и/или доработанный код, пожалуйста, укажите в файле "README.md" в качестве автора кода, в остальном ограничений нет.*

# Как использовать

1) Скачайте ZIP-архив программы и распакуйте его в любой папке.
2) Откройте командную строку в данной директории и пропишите следующую команду:
   `pip install -r requirements.txt`
3) Затем создайте файл со списком модов, необходимых для установки.
   `Важное примечание: указывать нужно не сами названия модов, а их ID в конце их ссылок. Каждый мод с новой строки.`
4) После этого запустите **main.py** следующим образом:
   `main.py -mode [server/client] -loader [загрузчик] -version [версия игры, для которой нужно установить моды] -modlist [путь к списку]`
5) После этого должен отобразиться прогресс загрузки модов, а также предупреждения о том, что некоторые из модов в процессе их скачивания могли быть не загружены.
6) После загрузки всех модов, они автоматически переместятся в отдельную папку, откуда их можно скопировать в папку модов или плагинов (в случае, если выбран режим "server").

*На этом пока всё* **:P**
