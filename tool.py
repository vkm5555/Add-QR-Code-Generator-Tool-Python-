import base64
import io

import qrcode


def generate_qr(data: str):
    if not data:
        return {
            "success": False,
            "error": "Data is required"
        }   

    try:
        qr = qrcode.make(data)

        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")

        image = base64.b64encode(
            buffer.getvalue() 
        ).decode("utf-8")

        return {
            "success": True,
            "data": data,
            "format": "png",
            "image": image
        }

    except Exception as exc:
        return {
            "success": False,
            "error": str(exc)
        }


if __name__ == "__main__":
    result = generate_qr("https://example.com")
    print(result)
