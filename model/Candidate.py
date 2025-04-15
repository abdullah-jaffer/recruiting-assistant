from pydantic import BaseModel, Field


class Candidate(BaseModel):
    name: str = Field(description="candidate name")
    email: str = Field(description="candidate name")
    phone: str = Field(description="candidate phone")
    experience: str = Field(description="candidate experience")
    years_of_experience: float = Field(description="candidates years of experience")
    education_level: str = Field(description="candidate education level")