from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['get'])
def test_mock():
    return {
        "code": "success",
        "data": [{"accountId": "64", "cvr": 0.56, "name": "祁少涛", "poc": 1000, "portrait": "", "qty": 5},
                 {"accountId": "64", "cvr": 0.66, "name": "祁少涛1", "poc": 1000, "portrait": "", "qty": 500}],
        "msg": "success",
        "responseTime": "2023-03-06 16:50:22",
        "success": True,
        "traceId": "iR6cReN2cDtHAXxPkOVni"}


@app.route('/1', methods=['get'])
def test_mock1():
    """
    接口URL:  http://shop-pre.vecverse.com/api/personal/dashboard/sales/ranking?orderBy=qty&date=2023-03
    :return:成单量
    """
    return {
        "code": "success",
        "data": [{"accountId": "1", "cvr": 0.56456666, "name": "祁", "poc": 1000, "portrait": "", "qty": 5},
                 {"accountId": "2", "cvr": 0.14258369, "name": "祁1", "poc": 1000, "portrait": "", "qty": 500},
                 {"accountId": "63", "cvr": 0.1253666, "name": "祁1", "poc": 1000, "portrait": "", "qty": 500},
                 {"accountId": "64", "cvr": 0.7896655456, "name": "祁1", "poc": 1000, "portrait": "", "qty": 500},
                 {"accountId": "65", "cvr": 0.39877456, "name": "祁1", "poc": 1000, "portrait": "", "qty": 500},
                 {"accountId": "74", "cvr": 0.925564411, "name": "祁1", "poc": 1000, "portrait": "", "qty": 500}, ],
        "msg": "success",
        "responseTime": "2023-03-06 16:50:22",
        "success": True,
        "traceId": "iR6cReN2cDtHAXxPkOVni"
    }


@app.route('/2', methods=['get'])
def test_mock2():
    """
    接口地址:   http://shop-pre.vecverse.com/api/personal/dashboard/order/count-amount/bar?dimension=5&day=2023-03
    :return:日均订单
    """
    return {
        "code": "success",
        "data": {"xAix": ["2023-03-01", "2023-03-02", "2023-03-03", "2023-03-04", "2023-03-05", "2023-03-06", "2023-03-07", "2023-03-08", "2023-03-09", "2023-03-10", "2023-03-11", "2023-03-12",
                          "2023-03-13", "2023-03-14", "2023-03-15", "2023-03-16", "2023-03-17", "2023-03-18", "2023-03-19", "2023-03-20", "2023-03-21", "2023-03-22", "2023-03-23", "2023-03-24",
                          "2023-03-25", "2023-03-26", "2023-03-27", "2023-03-28", "2023-03-29", "2023-03-30", "2023-03-31"],
                 "yAixs": [[1, 222, 3, 4, 5, 466, 7, 618, 9, 160, 20, 30, 40, 50, 60, 770, 80, 90, 100, 80, 70, 40, 490, 40, 50, 660, 70, 80, 90, 990, 1000],
                           [10000, 134807400, 6700014732, 77004172, 87004172, 3028860360, 610004172, 207004172, 3070045172, 407004172, 5070054172, 6070054172,
                            670004172, 97004172, 670004172, 670004172, 6700540172, 67004172, 6720084172, 670041782, 670034172, 6700941472, 670041472, 670054172,
                            670804172, 6700474172, 670774172, 670074172, 667004172, 670064172, 67004172]]},
        "msg": "success",
        "responseTime": "2023-03-08 15:55:04",
        "success": True,
        "traceId": "-sB-pElfraVDGNCztDXq2"
    }


@app.route('/3', methods=['get'])
def test_mock3():
    """
    接口URL:  http://shop-pre.vecverse.com/api/personal/dashboard/order/quarter/spu/category/ratio?year=2023
    :return: 产品季度销量
    """
    return {
        "code": "success",
        "data": {"quarters": ["2023-1", "2023-2", "2023-3", "2023-4"],
                 "ratios": [{"label": "移液设备", "total": 6516, "values": [65516, 22250, 33350, 44540]},
                            {"label": "样本管理", "total": 18031, "values": [18031, 66660, 67780, 89440]},
                            {"label": "环境感知", "total": 22072, "values": [22072, 45450, 87780, 31230]},
                            {"label": "检测仪器", "total": 7, "values": [7999, 7809, 6555, 25890]}]},
        "msg": "success",
        "responseTime": "2023-03-08 16:15:34",
        "success": True,
        "traceId": "CNBzUu6NJbl3WilSqB8JX"
    }


