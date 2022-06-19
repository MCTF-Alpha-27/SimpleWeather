from setuptools import setup
from SimpleWeather import __version__ as v

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name = "SimpleWeather",
    version = v,
    py_modules = ["SimpleWeather"],
    author = "Jerry0940",
    author_email = "j13816180940@139.com",
    license = "MIT",
    description = "一个简单的天气爬虫，可以获取某个城市简单的天气信息",
    long_description = long_description,
    url = "https://github.com/MCTF-Alpha-27/SimpleWeather",
    long_description_content_type = "text/markdown",
    requires= [
        "requests"
    ],
    classifiers = [
       "Programming Language :: Python :: 3"
    ],
)