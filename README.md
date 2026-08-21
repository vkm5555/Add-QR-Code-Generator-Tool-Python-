# QR Code Generator

A simple Python tool for generating QR codes from text or URLs.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from tool import generate_qr

result = generate_qr("https://example.com")
print(result)
```

## Output

The tool returns the generated PNG image as Base64.

```json
{
  "success": true,
  "data": "https://example.com",
  "format": "png",
  "image": "iVBORw0KGgo..."
}
```

## Test

```bash
python tool.py
```
