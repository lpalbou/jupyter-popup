# jupyter-popup

A simple and reliable popup/modal solution for Jupyter notebooks that works in remote environments.

## Installation

```bash
pip install jupyter-popup
```

## Usage

```python
from jupyter_popup import create_popup

# Simple usage
create_popup("This is a test message", "Title")

# With HTML content
html_content = """
<div style='line-height: 1.6'>
    <h3>Important Information</h3>
    <p>This is formatted content.</p>
</div>
"""
create_popup(html_content, "HTML Content")
```

## Features

- True fixed positioning that works in remote Jupyter environments
- Proper handling of long content with scrolling
- Works with HTML content
- Doesn't interfere with notebook layout
- Proper contrast and visibility in both light and dark themes

## Requirements

- Python ≥ 3.6
- IPython ≥ 7.0.0

## License

MIT