import inspect

URL = "http://localhost:8097/login.do"
UN = "admin"
PWD = "manager"


def whoami():
    return inspect.stack()[1][3]
