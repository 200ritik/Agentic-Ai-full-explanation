from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Virat", age="36")

print(user.age)
print(type(user.age))

# and many more optional vs required

from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    name: str
    age: int
    disease: Optional[str] = None
    
    
# email and url validation
from pydantic import BaseModel, EmailStr, AnyUrl

class User(BaseModel):
    email: EmailStr
    website: AnyUrl
    
    
# expert data validation
from pydantic import BaseModel, Field

class Patient(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=0, le=120)
    
# meat data and annoted
    
from typing import Annotated
from pydantic import Field

temperature: Annotated[
    float,
    Field(description="Patient's body temperature in Celsius")
]


# field validator
from pydantic import BaseModel, field_validator

class Patient(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def check_name(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value
    
# model validator

from pydantic import BaseModel, model_validator

class Patient(BaseModel):
    age: int
    guardian: str | None = None

    @model_validator(mode="after")
    def check_guardian(self):
        if self.age < 18 and self.guardian is None:
            raise ValueError("A minor must have a guardian")
        return self
    
    
# nested model

class Address(BaseModel):
    city: str
    country: str

class Patient(BaseModel):
    name: str
    address: Address
    
    patient = Patient(
    name="John",
    address={
        "city": "Delhi",
        "country": "India"
    }
)