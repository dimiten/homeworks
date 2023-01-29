from fastapi import HTTPException, APIRouter

from device_models.controllers.device_model_controller import DeviceModelsController
from device_models.models.schemas import DeviceModelSchema, DeviceModelSchemaIn, DeviceModelSchemaUpdate, \
    DeviceModelProducesBeverageSchema, DeviceModelSchemaWithBeverages
from http import HTTPStatus

device_model_router = APIRouter(tags=["Device Models"], prefix="/api/device-models")


@device_model_router.get("", response_model=list[DeviceModelSchema])
def get_all_device_models():
    return DeviceModelsController.get_all_device_models()


@device_model_router.get("/{device_model_id}", response_model=DeviceModelSchema)
def get_device_model_by_id(device_model_id: int):
    return DeviceModelsController.get_device_model_by_id(device_model_id)


@device_model_router.post("", response_model=DeviceModelSchema)
def create_device_model(device_model: DeviceModelSchemaIn):
    response = DeviceModelsController.create_device_model(**device_model.__dict__)
    return response


@device_model_router.put("/{id}", response_model=DeviceModelSchema)
def update_device_model(beverage_id: int, update_data: DeviceModelSchemaUpdate):
    return DeviceModelsController.update_device_model(update_data.__dict__, beverage_id)


@device_model_router.delete("/{device_model_is}")
def delete_device_model(device_model_id: int):
    try:
        DeviceModelsController.delete_device_model(device_model_id)
        return {"message": "Device model successfully deleted."}
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@device_model_router.post("/add-beverage-to-device-model", status_code=201,
                          response_model=DeviceModelSchemaWithBeverages)
def add_new_beverage_to_device_model(device_model_produces_beverage_schema: DeviceModelProducesBeverageSchema):
    try:
        DeviceModelsController.add_new_beverage_to_device_model(device_model_produces_beverage_schema.device_model_id,
                                                                device_model_produces_beverage_schema.beverage_id)

        return DeviceModelsController.device_model_with_list_of_beverages(
            device_model_produces_beverage_schema.device_model_id)
    except HTTPException as e:
        raise e


@device_model_router.get("/get-device-models-with-beverages/{device_model_id}",
                         response_model=DeviceModelSchemaWithBeverages)
def get_device_model_with_list_of_beverages(device_model_id: int):
    return DeviceModelsController.device_model_with_list_of_beverages(device_model_id=device_model_id)


@device_model_router.delete("/delete-beverage-from-device-model/{device_model_id, beverage_id}")
def delete_beverage_from_device_model(device_model_id: int, beverage_id: int):
    try:
        DeviceModelsController.delete_beverage_from_device_model(device_model_id, beverage_id)
        return {"message": "Beverage successfully deleted from device model."}
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@device_model_router.get("/get-all-device-models-with-all-beverages/{device_models}", response_model=list[DeviceModelSchemaWithBeverages])
def get_all_device_models_with_all_beverages():
    device_models = DeviceModelsController.get_all_device_models()
    device_models_with_beverages = []
    for device_model in device_models:
        device_models_with_beverages.append(DeviceModelsController.device_model_with_list_of_beverages(device_model_id=device_model.device_model_id))
    return device_models_with_beverages

