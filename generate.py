import anthropic
import os
from datetime import date

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "日本語で自己紹介を簡単に書いてください。また、arxiv編集ではどんなことができ層化も追加で述べてください。"}
    ]
)

text = response.content[0].text
today = date.today().strftime("%Y-%m-%d")

with open("output.md", "w", encoding="utf-8") as f:
    f.write(f"# 自己紹介 ({today})\n\n")
    f.write(text)
    f.write("\n")

print("完了しました")
print(text)
