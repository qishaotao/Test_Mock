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
    return {
        "code": "success",
        "data": [{"accountId": "1", "cvr": 0.56456666, "name": "祁少涛", "poc": 1000, "portrait": "", "qty": 5},
                 {"accountId": "2", "cvr": 0.14258369, "name": "祁少涛1", "poc": 1000, "portrait": "", "qty": 500},
                 {"accountId": "63", "cvr": 0.1253666, "name": "祁少涛1", "poc": 1000, "portrait": "", "qty": 500},
                 {"accountId": "64", "cvr": 0.7896655456, "name": "祁少涛1", "poc": 1000, "portrait": "", "qty": 500},
                 {"accountId": "65", "cvr": 0.39877456, "name": "祁少涛1", "poc": 1000, "portrait": "", "qty": 500},
                 {"accountId": "74", "cvr": 0.925564411, "name": "祁少涛1", "poc": 1000, "portrait": "", "qty": 500}, ],
        "msg": "success",
        "responseTime": "2023-03-06 16:50:22",
        "success": True,
        "traceId": "iR6cReN2cDtHAXxPkOVni"
    }


@app.route('/2', methods=['get'])
def test_mock2():
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
    return {
        "code": "success",
        "data": {"quarters": ["2023-1", "2023-2", "2023-3", "2023-4"],
                 "ratios": [{"label": "移液设备", "total": 6516, "values": [6516, 2220, 3330, 4440]},
                            {"label": "样本管理", "total": 18031, "values": [18031, 66660, 67780, 89440]},
                            {"label": "环境感知", "total": 22072, "values": [22072, 45450, 87780, 31230]},
                            {"label": "检测仪器", "total": 7, "values": [7999, 7809, 6555, 25890]}]},
        "msg": "success",
        "responseTime": "2023-03-08 16:15:34",
        "success": True,
        "traceId": "CNBzUu6NJbl3WilSqB8JX"
    }


app.run()
