from typing import Optional

from fastapi import APIRouter, Depends, Response, status

from workshop.models.operations import Operation, OperationKind, OperationCreate, OperationUpdate
from workshop.services.operations import OperationService

router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=list[Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        operation_service: OperationService = Depends(OperationService)
):
    return operation_service.get_list(kind=kind)


@router.post('/', response_model=Operation)
def create_operation(
        operation_data: OperationCreate,
        operation_service: OperationService = Depends(OperationService)
):
    return operation_service.create(operation_data)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
        operation_id: int,
        operation_service: OperationService = Depends()
):
    return operation_service.get(operation_id)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
        operation_id: int,
        operation_data: OperationUpdate,
        operation_service: OperationService = Depends()
):
    return operation_service.update(operation_id, operation_data)


@router.delete('/{operation_id}')
def delete_operation(
        operation_id: int,
        operation_service: OperationService = Depends()
):
    operation_service.delete(operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
