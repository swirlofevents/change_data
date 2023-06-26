# Веб-сервер для замены входящих данных HTTP запросов

## Настройки

Основной файл настроек находится в app/settings/settings.yaml. 
Образец настроек `app/settings/settings.yaml.copy`
### Секция app

```yaml
app:
  host: localhost
  port: 25083
  base_url: https://example.online
```

- `host` - ip или имя сервиса
- `port` - порт сервиса
- `base_url` - базовый адрес ресурса, с которого будут получаться и заменяться данные


## Запуск приложения
### Быстрый запуск

`start.bat` - windows пользователь,
`start.sh` - unix пользователь

### Медленный старт

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Тестик

[http://localhost:25083/test](http://localhost:25083/test) - тестовая страница.

#### Get параметры media_type=text/html&replace_content=True
- **media_type** - Формат отображения *text/plain*, *text/html...* Defaults = **text/plain**.
- **replace_content** - Заменять контент или нет. По дефолту не заменяется.