@app.route('/4', methods=['get'])
def test_mock4():
    """
    接口URL:  http://shop-pre.vecverse.com/api/personal/dashboard/order/spu/ratio?year=2023
    :return: 产品类别比例
    """
    return {
        "code": "success",
        "data": {"labels": ["无探头高温传感器", "无探头低温传感器", "半柔性温度传感器", "双半柔性温度传感器", "刚性温度传感器", "其他"],
                 "total": 1000,
                 "values": [200, 200, 200, 200, 200, 200]},
        "msg": "success", "responseTime": "2023-03-10 16:30:52", "success": True, "traceId": "aoQVY9q8TCXtJzrHSs-HS"
    }


@app.route('/5', methods=['get'])
def test_mock5():
    """
    接口URL:  http://shop-pre.vecverse.com/api/personal/dashboard/order/amount?dimension=5&date=2023-03-14&needLast7Day=True
    :return: 今日交易额
    """
    return {
        "code": "success",
        "data": {"last7Day":
                     {"xAxis": ["2023-03-07", "2023-03-08", "2023-03-09", "2023-03-10", "2023-03-11", "2023-03-12", "2023-03-13", "2023-03-14"],
                      "yAxis": [1800, 507, 507, 420, 220, 666, 870, 430]
                      },
                 "lastCycleTotal": "23234242340",
                 "linkRelativeRatio": -1.59,
                 "total": "123456789"},
        "msg": "success", "responseTime": "2023-03-14 10:03:07", "success": True, "traceId": "Goo4N9HG3M55-bqsO1GH6"
    }


@app.route('/6', methods=['get'])
def test_mock6():
    """
    接口URL:  http://shop-pre.vecverse.com/api/personal/dashboard/order/count?dimension=5&date=2023-03-14&needLast7Day=True
    :return: 今日成单量
    """
    return {
        "code": "success",
        "data": {"last7Day":
                     {"xAxis": ["2023-03-07", "2023-03-08", "2023-03-09", "2023-03-10", "2023-03-11", "2023-03-12", "2023-03-13", "2023-03-14"],
                      "yAxis": [430, 507, 507, 420, 220, 666, 870, 1800]
                      },
                 "lastCycleTotal": "23234242340",
                 "linkRelativeRatio": 1.79,
                 "total": "987654321"},
        "msg": "success", "responseTime": "2023-03-14 10:29:25", "success": True, "traceId": "1jrPFEazvrZ0Vy2DkU5F8"
    }


@app.route('/7', methods=['get'])
def test_mock7():
    """
    接口URL:  http://shop-pre.vecverse.com/api/personal/dashboard/purchase/count?dimension=5&date=2023-03-14&needLast7Day=True
    :return: 今日采购清单量
    """
    return {
        "code": "success",
        "data": {"last7Day":
                     {"xAxis": ["2023-03-07", "2023-03-08", "2023-03-09", "2023-03-10", "2023-03-11", "2023-03-12", "2023-03-13", "2023-03-14"],
                      "yAxis": [100, 200, 308, 450, 50, 60, 700, 80]
                      },
                 "lastCycleTotal": "23234242340",
                 "linkRelativeRatio": 0.669455638563863,
                 "total": "147258369"},
        "msg": "success", "responseTime": "2023-03-14 10:29:25", "success": True, "traceId": "1jrPFEazvrZ0Vy2DkU5F8"
    }


@app.route('/8', methods=['get'])
def test_mock8():
    """
    接口URL:  http://shop-pre.vecverse.com/api/personal/dashboard/order/amount?dimension=1&date=2023-03-14&needLast7Day=False
    :return: 本年度订单金额
    """
    return {
        "code": "success",
        "data": {"last7Day": None, "lastCycleTotal": "55555", "linkRelativeRatio": None, "total": "987456258"},
        "msg": "success", "responseTime": "2023-03-14 10:51:16", "success": True, "traceId": "L9mj7KsAIVwqnbAT5cjWi"
    }


