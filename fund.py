import Sdkrindegastos
import json

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjEiLCJjb21wYW55X2lkIjoiMTA5IiwicmFuZG9tIjoicmFuZEFQSTVhYTgzZTI4OWY0NWQzLjUwNDczNzY4In0.arDxsQlJlssjrUoh2Dx_72-wDm_RSYXDSO7s0pkFtIc"
r = Sdkrindegastos.Rindegastos(token)

params = {}
params["IdEmployee"] = "61"
params["IdAdmin"] = "61"
params["FundName"] = "Python"
params["FundCurrency"] = "CLP"
params["FundCode"] = "PPPP"
params["FundAmount"] = "10000"
params["FundComment"] = "Python commet"
params["FundFlexibility"] = "0"
params["FundAutoDeposit"] = "0"
params["FundAutoBlock"] = "0"
params["FundExpiration"] = "0"
params["FundExpirationDate"] = ""

encoded = json.dumps(params)

try:
    reportResult = r.createFund(encoded)
    print(reportResult.status)
    print(reportResult.reason)
    print(reportResult.read())
except ValueError:
    print(ValueError)
