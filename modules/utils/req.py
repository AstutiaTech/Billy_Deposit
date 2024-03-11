from typing import Dict
from sender import send_to_astutia

def do_create_deposit(data: Dict={}):
    endpoint = "deposits/create"
    resp = send_to_astutia(endpoint=endpoint, data=data, request_type=2)
    return resp

def get_all_customer_deposits(customer_id: int=0):
    endpoint = "deposits/get_by_customer/" + str(customer_id)
    resp = send_to_astutia(endpoint=endpoint)
    return resp
    
def get_single_deposit(id: int=0):
    endpoint = "deposits/single/" + str(id)
    resp = send_to_astutia(endpoint=endpoint)
    return resp
    
def do_liquidate_deposit(data: Dict={}):
    endpoint = "deposits/liquidate"
    resp = send_to_astutia(endpoint=endpoint, data=data, request_type=2)
    return resp
    
def do_calculate_rate(data: Dict={}):
    endpoint = "deposits/calculate_rate"
    resp = send_to_astutia(endpoint=endpoint, data=data, request_type=2)
    return resp