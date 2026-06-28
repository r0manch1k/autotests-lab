```sh
# macos

brew install allure

pip install -r requirements.txt

pytest --alluredir=allure-results tests/test_freefem.py

allure serve allure-results
```

![Результаты тестирования](docs/allure-results.png)
