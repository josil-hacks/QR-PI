import io

import qrcode
import qrcode.image.svg


def generate_qr_svg(value: str) -> bytes:
    """Generate an SVG QR code for the supplied value."""
    buffer = io.BytesIO()

    image = qrcode.make(
        value,
        image_factory=qrcode.image.svg.SvgPathImage,
    )
    image.save(buffer)

    return buffer.getvalue()