import scrapy
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.crawler import CrawlerProcess
from ScrapeHero.items import SongItem
from ScrapeHero import constant

# TODO implement scrapyd concurrent spider processes

class RandomSpider(scrapy.Spider):
    name = 'random-spider'
    start_urls = [constant.CHORUS_URL]


    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome(chrome_options=options)

    def parse(self, response):
        self.driver.get(response.url)

        randomLink = self.driver.find_element_by_link_text('Randomizer!')

        randomLink.click()

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//div[@class='{constant.SONG_DIV_CLASS}']"))
        )

        songs = self.driver.find_elements_by_xpath(f"//div[@class='{constant.SONG_DIV_CLASS}']")

        for song in songs:
            item = SongItem()

            item['md5_hash'] = song.find_element_by_xpath(
                "div[@class='Song__hash']").text.split(' ')[2]
            item['url'] = song.find_element_by_xpath(
                "div[@class='Song__charter']//a").get_attribute('href')

            yield item

        while True:
            more = self.driver.find_element_by_link_text('Gimme moar random')

            try:
                more.click()

                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f"//div[@class='{constant.SONG_DIV_CLASS}']"))
                )

                songs = self.driver.find_elements_by_xpath(f"//div[@class='{constant.SONG_DIV_CLASS}']")

                for song in songs:
                    item = SongItem()
                    
                    item['md5_hash'] = song.find_element_by_xpath(
                        "div[@class='Song__hash']").text.split(' ')[2]
                    item['url'] = song.find_element_by_xpath(
                        "div[@class='Song__charter']//a").get_attribute('href')

                    yield item

            except:
                break

class LatestSpider(scrapy.Spider):
    name = 'latest-spider'
    start_urls = [constant.CHORUS_URL]

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome(chrome_options=options)

    def parse(self, response):
        self.driver.get(response.url)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//div[@class='{constant.SONG_DIV_CLASS}']"))
        )

        songs = self.driver.find_elements_by_xpath(f"//div[@class='{constant.SONG_DIV_CLASS}']")

        for song in songs:
            item = SongItem()

            item['md5_hash'] = song.find_element_by_xpath(
                "div[@class='Song__hash']").text.split(' ')[2]
            item['url'] = song.find_element_by_xpath(
                "div[@class='Song__charter']//a").get_attribute('href')

            yield item

        while True:
            more = self.driver.find_element_by_link_text('More songs')

            try:
                more.click()

                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f"//div[@class='{constant.SONG_DIV_CLASS}']"))
                )

                songs = self.driver.find_elements_by_xpath(f"//div[@class='{constant.SONG_DIV_CLASS}']")

                for song in songs:
                    item = SongItem()
                    
                    item['md5_hash'] = song.find_element_by_xpath(
                        "div[@class='Song__hash']").text.split(' ')[2]
                    item['url'] = song.find_element_by_xpath(
                        "div[@class='Song__charter']//a").get_attribute('href')

                    yield item

            except:
                break
