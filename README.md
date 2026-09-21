# task-watch-monitor

A lightweight Python tool that periodically captures screenshots of your computer and sends them to a Discord channel through a webhook, allowing you to remotely monitor long-running tasks.

## Setup

Create a virtual environment:

```bash
python -m venv .venv
````

Activate the virtual environment.

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file based on `.env.example` and configure your Discord webhook:

```env
DISCORD_WEBHOOK_URL=YOUR_DISCORD_WEBHOOK_URL
SCREENSHOT_INTERVAL_MINUTES=10
```

## Run

Start the monitor with:

```bash
python main.py
```

Press `Ctrl+C` to stop the monitor.
