# -*- coding: utf-8 -*-
import scrapy
import numpy
import quandl
from mykgb import indicator
from myapp.models import Quandlset
from mykgb.items import MykgbItem

quandl.ApiConfig.api_key = "taJyZN8QXqj2Dj8SNr6Z"
quandl.ApiConfig.api_version = '2015-04-09'


class QuandlDataSpider(scrapy.Spider):
    name = "quandl_data"
    allowed_domains = ["www.baidu.com"]
    start_urls = ['http://www.baidu.com/']

    custom_settings = {