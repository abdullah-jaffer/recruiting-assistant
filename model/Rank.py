from pydantic import BaseModel, Field


class Rank(BaseModel):
    email: str = Field(description="candidate email")
    name: str = Field(description="candidate name")
    rank: int = Field(description="resume rank")
    experience: str = Field(description="experience")