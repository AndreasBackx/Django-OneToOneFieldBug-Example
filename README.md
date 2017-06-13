This project is a test case for ticket [28305](https://code.djangoproject.com/ticket/28305) on the Django issue tracker. The bug is present in Django 1.11.2 and the master branch for commit [7c4f05fae2ae12d698dc28421f5d4659162f928a](https://github.com/django/django/commit/7c4f05fae2ae12d698dc28421f5d4659162f928a) that is not present in 1.10.7. This was tested on MySQL 5.7.18.

## How to test the bug

Make sure you have a MySQL server installed and edit the settings in `onetoone/onetoone/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onetoone',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
    }
}
```

Then install tox and run `tox` to run the test.
