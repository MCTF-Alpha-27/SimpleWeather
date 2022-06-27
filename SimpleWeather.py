import requests
import json
import re

__all__ = ["get_weather"]

__author__ = "Jerry"
__version__ = "1.0.3"

def get_weather(name, *, write_json=False, json_path="./weather_info.json"):
    """
    获取一个城市的天气数据，返回一个字典

    设置 write_json=True 可以将数据写入json文件

    设置 json_path 可以更改json文件的名称和保存位置，默认为同级目录下的 weather_info.json
    """
    url = "http://wthrcdn.etouch.cn/weather_mini"
    response = requests.get(url, {"city": name})
    result = json.loads(response.content.decode())
    data = result.get("data")

    number_only = re.compile("[0-9]+")

    today = data.get("forecast")[0]
    today_date = today.get("date")
    today_high = number_only.search(today.get("high")).group()
    today_low = number_only.search(today.get("low")).group()
    today_fengli = today.get("fengli").replace("<![CDATA[", "").replace("]]>", "")
    today_fengxiang = today.get("fengxiang")
    today_type = today.get("type")
    today_info = {
        "日期": today_date,
        "最高温度": today_high,
        "最低温度": today_low,
        "风力": today_fengli,
        "风向": today_fengxiang,
        "天气": today_type
    }

    yesterday = data.get("yesterday")
    yesterday_date = yesterday.get("date")
    yesterday_high = number_only.search(yesterday.get("high")).group()
    yesterday_low = number_only.search(yesterday.get("low")).group()
    yesterday_fl = yesterday.get("fl").replace("<![CDATA[", "").replace("]]>", "")
    yesterday_fx = yesterday.get("fx")
    yesterday_type = yesterday.get("type")
    yesterday_info = {
        "日期": yesterday_date,
        "最高温度": yesterday_high,
        "最低温度": yesterday_low,
        "风力": yesterday_fl,
        "风向": yesterday_fx,
        "天气": yesterday_type
    }

    weather_info = {
        "today": today_info,
        "yesterday": yesterday_info
    }

    if json_path != "./weather_info.json" and not write_json:
        raise UserWarning(
            "如果没有设置 write_json=True，更改 json_path 的值是无意义的"
        )

    if write_json:
        with open(json_path, "w") as f:
            json.dump(weather_info, f, sort_keys=True, indent=4, separators=(',',': '), ensure_ascii=False)
    
    return weather_info

if __name__ == "__main__":
    print(get_weather("上海", write_json=True))