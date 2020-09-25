# MapDatumTrans

> 一个简单的python坐标转换库，支持WGS84, GCJ-02 and BD-09

## 安装：

```bash
pip install MapDatumTrans
```

## 使用：

```bash
import MapDatumTrans

MapDatumTrans.gcj02_to_bd09(lat, lon)   # GCJ02坐标系 转换为 BD-09坐标系
MapDatumTrans.bd09_to_gcj02(lat, lon)   # BD-09坐标系 转换为 GCJ02坐标系
MapDatumTrans.wgs84_to_gcj02(lat, lon)  # WGS84坐标系 转换为 GCJ02坐标系
MapDatumTrans.gcj02_to_wgs84(lat, lon)  # GCJ02坐标系 转换为 WGS84坐标系
MapDatumTrans.bd09_to_wgs84(lat, lon)   # BD-09坐标系 转换为 WGS84坐标系
MapDatumTrans.wgs84_to_bd09(lat, lon)   # WGS84坐标系 转换为 BD-09坐标系
```