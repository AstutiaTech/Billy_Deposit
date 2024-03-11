from fastapi import APIRouter
from modules.utils.req import do_create_deposit, get_all_customer_deposits, get_single_deposit, do_liquidate_deposit, do_calculate_rate
from schemas import CreateDeposit, LiquidateDeposit, RateModel

router = APIRouter()

@router.post("/create")
async def create_new_deposit(depo: CreateDeposit):
    return do_create_deposit(data=depo.dict())

@router.get("/get_customer/{customer_id}")
async def customer_deposit(customer_id: int=0):
    return get_all_customer_deposits(customer_id=customer_id)

@router.get("/get_single/{id}")
async def single_deposit(id: int=0):
    return get_single_deposit(id=id)

@router.post("/liquidate")
async def liquidate(depo: LiquidateDeposit):
    return do_liquidate_deposit(data=depo.dict())
    
@router.post("/calculate_rate")
async def calculate_rate(depo: RateModel):
    return do_calculate_rate(data=depo.dict())