# Text Steganography in Image (Python)

This project demonstrates a simple steganography technique that hides a text message inside an RGB image using the Least Significant Bit (LSB) method. 
The message is converted to binary and embedded into the pixel data of the image. The script also allows retrieving the hidden message.

## File

- `putTextInImage/code.py` — Python script that includes both encoding and decoding functionalities.

## Features

- Converts text to binary using ASCII encoding.
- Embeds the binary message in the image by modifying RGB pixel values (odd if bit = 1, even if bit = 0).
- Adds a 16-bit delimiter (`1111111111111110`) at the end of the message to mark its boundary.
- Extracts and reconstructs the original message from the image.

## Requirements

Install dependencies with:

```bash
pip install pillow numpy
```

# How to use it
## Encode text in image
```bash
cacher_texte_dans_image('name_image_in.png', 'message', 'name_image_out.png')
```
The function takes three inputs: the name of the image in which the text will be encoded ('name_image_in.png'), the message to encode ('message'), and the name of the output image that will result from the function ('name_image_out.png').
put in this function the name of the image
## Decode text in image
```bash
decoder_texte_dans_image('name_image_out.png')
```
With this function, you can pass the previously encoded image to retrieve the hidden message by simply providing the name of the image ('name_image_out.png').

