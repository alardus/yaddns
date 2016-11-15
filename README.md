# Yandex Dynamic DNS

- Преполагается, что управление доменом делегировано Яндексу.
- В "Редакторе DNS" на странице управления доменом в http://pdd.yandex.ru добавьте новую DNS-запись типа "А" с нужным именем поддомена:

`subdomain.host.com A 1.2.3.4`

В поле "Значение записи" указывайте любой IP, он будет заменен нужным адресом.

- Получите ключ для управления доменом. Для этого откройте:

`https://pddimp.yandex.ru/get_token.xml?domain_name=subdomain.host.com`

авторизуйтесь и в исходнике страницы (`хинт! web developer`) найдите поле:

`token="XXXXXX"`

Копируйте его в поле `TOKEN` в файле `.env`.

- Теперь получите ID вашей учетной записи на Яндексе. Для этого откройте:

`https://pddimp.yandex.ru/nsapi/get_domain_records.xml?token=XXXXXX&domain=host.com`

В поле `token` указываем полученный ранее ключ, в `domain` - имя делегированного на Яндекс домена. В выводе страницы ищем запись для ранее созданного поддомена, в этой же строке будет указан `ID` вида:

`id="1234567"`

Копируйте его в поле `RECID` в файле `.env`.

- Заполните поля `DOMAIN` и `SUBDOMAIN` в файле `.env`:

```
DOMAIN = 'host.com'
SUBDOMAIN = 'subdomain'
```

- Установите необходимые модули (если планируете запускать скрипт не из Docker):

`pip install -r req.txt`

- Добавьте скрипт `yaddns.py` в CRON:

`crontab -e`
`*/30 * * * * /path/to/yaddns.py`

Или запустите его из Docker:

```
docker build -t alardus/yaddns .
docker run -d --restart=always --name yaddns alardus/yaddns
```
