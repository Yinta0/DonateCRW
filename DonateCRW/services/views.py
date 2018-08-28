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
    RPC_URL = os.getenv("RPC_URL")

    #Check crownd for info
    payload = json.dumps({"method": method, "params": params})
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    try:
        response = requests.request("POST", RPC_URL, data=payload, headers=headers, auth=(RPC_USER, RPC_PHRASE))
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
        PHRASE = os.getenv("PHRASE")
        #Check crown needed
        needed = service.crw_donate - balance

        #Check for finish project
        if balance >= service.crw_donate:
            #send tx
            timeout = 5

            #Set True on completed and save
            service.completed = True
            service.save()

            #Unblock wallet, settxfee and send the tx at wallet shop.
            answer = instruct_wallet('walletpassphrase', [PHRASE, timeout])
            set_txfee = instruct_wallet('settxfee', [0.00000007])
            send_tx = instruct_wallet("sendfrom", [str(service.title), str(service.wallet_shop), 1]) #Cambiar ammount
            print(send_tx)

        else:
            #Update balance for project
            service.amount_needed = needed
            service.amount_donate = balance
            service.save()

    return render(request, "services/services.html", {'services':services})


    
def completed(request):
    #Show all services, html check if true or false
    services = Service.objects.all()

    return render(request, "services/completed.html", {'services':services})