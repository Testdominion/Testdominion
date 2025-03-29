from stegano import lsb

# Input image (make sure this file exists in your working directory)
input_image = "doms.png"
output_image = "uju.png"

# Secret message to hide
secret_message = "dominion loves uju!"

# Hide message inside the image
hidden_image = lsb.hide(input_image, secret_message)
hidden_image.save(output_image)

print(f"Message hidden in {output_image}")
