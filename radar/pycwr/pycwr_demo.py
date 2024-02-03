import numpy as np
from pycwr.io import read_auto  ## 识别雷达数据类型，并转化为pycwr内置的雷达数据存储格式PRD（Polarimetry Radar Data）类型

test_filename = r"data/input/Z_RADR_I_Z9898_20190828181529_O_DOR_SAD_CAP_FMT.bin.bz2"

def export_cr_to_geojson_data(filename):
    prd = read_auto(filename)

    lat = prd.fields[0].lat.values
    lon = prd.fields[0].lon.values

    # 起始值、结束值、格网宽度生成等差数列数组
    cell_width = 0.01   # wgs84坐标系，单位：度
    lon1d = np.arange(lon.min(), lon.max(), cell_width)
    lat1d = np.arange(lat.min(), lat.max(), cell_width)

    prd.add_product_CR_lonlat(XLon=lon1d, YLat=lat1d)   # 计算给定经纬度范围的组合反射率

    cr_geo_dict = prd.product.CR_geo.to_dict()

    coords = cr_geo_dict["coords"]
    coords_cr = cr_geo_dict.get("data")
    coords_lat_cr = coords.get("lat_cr").get("data")
    coords_lon_cr = coords.get("lon_cr").get("data")

    result_lon = []
    result_lat = []
    result_value = []
    invalid_value = -9999

    config = {
        "invalidValue" : invalid_value, # 无效值
        "cellWidth":cell_width # 格网cell width
    }
    for i, cr in enumerate(coords_cr):
        arr = []
        for j, c in enumerate(cr):
            if np.isnan(c):
                c = config["invalidValue"]
            result_lon.append(coords_lon_cr[j])
            result_lat.append(coords_lat_cr[j])
            arr.append(c)
        result_value.append(arr)


    print(len(coords_lon_cr))
    print(len(coords_lat_cr))
    print(len(result_value))

    result_dict = {
        "lon":coords_lon_cr,
        "lat":coords_lat_cr,
        "value":result_value,
        "config":config
    }

    file2 = open("data/output/wContourData_0.02.json", "w")  # write mode
    file2.write(str(result_dict))
    file2.close()

if __name__ == "__main__":
    export_cr_to_geojson_data(test_filename)
