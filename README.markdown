PyUnoService
============


Simple wrapper for [UnoService](https://github.com/alephdata/unoservice/).


Install
-------


```
python setup.py install
```


Usage
-----

```
from pyunoservice import UnoService

service = UnoService()
service.convert('/tmp/input-file.doc', '/tmp/output-file.pdf')
```


