import Sdkrindegastos
import json

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjEiLCJjb21wYW55X2lkIjoiMTA5IiwicmFuZG9tIjoicmFuZEFQSTVhYTgzZTI4OWY0NWQzLjUwNDczNzY4In0.arDxsQlJlssjrUoh2Dx_72-wDm_RSYXDSO7s0pkFtIc"
r = Sdkrindegastos.Rindegastos(token)
params = {}

params["Status"] = "1"
params["OrderBy"] = "1"
params["Order"] = "ASC"
params["ResultsPerPage"] = "100"
params["Page"] = "1"

try:
    policiesResult = r.getExpensePolicies(params)
    print(policiesResult.status)
    print(policiesResult.reason)
    print(policiesResult.read())
except ValueError:
    print(ValueError)