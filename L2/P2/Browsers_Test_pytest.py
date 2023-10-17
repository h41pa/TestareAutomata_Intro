import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
"""
pip install pytest
pip install pytest-xdist ( pentru a rula test in paralel

Pytest este un framework de testare care poate fi folosit atat in UniteTesting cat si in Integration Testing,
System Testing, etc. Functional testing in general

### Teste rulate in mod secvential ( unul dupa celalalt ):
pytest .\L2\P2\\Browsers_Test_pytest.py\

### Teste rulate in paralel ( mai multe deodata ):
pytest .\L2\P2\Browsers_Test_pytest.py\ -n x ( unde x este nr-ul de teste care merg in paralel )
daca dau 3 o sa apara 3 workeri care inseamna 1 worker pe fiecare test , 1worker = 1 cpu
"""
LINK = "https://formy-project.herokuapp.com/form"


def test_chrome():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(LINK)
    expected_url = "https://formy-project.herokuapp.com/form"
    actual_url = driver.current_url
    time.sleep(3)
    assert expected_url == actual_url, "Invalid URL !"
    driver.quit()


def test_firefox():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get(LINK)
    expected_url = "https://formy-project.herokuapp.com/form"
    curent_url = driver.current_url
    time.sleep(2)
    assert expected_url == curent_url, "Invalid !!!"
    driver.quit()

def test_edge():
    sevice = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=sevice)
    driver.get(LINK)
    expected_url = "https://formy-project.herokuapp.com/form"
    actual_url = driver.current_url
    time.sleep(3)
    assert expected_url == actual_url, "Invalid URL"
    driver.quit()
