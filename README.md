This project shows a bug present in Django with migrating MySQL OneToOneFields in Django 1.11.2 that is not present in 1.10.7. This was tested on MySQL 5.7.18.

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
