# Yandex Dynamic DNS

- Преполагается, что управление доменом делегировано Яндексу.
- Получите ключ для управления доменом. Для этого откройте:

`https://pddimp.yandex.ru/api2/admin/get_token`

авторизуйтесь, укажите имя домена и получите токен. Копируйте его в поле `TOKEN` в файле `.env`.

- Укажите `DOMAIN` и `SUBDOMAIN`, которыми хотите управлять, в файле `.env`:

```
DOMAIN = 'host.com'
SUBDOMAIN = 'subdomain'
```

- Установите необходимые модули:

`pip install -r req.txt`

- Чтобы добавить поддомен:

`./yaddns --add hostname ip`

- Чтобы удалить поддомен:

`./yaddns --delete hostname`

- Чтобы обновить адрес поддомена вручную:

`./yaddns --update hostname ip`

- Чтобы автоматически раз в 30 минут обновлять адрес для поддомена указанного в .env:

`./yaddns --auto`

Для последнего случая удобно положить скрипт в Docker:

```
docker build -t alardus/yaddns .
docker run -d --restart=always --name yaddns alardus/yaddns
```
