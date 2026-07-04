from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from pydantic import BaseModel
from dotenv import load_dotenv
import json

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-7B-Instruct"
)

model = ChatHuggingFace(llm=llm)


class Review(BaseModel):
    summary:str
    sentiment:str

prompt = """
You are a JSON generator.

Return ONLY a valid JSON object.

Do not explain anything.
Do not use markdown.
Do not write ```json.
Do not write any text before or after the JSON.

The JSON must follow this schema:

{
    "summary": "A short summary in one sentence",
    "sentiment": "positive | negative | neutral"
}
Review:
I recently purchased the AeroFit Smart Fitness Watch, and overall I am very happy with it. The watch arrived two days earlier than expected, and the packaging was excellent. The display is bright and easy to read even in direct sunlight. It accurately tracks my daily steps, heart rate, sleep, and workouts. The battery lasts for about 9 days on a single charge, which is much better than I expected.
However, the companion mobile app can be a bit slow at times, especially when syncing workout data. I also noticed that the GPS takes a little longer than expected to connect when I start an outdoor run. Despite these minor issues, the watch is lightweight, comfortable to wear all day, and offers great value for the price.
Overall, I am satisfied with my purchase and would definitely recommend the AeroFit Smart Fitness Watch to anyone looking for an affordable fitness tracker with premium features. I would rate it 4.5 out of 5 stars.
"""


response = model.invoke(prompt)


data = json.loads(response.content)


review = Review(**data)

print(review)

print(review.summary)
print(review.sentiment)
