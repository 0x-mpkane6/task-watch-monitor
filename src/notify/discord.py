import time

import requests


class DiscordNotifier:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
        self.session = requests.Session()

    def send_message(self, message: str) -> bool:
        return self._send(
            data={"content": message},
        )

    def send_image(
        self,
        image: bytes,
        message: str = "",
    ) -> bool:
        files = {
            "file": (
                "screenshot.png",
                image,
                "image/png",
            )
        }

        return self._send(
            data={"content": message},
            files=files,
        )

    def _send(
        self,
        data: dict,
        files: dict | None = None,
        max_retries: int = 3,
    ) -> bool:

        for attempt in range(1, max_retries + 1):
            try:
                response = self.session.post(
                    self.webhook_url,
                    data=data,
                    files=files,
                    timeout=30,
                )

                if response.status_code == 429:
                    retry_after = response.json().get(
                        "retry_after",
                        1,
                    )

                    print(
                        f"[!] Discord rate limited. "
                        f"Retrying after {retry_after}s..."
                    )

                    time.sleep(retry_after)
                    continue

                response.raise_for_status()

                return True

            except requests.RequestException as error:
                print(
                    f"[!] Discord request failed "
                    f"({attempt}/{max_retries}): {error}"
                )

                if attempt < max_retries:
                    time.sleep(2)

        return False