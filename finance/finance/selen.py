import os
from selenium import webdriver
from time import sleep


class LinkReacord(webdriver.Chrome):
    """ Class for record a links href to txt file """

    def __init__(self, *args, **kwargs):
        super(LinkReacord, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome(executable_path='../media/chrome_exe/chromedriver.exe')

    def collect_link(self):
        """Function for collecting a link of company link csv"""

        driver = self.driver
        short_names = ['PD', 'ZUO', 'PINS', 'ZM', 'CLDR', 'RUN', 'DOCU']
        os.chdir('../../finance/media/company_name/')
        if os.path.getsize('company.txt') > 0:
            os.system(r'null>company.txt')
        # open('company.txt', 'w').close() second variant

        for link in short_names:
            yahoo_link = f'https://finance.yahoo.com/quote/{link}/history?p={link}'
            driver.get(yahoo_link)
            d = driver.find_element_by_xpath(
                '//div[@class="Pt(15px)"]/div[@class="Bgc($lv1BgColor) Bdrs(3px) P(10px)"]/div[@class="D(ib) Py(6px) Mend(40px) Mend(10px)--tab768 smartphone_Mend(0px)"]')
            d.click()
            sleep(5)
            max1 = driver.find_element_by_xpath(
                '//div[@class="W(195px)"]/ul[@class="P(0) M(0) List(n) Mb(5px)"][2]/li[@class="W(25%) D(ib) Va(m)"][4]/button[@class="Py(5px) W(45px) Fz(s) C($tertiaryColor) Cur(p) Bd Bdc($seperatorColor) Bgc($lv4BgColor) Bdc($linkColor):h Bdrs(3px)"]')
            max1.click()
            sleep(5)
            download_href = driver.find_elements_by_xpath('//a[@class="Fl(end) Mt(3px) Cur(p)"]')
            download_link = download_href[0].get_attribute('href')

            with open('company.txt', 'a', encoding='utf-8') as company_file:
                company_file.write(download_link + ',\n')
        company_file.close()
        self.driver.close()


if __name__ == '__main__':
    collect_href = LinkReacord(executable_path='../media/chrome_exe/chromedriver.exe')
    collect_href.collect_link()






### For testing

# class PythonOrgSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome('../chromedriver.exe')
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         short_names = ['PD', 'ZUO', 'PINS', 'ZM', 'CLDR', 'RUN']
#         os.chdir('../../finance/media/company_name/')
#         if os.path.getsize('company.txt') > 0:
#             os.system(r'null>company.txt')
#         # open('company.txt', 'w').close() second variant
#
#         for link in short_names:
#             yahoo_link = f'https://finance.yahoo.com/quote/{link}/history?p={link}'
#             driver.get(yahoo_link)
#             d = driver.find_element_by_xpath('//div[@class="Pt(15px)"]/div[@class="Bgc($lv1BgColor) Bdrs(3px) P(10px)"]/div[@class="D(ib) Py(6px) Mend(40px) Mend(10px)--tab768 smartphone_Mend(0px)"]')
#             d.click()
#             sleep(5)
#             max1 = driver.find_element_by_xpath('//div[@class="W(195px)"]/ul[@class="P(0) M(0) List(n) Mb(5px)"][2]/li[@class="W(25%) D(ib) Va(m)"][4]/button[@class="Py(5px) W(45px) Fz(s) C($tertiaryColor) Cur(p) Bd Bdc($seperatorColor) Bgc($lv4BgColor) Bdc($linkColor):h Bdrs(3px)"]')
#             max1.click()
#             sleep(5)
#             download_href = driver.find_elements_by_xpath('//a[@class="Fl(end) Mt(3px) Cur(p)"]')
#             download_link = download_href[0].get_attribute('href')
#             print('первая путь', os.getcwd())
#
#             with open('company.txt', 'a', encoding='utf-8') as company_file:
#                 company_file.write(download_link+',\n')
#         company_file.close()
#
#
#     def tearDown(self):
#         self.driver.close()
