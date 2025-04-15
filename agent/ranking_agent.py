from model.Rank import Rank

def rank_resumes_by_requirements(llm, requirements: str, resumes, top_n: int = 4):
    structured_llm = llm.bind_tools([Rank])

    scored_resumes = []
    for resume in resumes:
        try:
            resume_summary = f"""
Name: {resume['name']}
Email: {resume['email']}
Phone: {resume['phone']}
Years of Experience: {resume['years_of_experience']}
Education: {resume['education_level']}
Experience:
{resume['experience']}
"""

            prompt = f"""
You are a technical recruiter.

Given the job requirements below, score the candidate resume on a scale from 1 to 10
(10 being a perfect match) based on relevance, experience, and skill alignment.

Job Requirements:
{requirements}

Candidate Resume:
{resume_summary}

Respond with email, name, experience and rank.
"""

            response = structured_llm.invoke(prompt)
            rank = response.tool_calls[0]['args']
            scored_resumes.append(rank)

        except Exception as e:
            print(f"Error scoring resume")

    scored_resumes.sort(key=lambda x: x['rank'], reverse=True)
    return scored_resumes[:top_n]
