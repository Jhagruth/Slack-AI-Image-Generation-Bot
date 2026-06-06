# Slack-AI-Image-Generation-Bot

A Slack bot that generates images using a custom Replicate model when mentioned in a channel or messaged directly.

## Features

- Mention the bot in any channel to generate an image
- DM the bot directly with a prompt
- Images rendered inline in Slack

## Setup

### 1. Install dependencies
pip install slack-bolt replicate python-dotenv

### 2. Create a `.env` file
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...
REPLICATE_API_TOKEN=r8_...

### 3. Run
python app.py

## Usage

**In a channel:**
@Voo a dog surfing on a wave

**In a DM:**
a futuristic city at sunset

## Tech Stack

- [Slack Bolt for Python](https://slack.dev/bolt-python/)
- [Replicate](https://replicate.com)
- Custom fine-tuned image generation model (`jhagruth/voo`)
