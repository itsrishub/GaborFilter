import cv2

def apply_gabor_filter(image_path, kernel_size, sigma, theta, lambd, gamma, psi, output_path):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Create the Gabor kernel
    kernel = cv2.getGaborKernel((kernel_size, kernel_size), sigma, theta, lambd, gamma, psi, ktype=cv2.CV_32F)

    # Apply the Gabor filter to the image
    filtered_img = cv2.filter2D(img, cv2.CV_8UC3, kernel)

    # Save the filtered image to a file
    cv2.imwrite(output_path, filtered_img)

    print(f"Gabor filter applied to {image_path} and saved to {output_path}.")

# Example usage
apply_gabor_filter("input.jpg", kernel_size=31, sigma=5, theta=0, lambd=10, gamma=0.5, psi=0, output_path="output.jpg")