@app.route('/9', methods=['get'])
def test_mock9():
    """
    接口URL:  http://shop-pre.vecverse.com/api/personal/dashboard/order/count?dimension=1&date=2023-03-14&needLast7Day=False
    :return: 本年度订单量
    """
    return {
        "code": "success",
        "data": {"last7Day": None, "lastCycleTotal": 987, "linkRelativeRatio": None, "total": 1024},
        "msg": "success", "responseTime": "2023-03-14 10:57:53", "success": True, "traceId": "UpIHe6w7IhxPm0X-54ZVU"
    }


@app.route('/shopping_cart', methods=['Get'])
def Shopping_Cart():
    """
    接口URL:  http://shop-pre.vecverse.com/api/personal/cart/page
    :return: 购物车
    """
    data = {
        "previewItems": [{"picture": "//shop-oss.vecverse.com/product/ZbcpGbjVJz87zMKXEfbyX.png", "skuId": "86"},
                         {"picture": "//shop-oss.vecverse.com/product/y35V3a4gJAnEIKZPsXIMm.png", "skuId": "87"},
                         {"picture": "//shop-oss.vecverse.com/product/7CiY_0TFt-fQr6MrxAqcN.png", "skuId": "92"},
                         {"picture": "//shop-oss.vecverse.com/product/pL9mLFn573vwJiL_T6MIQ.png", "skuId": "93"},
                         {"picture": "//shop-oss.vecverse.com/product/SP8j7CmzS6xd3-U9x96Ma.png", "skuId": "101"},
                         {"picture": "//shop-oss.vecverse.com/product/dfzs_N8eeCdYDqhUsVfHD.png", "skuId": "102"},
                         {"picture": "//shop-oss.vecverse.com/product/2UTn8qS4MjAJO31_rOC5w.png", "skuId": "103"},
                         {"picture": "//shop-oss.vecverse.com/product/qNubqGP8uCdqnZpZqgT_n.png", "skuId": "106"},
                         {"picture": "//shop-oss.vecverse.com/product/3iXfBem15cDurTueS6idm.png", "skuId": "110"},
                         {"picture": "//shop-oss.vecverse.com/product/i_t2s_dt7eD69hL85hdQQ.png", "skuId": "112"},
                         {"picture": "//shop-oss.vecverse.com/product/-nbyF5rfye0KOexnUvl8U.png", "skuId": "114"}]}
    return {
        "code": "success", "data": {"countId": "", "current": 1, "maxLimit": None, "optimizeCountSql": True, "orders": [], "pages": 1, "records": [
            {"englishName": "Vecsee", "gmtCreate": "2023-03-14 16:57:59", "historyPrice": 587955, "id": "710", "invalid": True, "isFav": True, "lowStock": 0, "price": 6000, "productId": "44",
             "productName": "AI智能液位仪", "productPictures": ["//shop-oss.vecverse.com/product/kaAtMV9iF1-vstiuw-DAB.png"], "productQuantity": 1, "productSn": "Vecverse-230", "skuCode": "230-0001",
             "skuId": "114", "skuPictures": "", "skuSpecs": "[{\"k\": \"类型\", \"v\": \"液氮检测\"}]", "skuTaxFee": 67641, "state": 1, "stockTag": 2, "taxRate": 0.13, "totalTaxFee": 67641},
            {"englishName": "Pscanner", "gmtCreate": "2023-03-14 16:57:53", "historyPrice": 693405, "id": "709", "invalid": True, "isFav": False, "lowStock": 0, "price": 200, "productId": "42",
             "productName": "手持扫描仪", "productPictures": ["//shop-oss.vecverse.com/product/siADgvHF_IPAIcP8xIjpf.png"], "productQuantity": 1, "productSn": "Vecverse-222", "skuCode": "222-0001",
             "skuId": "112", "skuPictures": "", "skuSpecs": "[{\"k\": \"类型\", \"v\": \"RFID\"}]", "skuTaxFee": 79773, "state": 1, "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 79773},
            {"englishName": "Pstation", "gmtCreate": "2023-03-14 16:57:47", "historyPrice": 13584905, "id": "708", "invalid": True, "isFav": False, "lowStock": 0, "price": 3111, "productId": "41",
             "productName": "移动式智能工作站", "productPictures": ["//shop-oss.vecverse.com/product/iE3ka76qChn9jfR1GDT-e.png"], "productQuantity": 1, "productSn": "Vecverse-223",
             "skuCode": "223-0001", "skuId": "111", "skuPictures": "", "skuSpecs": "[{\"k\": \"类型\", \"v\": \"移动式工作站\"}]", "skuTaxFee": 1562866, "state": 1, "stockTag": 1, "taxRate": 0.13,
             "totalTaxFee": 1562866},
            {"englishName": "", "gmtCreate": "2023-03-14 16:57:41", "historyPrice": 436905, "id": "707", "invalid": True, "isFav": False, "lowStock": 0, "price": 855, "productId": "40",
             "productName": "可定位温度传感器", "productPictures": ["//shop-oss.vecverse.com/product/ygk6TR7-zoRMnI4mKqCge.png"], "productQuantity": 1, "productSn": "Vecverse-370",
             "skuCode": "370-0001", "skuId": "110", "skuPictures": "", "skuSpecs": "[{\"k\": \"类型\", \"v\": \"可定位\"}]", "skuTaxFee": 50264, "state": 1, "stockTag": 1, "taxRate": 0.13,
             "totalTaxFee": 50264},
            {"englishName": "", "gmtCreate": "2023-03-14 16:57:36", "historyPrice": 408405, "id": "706", "invalid": True, "isFav": False, "lowStock": 0, "price": 6666666, "productId": "39",
             "productName": "迷你温度传感器", "productPictures": ["//shop-oss.vecverse.com/product/uWXsHurtEX30V2VrN_fnm.png"], "productQuantity": 1, "productSn": "Vecverse-360",
             "skuCode": "360-0001", "skuId": "109", "skuPictures": "", "skuSpecs": "[{\"k\": \"类型\", \"v\": \"迷你\"}]", "skuTaxFee": 46985, "state": 1, "stockTag": 1, "taxRate": 0.13,
             "totalTaxFee": 46985},
            {"englishName": "", "gmtCreate": "2023-03-14 16:57:30", "historyPrice": 568860, "id": "705", "invalid": True, "isFav": False, "lowStock": 0, "price": 568860, "productId": "36",
             "productName": "刚性温度传感器", "productPictures": ["//shop-oss.vecverse.com/product/waT7uEI8C_4gxRJYXnqRP.png"], "productQuantity": 1, "productSn": "Vecverse=340",
             "skuCode": "340-0001", "skuId": "106", "skuPictures": "", "skuSpecs": "[{\"k\": \"探头类型\", \"v\": \"刚性\"}]", "skuTaxFee": 65445, "state": 1, "stockTag": 1, "taxRate": 0.13,
             "totalTaxFee": 65445},
            {"englishName": "", "gmtCreate": "2023-03-14 16:57:25", "historyPrice": 568860, "id": "704", "invalid": True, "isFav": True, "lowStock": 0, "price": 568860, "productId": "35",
             "productName": "双半柔性温度传感器", "productPictures": ["//shop-oss.vecverse.com/product/1PsBOE4_MMPNr7maMHBLR.png"], "productQuantity": 1, "productSn": "Vecverse-331",
             "skuCode": "331-0001", "skuId": "105", "skuPictures": "", "skuSpecs": "[{\"k\": \"探头类型\", \"v\": \"双半柔性\"}]", "skuTaxFee": 65445, "state": 1, "stockTag": 1, "taxRate": 0.13,
             "totalTaxFee": 65445},
            {"englishName": "", "gmtCreate": "2023-03-14 16:57:20", "historyPrice": 521455, "id": "703", "invalid": True, "isFav": False, "lowStock": 0, "price": 521455, "productId": "34",
             "productName": "半柔性温度传感器", "productPictures": ["//shop-oss.vecverse.com/product/wPZTc2uTGNr7SMfCiPieW.png"], "productQuantity": 1, "productSn": "Vecverse-330",
             "skuCode": "330-0001", "skuId": "104", "skuPictures": "", "skuSpecs": "[{\"k\": \"探头类型\", \"v\": \"半柔性\"}]", "skuTaxFee": 59991, "state": 1, "stockTag": 1, "taxRate": 0.13,
             "totalTaxFee": 59991},
            {"englishName": "", "gmtCreate": "2023-03-14 16:57:16", "historyPrice": 379905, "id": "702", "invalid": True, "isFav": False, "lowStock": 0, "price": 379905, "productId": "33",
             "productName": "无探头低温传感器", "productPictures": ["//shop-oss.vecverse.com/product/vV6QzDaQzRYUbpCwIewGJ.png"], "productQuantity": 1, "productSn": "Vecverse-321",
             "skuCode": "321-0001", "skuId": "103", "skuPictures": "", "skuSpecs": "[{\"k\": \"温度类型\", \"v\": \"低温\"}, {\"k\": \"探头类型\", \"v\": \"无探头\"}]", "skuTaxFee": 43706, "state": 1,
             "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 43706},
            {"englishName": "", "gmtCreate": "2023-03-14 16:57:11", "historyPrice": 579405, "id": "701", "invalid": True, "isFav": False, "lowStock": 0, "price": 579405, "productId": "32",
             "productName": "无探头高温传感器", "productPictures": ["//shop-oss.vecverse.com/product/Qam_fDef6xG-wm-a9Zr92.png"], "productQuantity": 1, "productSn": "Vecverse-320",
             "skuCode": "320-1000", "skuId": "102", "skuPictures": "", "skuSpecs": "[{\"k\": \"温度类型\", \"v\": \"高温\"}, {\"k\": \"探头类型\", \"v\": \"无探头\"}]", "skuTaxFee": 66658, "state": 1,
             "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 66658},
            {"englishName": "Micro", "gmtCreate": "2023-03-14 16:57:04", "historyPrice": 2849905, "id": "700", "invalid": True, "isFav": False, "lowStock": 0, "price": 2849905, "productId": "31",
             "productName": "小型酶标仪", "productPictures": ["//shop-oss.vecverse.com/product/7W8SnSOx7djeViwdLGzME.png"], "productQuantity": 1, "productSn": "Vecverse-400", "skuCode": "400-0001",
             "skuId": "101", "skuPictures": "", "skuSpecs": "[{\"k\": \"型号\", \"v\": \"Micro\"}]", "skuTaxFee": 327866, "state": 1, "stockTag": 2, "taxRate": 0.13, "totalTaxFee": 327866},
            {"englishName": "@Pette Pro", "gmtCreate": "2023-03-14 16:56:59", "historyPrice": 693405, "id": "696", "invalid": True, "isFav": False, "lowStock": 0, "price": 693405, "productId": "27",
             "productName": "8通道电动移液器", "productPictures": ["//shop-oss.vecverse.com/product/25Ota8OD1KuEuorLf87cI.png"], "productQuantity": 1, "productSn": "Vecverse-111",
             "skuCode": "111-0010", "skuId": "90", "skuPictures": "", "skuSpecs": "[{\"k\": \"型号\", \"v\": \"8通道\"}, {\"k\": \"量程\", \"v\": \"0.5 µL – 10 µL\"}]", "skuTaxFee": 79773, "state": 1,
             "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 79773},
            {"englishName": "@Pette Pro", "gmtCreate": "2023-03-14 16:56:59", "historyPrice": 693405, "id": "697", "invalid": True, "isFav": False, "lowStock": 0, "price": 693405, "productId": "27",
             "productName": "8通道电动移液器", "productPictures": ["//shop-oss.vecverse.com/product/25Ota8OD1KuEuorLf87cI.png"], "productQuantity": 1, "productSn": "Vecverse-111",
             "skuCode": "111-0100", "skuId": "91", "skuPictures": "", "skuSpecs": "[{\"k\": \"型号\", \"v\": \"8通道\"}, {\"k\": \"量程\", \"v\": \"5 µL – 100 µL\"}]", "skuTaxFee": 79773, "state": 1,
             "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 79773},
            {"englishName": "@Pette Pro", "gmtCreate": "2023-03-14 16:56:59", "historyPrice": 693405, "id": "698", "invalid": True, "isFav": False, "lowStock": 0, "price": 693405, "productId": "27",
             "productName": "8通道电动移液器", "productPictures": ["//shop-oss.vecverse.com/product/25Ota8OD1KuEuorLf87cI.png"], "productQuantity": 1, "productSn": "Vecverse-111",
             "skuCode": "111-0300", "skuId": "92", "skuPictures": "", "skuSpecs": "[{\"k\": \"型号\", \"v\": \"8通道\"}, {\"k\": \"量程\", \"v\": \"30 µL – 300 µL\"}]", "skuTaxFee": 79773, "state": 1,
             "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 79773},
            {"englishName": "@Pette Pro", "gmtCreate": "2023-03-14 16:56:59", "historyPrice": 693405, "id": "699", "invalid": True, "isFav": False, "lowStock": 0, "price": 693405, "productId": "27",
             "productName": "8通道电动移液器", "productPictures": ["//shop-oss.vecverse.com/product/25Ota8OD1KuEuorLf87cI.png"], "productQuantity": 1, "productSn": "Vecverse-111",
             "skuCode": "111-1000", "skuId": "93", "skuPictures": "", "skuSpecs": "[{\"k\": \"型号\", \"v\": \"8通道\"}, {\"k\": \"量程\", \"v\": \"50 µL – 1000 µL\"}]", "skuTaxFee": 79773,
             "state": 1, "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 79773},
            {"englishName": "@Pette Pro", "gmtCreate": "2023-03-14 16:56:51", "historyPrice": 369905, "id": "692", "invalid": True, "isFav": True, "lowStock": 0, "price": 369905, "productId": "26",
             "productName": "单通道电动移液器", "productPictures": ["//shop-oss.vecverse.com/product/UEPoYbigqMP4DsmpN5NRx.png"], "productQuantity": 1, "productSn": "Vecverse-110",
             "skuCode": "110-0010", "skuId": "86", "skuPictures": "", "skuSpecs": "[{\"k\": \"型号\", \"v\": \"单通道\"}, {\"k\": \"量程\", \"v\": \"0.5µL — 10µL\"}]", "skuTaxFee": 42556, "state": 1,
             "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 42556},
            {"englishName": "@Pette Pro", "gmtCreate": "2023-03-14 16:56:51", "historyPrice": 379905, "id": "693", "invalid": True, "isFav": True, "lowStock": 0, "price": 379905, "productId": "26",
             "productName": "单通道电动移液器", "productPictures": ["//shop-oss.vecverse.com/product/UEPoYbigqMP4DsmpN5NRx.png"], "productQuantity": 1, "productSn": "Vecverse-110",
             "skuCode": "110-0100", "skuId": "87", "skuPictures": "", "skuSpecs": "[{\"k\": \"型号\", \"v\": \"单通道\"}, {\"k\": \"量程\", \"v\": \"5µL — 100µL\"}]", "skuTaxFee": 43706, "state": 1,
             "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 43706},
            {"englishName": "@Pette Pro", "gmtCreate": "2023-03-14 16:56:51", "historyPrice": 379905, "id": "694", "invalid": True, "isFav": False, "lowStock": 0, "price": 379905, "productId": "26",
             "productName": "单通道电动移液器", "productPictures": ["//shop-oss.vecverse.com/product/UEPoYbigqMP4DsmpN5NRx.png"], "productQuantity": 1, "productSn": "Vecverse-110",
             "skuCode": "110-0300", "skuId": "88", "skuPictures": "", "skuSpecs": "[{\"k\": \"型号\", \"v\": \"单通道\"}, {\"k\": \"量程\", \"v\": \"30µL — 300µL\"}]", "skuTaxFee": 43706, "state": 1,
             "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 43706},
            {"englishName": "@Pette Pro", "gmtCreate": "2023-03-14 16:56:51", "historyPrice": 379905, "id": "695", "invalid": True, "isFav": False, "lowStock": 0, "price": 379905, "productId": "26",
             "productName": "单通道电动移液器", "productPictures": ["//shop-oss.vecverse.com/product/UEPoYbigqMP4DsmpN5NRx.png"], "productQuantity": 1, "productSn": "Vecverse-110",
             "skuCode": "110-1000", "skuId": "89", "skuPictures": "", "skuSpecs": "[{\"k\": \"型号\", \"v\": \"单通道\"}, {\"k\": \"量程\", \"v\": \"50µL — 1000µL\"}]", "skuTaxFee": 43706, "state": 1,
             "stockTag": 1, "taxRate": 0.13, "totalTaxFee": 43706}],
            "searchCount": True, "size": 1000, "total": 19}, "msg": "success", "responseTime": "2023-03-14 16:58:21", "success": True,"traceId": "5sspuYWRvxGkQ71aTf8Z8"
    }


app.run(host='192.168.110.49', port=8088)
