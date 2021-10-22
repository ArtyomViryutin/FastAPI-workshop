from enum import Enum

from pydantic import BaseModel
from datetime import date


class OperationKind(Enum):
    income = "income"
    outcome = "outcome"


class Operation(BaseModel):
    id: int
    date: date
    kind: OperationKind
    amount: int
    description: str | None
