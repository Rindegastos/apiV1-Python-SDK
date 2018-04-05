import Sdkrindegastos
import json

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjEiLCJjb21wYW55X2lkIjoiMTA5IiwicmFuZG9tIjoicmFuZEFQSTVhYTgzZTI4OWY0NWQzLjUwNDczNzY4In0.arDxsQlJlssjrUoh2Dx_72-wDm_RSYXDSO7s0pkFtIc"
r = Sdkrindegastos.Rindegastos(token)
params = {}

params["Since"] = "2017-10-01"
params["Until"] = "2017-10-26"
params["Currency"] = "CLP"
params["Status"] = "1"
params["Category"] = ""
params["ReportId"] = ""
params["ExpensePolicyId"] = ""
params["IntegrationStatus"] = ""
params["IntegrationCode"] = ""
params["IntegrationDate"] = ""
params["UserId"] = ""
params["OrderBy"] = ""
params["Order"] = ""
params["ResultsPerPage"] = ""
params["Page"] = ""

try:
    expenesResult = r.getExpenses(params)
    print(expenesResult.status)
    print(expenesResult.reason)
    print(expenesResult.read())
except ValueError:
    print(ValueError)