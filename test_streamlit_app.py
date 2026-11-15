import unittest
from io import BytesIO
from unittest.mock import patch

from PIL import Image

from streamlit_app import decode_image


class DecodeImageTests(unittest.TestCase):
    def create_png(self, size=(12, 8), image_mode="RGBA"):
        image = Image.new(image_mode, size, color=(30, 120, 45, 255))
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        return buffer.getvalue()

    def test_decodes_image_as_rgb(self):
        decoded = decode_image(self.create_png())

        self.assertEqual(decoded.mode, "RGB")
        self.assertEqual(decoded.size, (12, 8))

    def test_rejects_non_image_data(self):
        with self.assertRaisesRegex(ValueError, "valid, readable image"):
            decode_image(b"not an image")

    def test_rejects_images_above_pixel_limit(self):
        with patch("streamlit_app.MAX_IMAGE_PIXELS", 10):
            with self.assertRaisesRegex(ValueError, "dimensions are too large"):
                decode_image(self.create_png())

    def test_rejects_images_above_byte_limit(self):
        with patch("streamlit_app.MAX_IMAGE_BYTES", 4):
            with self.assertRaisesRegex(ValueError, "Image is too large"):
                decode_image(self.create_png())


if __name__ == "__main__":
    unittest.main()
