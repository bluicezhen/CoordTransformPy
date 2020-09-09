# 坐标转换模块

此模块用于百度坐标系(bd-09)、火星坐标系(国测局坐标系、gcj02)、WGS84坐标系的相互转换，并提供中文地址到坐标的转换功能，仅使用Python标准模块，无其他依赖。

需要js版本可以移步[coordtransform](https://github.com/wandergis/coordtransform)

## 使用说明(coordTransform_utils.py)

### 方法说明

```bash
# 方法说明
gcj02_to_bd09(lng, lat) # 火星坐标系->百度坐标系
bd09_to_gcj02(lng, lat) # 百度坐标系->火星坐标系
wgs84_to_gcj02(lng, lat) # WGS84坐标系->火星坐标系
gcj02_to_wgs84(lng, lat) # 火星坐标系->WGS84坐标系
bd09_to_wgs84(lng, lat) # 百度坐标系->WGS84坐标系
wgs84_to_bd09(lng, lat) # WGS84坐标系->百度坐标系

# 中文地址到火星坐标系, 需要高德地图API Key
g = Geocoding('API_KEY')  # 这里填写你的高德Api_Key
g.geocode('北京市朝阳区朝阳公园')
```