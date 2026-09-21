import os
import time
from datetime import datetime

from dotenv import load_dotenv

from src.capture.screenshot import capture_screen
from src.notify.discord import DiscordNotifier


def load_config():
    load_dotenv()

    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    interval_minutes = float(
        os.getenv(
            "SCREENSHOT_INTERVAL_MINUTES",
            "1",
        )
    )

    if not webhook_url:
        raise RuntimeError(
            "DISCORD_WEBHOOK_URL is missing in .env"
        )

    if interval_minutes <= 0:
        raise ValueError(
            "SCREENSHOT_INTERVAL_MINUTES must be greater than 0"
        )

    return webhook_url, interval_minutes


def main():
    webhook_url, interval_minutes = load_config()

    interval_seconds = interval_minutes * 60

    notifier = DiscordNotifier(webhook_url)

    print("[+] Task Watch Monitor")
    print(
        f"[+] Screenshot interval: "
        f"{interval_minutes} minute(s)"
    )
    print("[+] Press Ctrl+C to stop")

    notifier.send_message(
        "🟢 **Task Watch Monitor started**"
    )

    try:
        while True:
            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            try:
                image = capture_screen()

                success = notifier.send_image(
                    image,
                    f"🖥️ Screenshot — `{timestamp}`",
                )

                if success:
                    print(
                        f"[{timestamp}] Screenshot sent"
                    )
                else:
                    print(
                        f"[{timestamp}] Failed to send screenshot"
                    )

            except Exception as error:
                print(
                    f"[{timestamp}] Capture error: {error}"
                )

            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\n[-] Monitor stopped")

        notifier.send_message(
            "🔴 **Task Watch Monitor stopped**"
        )


if __name__ == "__main__":
    main()