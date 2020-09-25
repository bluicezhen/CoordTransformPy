# MapDatumTrans

[简体中文](https://github.com/bluicezhen/MapDatumTrans/blob/master/README-cn.md)

> MapDatumTranss is a transformer for map datum，include WGS84, GCJ-02 and BD-09.

## Install：

```bash
pip install MapDatumTrans
```

## Demo：

```bash
import MapDatumTrans

MapDatumTrans.gcj02_to_bd09(lat, lon)   # GCJ02 to BD-09
MapDatumTrans.bd09_to_gcj02(lat, lon)   # BD-09 to GCJ02
MapDatumTrans.wgs84_to_gcj02(lat, lon)  # WGS84 to GCJ02
MapDatumTrans.gcj02_to_wgs84(lat, lon)  # GCJ02 to WGS84
MapDatumTrans.bd09_to_wgs84(lat, lon)   # BD-09 to WGS84
MapDatumTrans.wgs84_to_bd09(lat, lon)   # WGS84 to BD-09
```