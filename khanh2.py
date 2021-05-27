from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
class craw_lazada(object):
  def __init__(self,q):
    self.q = q
    self.url =f"https://www.lazada.vn/catalog/?spm=a2o4n.home.search.1.38f06afedTmOpn&q={q}&_keyori=ss&from=search_history&sugg=Macbook_0_1"
    self.driver = webdriver.Chrome("C:/Users/Administrator/Documents/BaoCaoPyThon/chromedriver.exe")
    self.delay=5

  def load_page(self):
    driver = self.driver
    driver.get(self.url)
    all_data = driver.find_elements_by_class_name("c16H9d,c13VH6,c1ZEkM")
    for data in all_data:
      print(data.text)
q = "Xiaomi"
crawler = craw_lazada(q)
crawler.load_page()