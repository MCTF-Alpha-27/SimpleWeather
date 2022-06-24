# SimpleWeather
一个简单的天气爬虫，可以获取某个城市简单的天气信息<br>
使用方法：
```
pip install SimpleWeather
```
实例：
```Python
import SimpleWeather as sw
shanghai = sw.get_weather("上海") # 获取上海的天气信息，返回一个字典
shanghai = shanghai["today"] # 获取上海当日温度信息
print(shanghai["最高温度"]) # 获取上海的最高温度
print(shanghai["最低温度"]) # 获取上海的最低温度
print(shanghai["风力"]) # 获取上海的风力
print(shanghai["风向"]) # 获取上海的风向
print(shanghai["天气"]) # 获取上海的天气

```
