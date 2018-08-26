from django.shortcuts import render
from .models import Service

import getpass
import json
import requests
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#Function for connect with Crownd
def instruct_wallet(method, params):

    #Set data for login
    RPC_USER = os.getenv("RPC_USER")
    RPC_PHRASE = os.getenv("RPC_PHRASE")

    #Check crownd for info
    url = "http://127.0.0.1:9341/"
    payload = json.dumps({"method": method, "params": params})
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    try:
        response = requests.request("POST", url, data=payload, headers=headers, auth=(RPC_USER, RPC_PHRASE))
        result = json.loads(response.text)
        return result
    except requests.exceptions.RequestException as e:
        print (e)
    except:
        print ('No response from Wallet, check Bitcoin is running on this machine')


def services(request):
    #Show all services
    services = Service.objects.all()

    #Check Balance for each service
    for service in services:

        balance = instruct_wallet('getbalance', [service.title])["result"]
        needed =service.crw_donate - balance

        PHRASE = os.getenv("PHRASE")

        #Check for finish project
        if balance >= service.crw_donate:
            #send tx
            timeout = 5

            answer = instruct_wallet('walletpassphrase', [PHRASE, timeout])
            set_txfee = instruct_wallet('settxfee', [0.00000007])
            send_tx = instruct_wallet("sendfrom", [str(service.title), str(service.wallet_shop), 1]) #Cambiar ammount
            print(send_tx)

        else:
            #Update balance for service
            service.amount_needed = needed
            service.amount_donate = balance
            service.save()

    return render(request, "services/services.html", {'services':services})


    
