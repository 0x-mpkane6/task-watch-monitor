import mss
import mss.tools


def capture_screen() -> bytes:
    """
    Capture the entire desktop and return the screenshot
    as PNG bytes.
    """
    with mss.mss() as sct:
        # monitors[0] = toàn bộ desktop
        # Nếu chỉ có một màn hình thì vẫn dùng được bình thường.
        monitor = sct.monitors[0]

        screenshot = sct.grab(monitor)

        image_bytes = mss.tools.to_png(
            screenshot.rgb,
            screenshot.size,
        )

    return image_bytes