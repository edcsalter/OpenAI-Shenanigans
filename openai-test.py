from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a prolific dungeon master named Tim. You are known for creating interesting and unique nonplayer characters."},
    {"role": "user", "content": "Generate a goblin NPC for my next session. Provide a backstory if possible. Print the NPC's character sheet.."},
  ]
)

print(completion.choices[0].message)