import http.client
import socket

class Rindegastos:
    Token = ""
    Api = "api.rindegastos.com"
    def __init__(self,token):
        self.Token = token

    def getExpenses(self, Params):
        url = "/v1/getExpenses"
        
        control = 0
        
        try:
            for key in Params.keys():
                if Params[key] != "":
                    if control == 0:
                        url = url + "?"
                    elif control < len(Params.keys()):
                        url = url + "&"
                    
                    url = url + key + "=" + Params[key]

                control = control + 1

            conn = http.client.HTTPSConnection(self.Api)
            conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
            return conn.getresponse()
        except socket.gaierror:
            print('ignoring failed address lookup')
        
    
    def getExpense(self, Id):
        url = "/v1/getExpense?Id=" + Id
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
        return conn.getresponse()

    def setExpenseIntegration(self, putExpenseIntegration):
        url = "/v1/setExpenseIntegration"
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("PUT",url,putExpenseIntegration,headers={"Authorization": "Bearer "+ self.Token, "Content-type": "application/json"})
        return conn.getresponse()

    def getExpenseReports(self, Params):
        url = "/v1/getExpenseReports"
        
        control = 0
        
        try:
            for key in Params.keys():
                if Params[key] != "":
                    if control == 0:
                        url = url + "?"
                    elif control < len(Params.keys()):
                        url = url + "&"
                    
                    url = url + key + "=" + Params[key]

                control = control + 1

            conn = http.client.HTTPSConnection(self.Api)
            conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
            return conn.getresponse()
        except socket.gaierror:
            print('ignoring failed address lookup')

    def getExpenseReport(self, Id):
        url = "/v1/getExpenseReport?Id=" + Id
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
        return conn.getresponse()
    
    def setExpenseReportIntegration(self, putExpenseReportIntegration):
        url = "/v1/setExpenseReportIntegration"
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("POST",url,putExpenseReportIntegration,headers={"Authorization": "Bearer "+ self.Token, "Content-type": "application/json"})
        return conn.getresponse()

    def setExpenseReportCustomStatus(self, putExpenseReportCustomStatus):
        url = "/v1/setExpenseReportCustomStatus"
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("PUT",url,putExpenseReportCustomStatus,headers={"Authorization": "Bearer "+ self.Token, "Content-type": "application/json"})
        return conn.getresponse()
    
    def getFunds(self, Params):
        url = "/v1/getFunds"
        
        control = 0
        
        try:
            for key in Params.keys():
                if Params[key] != "":
                    if control == 0:
                        url = url + "?"
                    elif control < len(Params.keys()):
                        url = url + "&"
                    
                    url = url + key + "=" + Params[key]

                control = control + 1

            conn = http.client.HTTPSConnection(self.Api)
            conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
            return conn.getresponse()
        except socket.gaierror:
            print('ignoring failed address lookup')
    
    def getFund(self, Id):
        url = "/v1/getFund?Id=" + Id
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("GET", url, headers={"Authorization": "Bearer " + self.Token})
        return conn.getresponse()

    def createFund(self, postFund):
        url = "/v1/createFund"
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("POST",url,postFund,headers={"Authorization": "Bearer "+ self.Token, "Content-type": "application/json"})
        return conn.getresponse()
    
    def updateFund(self, putFund):
        url = "/v1/updateFund"
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("PUT",url,putFund,headers={"Authorization": "Bearer "+ self.Token, "Content-type": "application/json"})
        return conn.getresponse()

    def depositMoneyToFund(self, postDepositMoney):
        url = "/v1/depositMoneyToFund"
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("POST",url,postDepositMoney,headers={"Authorization": "Bearer "+ self.Token, "Content-type": "application/json"})
        return conn.getresponse()
    
    def withdrawMoneyFromFund(self, postWithdrawMoney):
        url = "/v1/withdrawMoneyFromFund"
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("POST",url,postWithdrawMoney,headers={"Authorization": "Bearer "+ self.Token, "Content-type": "application/json"})
        return conn.getresponse()

    def setFundStatus(self, putFundStatus):
        url = "/v1/setFundStatus"
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("PUT",url,putFundStatus,headers={"Authorization": "Bearer "+ self.Token, "Content-type": "application/json"})
        return conn.getresponse()

    def getExpensePolicies(self, Params):
        url = "/v1/getExpensePolicies"
        
        control = 0
        
        try:
            for key in Params.keys():
                if Params[key] != "":
                    if control == 0:
                        url = url + "?"
                    elif control < len(Params.keys()):
                        url = url + "&"
                    
                    url = url + key + "=" + Params[key]

                control = control + 1

            conn = http.client.HTTPSConnection(self.Api)
            conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
            return conn.getresponse()
        except socket.gaierror:
            print('ignoring failed address lookup')
        
    
    def getExpensePolicy(self, Id):
        url = "/v1/getExpensePolicy?Id=" + Id
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
        return conn.getresponse()

    def getExpensePolicyExpenseReportFields(self, Id):
        url = "/v1/getExpensePolicyExpenseReportFields?IdPolicy=" + Id
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
        return conn.getresponse()
    
    def getExpensePolicyExpenseFields(self, Id):
        url = "/v1/getExpensePolicyExpenseFields?IdPolicy=" + Id
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
        return conn.getresponse()
    
    def getExpensePolicyCategories(self, Id):
        url = "/v1/getExpensePolicyCategories?IdPolicy=" + Id
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
        return conn.getresponse()
    
    def getExpensePolicyWorkflow(self, Id):
        url = "/v1/getExpensePolicyWorkflow?IdPolicy=" + Id
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
        return conn.getresponse()
    
    def getExpensePolicyTaxes(self, Id):
        url = "/v1/getExpensePolicyTaxes?IdPolicy=" + Id
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
        return conn.getresponse()
    
    def getUsers(self, Params):
        url = "/v1/getUsers"
        
        control = 0
        
        try:
            for key in Params.keys():
                if Params[key] != "":
                    if control == 0:
                        url = url + "?"
                    elif control < len(Params.keys()):
                        url = url + "&"
                    
                    url = url + key + "=" + Params[key]

                control = control + 1

            conn = http.client.HTTPSConnection(self.Api)
            conn.request("GET",url,headers={"Authorization": "Bearer "+ self.Token})
            return conn.getresponse()
        except socket.gaierror:
            print('ignoring failed address lookup')
    
    def getUser(self, Id):
        url = "/v1/getUser?Id=" + Id
        conn = http.client.HTTPSConnection(self.Api)
        conn.request("GET", url, headers={"Authorization": "Bearer " + self.Token})
        return conn.getresponse()