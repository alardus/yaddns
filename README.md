# Yandex Dynamic DNS

- Преполагается, что управление доменом делегировано Яндексу.
- В "Редакторе DNS" на странице управления доменом в http://pdd.yandex.ru добавьте новую DNS-запись типа "А" с нужным именем поддомена:

`subdomain.host.com A 1.2.3.4`

В поле "Значение записи" указывайте любой IP, он будет заменен нужным адресом. Или вызовите `addhost(subdomain,ip)` из api.py.

- Получите ключ для управления доменом. Для этого откройте:

`https://pddimp.yandex.ru/api2/admin/get_token`

авторизуйтесь, укажите имя домена и получите токен.

Копируйте его в поле `TOKEN` в файле `.env`.

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
