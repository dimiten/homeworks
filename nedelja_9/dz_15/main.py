from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from device_model import DeviceModel
from typing import Optional

app = FastAPI()


class DeviceModelSchema(BaseModel):
    device_model_id: int
    model_name: str
    model_number: str
    water_capacity_liters: float
    coffee_capacity_kgs: float
    milk_capacity_kgs: float
    sugar_capacity_kgs: float
    sweetener_capacity_count: int
    cups_capacity_count: int

    class Config:
        orm_mode = True


class DeviceModelSchemaIn(BaseModel):
    model_name: str
    model_number: str
    water_capacity_liters: float
    coffee_capacity_kgs: float
    milk_capacity_kgs: float
    sugar_capacity_kgs: float
    sweetener_capacity_count: int
    cups_capacity_count: int

    class Config:
        orm_mode = True


class DeviceModelSchemaUpdate(BaseModel):
    model_name: Optional[str]
    model_number: Optional[str]
    water_capacity_liters: Optional[float]
    coffee_capacity_kgs: Optional[float]
    milk_capacity_kgs: Optional[float]
    sugar_capacity_kgs: Optional[float]
    sweetener_capacity_count: Optional[int]
    cups_capacity_count: Optional[int]

    class Config:
        orm_mode = True


@app.get("/api/device_models/{device_model_id}", response_model=DeviceModelSchema)
def get_device_model_by_id(device_model_id: int):
    """Returns device model by id from database"""
    try:
        return DeviceModel.get_device_model_by_id(device_model_id=device_model_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Device model with provided ID not found")


@app.post("/api/device_models", response_model=DeviceModelSchema)
def create_device_model(device_model: DeviceModelSchemaIn):
    return DeviceModel.create_new_device_model(model_name=device_model.model_name,
                                               model_number=device_model.model_number,
                                               water_capacity_liters=device_model.water_capacity_liters,
                                               coffee_capacity_kgs=device_model.coffee_capacity_kgs,
                                               milk_capacity_kgs=device_model.milk_capacity_kgs,
                                               sugar_capacity_kgs=device_model.sugar_capacity_kgs,
                                               sweetener_capacity_count=device_model.sweetener_capacity_count,
                                               cups_capacity_count=device_model.cups_capacity_count)


@app.put("/api/device_models/{device_model_id}", response_model=DeviceModelSchema)
def update_device_model(device_model_id: int, update_device_model_d: DeviceModelSchemaUpdate):
    device_model = DeviceModel.get_device_model_by_id(device_model_id=device_model_id)
    update_device_model_dict = update_device_model_d.__dict__
    for key in update_device_model_dict.copy():
        if update_device_model_dict[key] is None:
            del update_device_model_dict[key]
    return device_model.update_device_model(attributes_dict=update_device_model_dict)


@app.delete("/api/device_models/{device_model_id}")
def delete_device_model(device_model_id: int):
    try:
        DeviceModel.delete_device_model_by_id(device_model_id=device_model_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.__str__())
