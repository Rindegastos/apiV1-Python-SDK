import Sdkrindegastos
import json

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjEiLCJjb21wYW55X2lkIjoiMTA5IiwicmFuZG9tIjoicmFuZEFQSTVhYTgzZTI4OWY0NWQzLjUwNDczNzY4In0.arDxsQlJlssjrUoh2Dx_72-wDm_RSYXDSO7s0pkFtIc"
r = Sdkrindegastos.Rindegastos(token)

params = {}
params["Id"] = "6582"
params["IdAdmin"] = "61"
params["DepositAmount"] = 11000

encoded = json.dumps(params)

try:
    reportResult = r.depositMoneyToFund(encoded)
    print(reportResult.status)
    print(reportResult.reason)
    print(reportResult.read())
except ValueError:
    print(ValueError)
