#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from selenium import webdriver
import time
import csv


class TastemadeSpider(scrapy.Spider):
    name = 'tastemade'
    start_urls = ['https://www.tastemade.com.br/receitas']

    def __init__(self, quantity_pages = 1, OUTPUT_FILE = '',DIR_WEBDRIVER = '', *args,**kwargs):
        self.OUTPUT_FILE = OUTPUT_FILE

        self.quantity_pages = quantity_pages

        self.driver = webdriver.Chrome(DIR_WEBDRIVER)

    def parse(self, response):
        items = response.xpath('//*[@id="react-root"]/div[2]/div/div/ul[1]/li')

        outfile = open(self.OUTPUT_FILE, "w", newline="")
        self.writer = csv.writer(outfile, delimiter = ';')

        self.writer.writerow(['link','titulo','descricao','ingredientes','instrucao','porcao'])

        for item in items:
            url = item.xpath('./div/div/a//@href').extract_first()
            yield(response.follow(url = url, callback=self.parse_receitas))

    def parse_receitas(self, response):
        self.driver.get(response.url)

        for i in range(self.quantity_pages):
            button = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div[2]/button')[0]
            button.click()
            time.sleep(1)

        res = response.replace(body=self.driver.page_source)

        receitas = res.xpath('//*[@id="react-root"]/div[2]/div/div/ul/li')

        for receita in receitas:
            url = receita.xpath('./div/div[2]/a//@href').extract_first()

            yield(response.follow(url = url, callback=self.parse_receita))

    def parse_receita(self, response):
        titulo = response.xpath('//*[@id="react-root"]/div[2]/main/div[2]/div[2]/div[1]/div[1]/div/div[1]/h1/a//@title').extract_first().replace('\n','').encode('utf-8')
        link = response.request.url
        descricao = response.xpath('//*[@id="react-root"]/div[2]/main/div[2]/div[2]/div[1]/div[1]/p/span//text()').extract_first().replace('\n','').encode('utf-8')

        ingredientes = response.xpath('//*[@id="react-root"]/div[2]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/p//text()').getall()
        ingredientes = ingredientes or response.xpath('//*[@id="react-root"]/div[2]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/ul/li//text()').getall()
        ingredientes = [ingrediente.replace('\n','').encode('utf-8') for ingrediente in ingredientes]

        instrucao = response.xpath('//*[@id="react-root"]/div[2]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/ol/li//text()').getall()
        instrucao = instrucao or response.xpath('//*[@id="react-root"]/div[2]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/ol/li//text()').getall()
        instrucao = [inst.replace('\n','').encode('utf-8') for inst in instrucao]
        
        porcao = response.xpath('//*[@id="react-root"]/div[2]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/p/text()').extract_first()
        porcao = porcao or response.xpath('//*[@id="react-root"]/div[2]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/p/text()').extract_first()
        porcao = porcao or response.xpath('//*[@id="react-root"]/div[2]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div/p/text()').extract_first()

        try:
            self.writer.writerow([link,titulo,descricao,ingredientes,instrucao,porcao])

        except Exception as e:
            print(e)
