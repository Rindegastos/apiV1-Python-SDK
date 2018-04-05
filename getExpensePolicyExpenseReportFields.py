import Sdkrindegastos
import json

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjEiLCJjb21wYW55X2lkIjoiMTA5IiwicmFuZG9tIjoicmFuZEFQSTVhYTgzZTI4OWY0NWQzLjUwNDczNzY4In0.arDxsQlJlssjrUoh2Dx_72-wDm_RSYXDSO7s0pkFtIc"
r = Sdkrindegastos.Rindegastos(token)

try:
    policiesResult = r.getExpensePolicyExpenseReportFields("4044")
    print(policiesResult.status)
    print(policiesResult.reason)
    print(policiesResult.read())
except ValueError:
    print(ValueError)