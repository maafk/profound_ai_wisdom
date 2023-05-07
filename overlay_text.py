from PIL import Image, ImageDraw, ImageFont
import textwrap
import json
import random
import os

def wrap_text(draw, text, font, max_width):
    lines = textwrap.wrap(text, width=1)
    line_width = 0
    while line_width <= max_width:
        bbox = draw.textbbox((0, 0), lines[0], font)
        line_width = bbox[2] - bbox[0]
        wrap_width = max_width // (line_width // len(lines[0]) + 1)
        new_lines = textwrap.wrap(text, width=wrap_width)
        if len(new_lines) == len(lines):
            break
        lines = new_lines
    return lines

def add_text_to_image(image, text, font_path, font_size):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    img_width, img_height = image.size
    wrapped_text = wrap_text(draw, text, font, img_width)
    text_height = len(wrapped_text) * font_size

    position_y = (img_height - text_height) // 2
    color = (255, 255, 255)  # White
    border_color = (0, 0, 0)  # Black
    border_width = 2  # Border width in pixels

    for line in wrapped_text:
        bbox = draw.textbbox((0, 0), line, font)
        text_width = bbox[2] - bbox[0]
        position_x = (img_width - text_width) // 2

        # Draw the black border
        for x_offset in range(-border_width, border_width + 1):
            for y_offset in range(-border_width, border_width + 1):
                draw.text((position_x + x_offset, position_y + y_offset), line, border_color, font=font)

        # Draw the white text
        draw.text((position_x, position_y), line, color, font=font)
        position_y += font_size

    return image

width = 1080 # Ideal width for Instagram Portrait
height = 1350 # Ideal height for Instagram Portrait
# Location of Arial Unicode font on a macbook
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_size = 70  # Big enough, but not too big

with open('quotes.json', 'r') as f:
    quotes = json.load(f)

backgrounds = [
    "background_beach",
    "background_valley",
    "background_woods",
]

for i, quote in enumerate(quotes["quotes"]):
    bkg = random.choice(backgrounds)
    image = Image.open(f'{bkg}.png')
    attr_quote = f"{quote} - Profound AI Wisdom"
    output_image = add_text_to_image(image, attr_quote, font_path, font_size)
    output_dir = f"posts/{bkg}"
    os.makedirs(output_dir, exist_ok=True)
    output_image.save(f'{output_dir}/quote_{i:0{3}d}.png')