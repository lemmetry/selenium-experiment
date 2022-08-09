# selenium-experiment

This repository holds experiments wtih [Selenium](https://www.selenium.dev/documentation/) in Python and 
[pytest](https://docs.pytest.org/) framework.

## Prerequisites:
1. [Python 3.7](https://www.python.org/downloads/).
2. [pipenv](https://github.com/pyenv/pyenv#installation).

## How to set up:
1. Clone the repository.
2. Install [dependencies](#dependencies) by running `pipenv install`.
3. From [browser drivers](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) install 
`ChromeDriver` for Chromium/Chrome and/or `geckodriver` for Firefox. This repository utilizes `ChromeDriver` version 
`104.0.5112.79` and `geckodriver` version `0.31.0`, but you will have to have only one.


## Dependencies:
1. [pytest](https://docs.pytest.org/en/7.1.x/).
2. [Selenium](https://www.selenium.dev/documentation/).
3. [Browser driver(s)](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) of choice.

## How to run:
`pipenv run python -m pytest`
