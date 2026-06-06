from dotenv import load_dotenv
load_dotenv()

import os
import re
import replicate
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])

MODEL = "jhagruth/voo:7b9af8cabe05dae62dae776eff00f3c55c2cfca85eb10fdb5c3ca358168e80d0"

def generate_image(prompt, say, user=None):
    output = replicate.run(MODEL, input={"prompt": prompt})
    url = str(output[0].url)
    prefix = f"<@{user}> " if user else ""
    say(
        text=prefix + prompt,
        blocks=[{
            "type": "image",
            "image_url": url,
            "alt_text": prompt
        }]
    )

@app.event("app_mention")
def handle_mention(event, say):
    prompt = event["text"].split(">", 1)[-1].strip()
    prompt = re.sub(r"<@[A-Z0-9]+>", "", prompt).strip()
    if prompt:
        generate_image(prompt, say, user=event["user"])

@app.event("message")
def handle_dm(event, say):
    if event.get("channel_type") == "im" and not event.get("bot_id"):
        prompt = event["text"].strip()
        if prompt:
            generate_image(prompt, say)

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()