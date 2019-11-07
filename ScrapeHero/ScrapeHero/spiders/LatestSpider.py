# -*- coding: utf-8 -*-
import scrapy
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ScrapeHero.items import ScrapeHeroItem


class LatestspiderSpider(scrapy.Spider):
    name = 'LatestSpider'
    allowed_domains = ['chorus.fightthe.pw']
    start_urls = ['https://chorus.fightthe.pw/']

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome(chrome_options=options)

    def parse(self, response):
        xPath_SongMeta = "//div[@class='Song__meta']"
        xPath_CharterLink = "div[@class='Song__charter']//a"

        self.driver.get(response.url)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xPath_SongMeta)))

        songs = self.driver.find_elements_by_xpath(xPath_SongMeta)

        for song in songs:
            item = ScrapeHeroItem()

            item['url'] = song.find_element_by_xpath(
                xPath_CharterLink).get_attribute('href')
            item['source'] = 'CHORUS'

            yield item

        while True:
            more = self.driver.find_element_by_link_text('More songs')

            try:
                more.click()

                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xPath_SongMeta)))

                songs = self.driver.find_elements_by_xpath(xPath_SongMeta)

                for song in songs:
                    item = ScrapeHeroItem()

                    item['url'] = song.find_element_by_xpath(
                        xPath_CharterLink).get_attribute('href')
                    item['source'] = 'CHORUS'

                    yield item

            except:
                break
