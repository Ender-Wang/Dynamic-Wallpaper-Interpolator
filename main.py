import cv2
import numpy as np
import argparse
import os

def interpolate_images(img_paths, num_steps_list):
    # Define the output folder
    output_folder = 'interpolated_images'
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each pair of consecutive images
    for i in range(len(img_paths) - 1):
        img1_path = img_paths[i]
        img2_path = img_paths[i + 1]
        num_steps = num_steps_list[i]
        
        img1 = cv2.imread(img1_path)
        img2 = cv2.imread(img2_path)
        
        if img1 is None:
            raise FileNotFoundError(f"{img1_path} could not be loaded. Please check the file paths.")
        if img2 is None:
            raise FileNotFoundError(f"{img2_path} could not be loaded. Please check the file paths.")

        if img1.shape != img2.shape:
            raise ValueError(f"Images {img1_path} and {img2_path} must have the same dimensions for interpolation")

        # Set file name prefix from the first image
        base_name = f'image_{i+1}'

        # Save the first image of the current pair
        first_image_path = os.path.join(output_folder, f'{base_name}_0.png')
        cv2.imwrite(first_image_path, img1)
        print(f'Saved to ./{first_image_path}')

        # Generate interpolated images
        for step in range(1, num_steps + 1):
            alpha = step / (num_steps + 1)  # Adjust alpha to produce the correct number of images
            beta = 1.0 - alpha
            interpolated_img = cv2.addWeighted(img1, beta, img2, alpha, 0.0)
            output_path = os.path.join(output_folder, f'{base_name}_{step}.png')
            cv2.imwrite(output_path, interpolated_img)
            print(f'Saved to ./{output_path}')

    # Ensure the last image in the list is saved
    last_img_path = img_paths[-1]
    last_base_name = f'image_{len(img_paths)}'
    final_image_path = os.path.join(output_folder, f'{last_base_name}_0.png')
    cv2.imwrite(final_image_path, cv2.imread(last_img_path))
    print(f'Saved to ./{final_image_path}')

def main():
    parser = argparse.ArgumentParser(description='Interpolate images between two images with customizable order and number of inter-images for each image-pairs.')
    
    parser.add_argument(
        '-img',
        '--images', 
        type=str, 
        nargs='+', 
        help='Paths of the input images, separated by spaces.'
    )
    parser.add_argument(
        '-num',
        '--num_steps', 
        type=int, 
        nargs='+', 
        help='Number of images between two images. If only one number is provided, it will be used for all image-pairs.'
    )

    args = parser.parse_args()

    # Validate the number of steps
    if len(args.images) < 2:
        parser.error("At least 2 image paths must be provided.")
    
    if len(args.num_steps) != len(args.images) - 1 and len(args.num_steps) != 1:
        parser.error(f"The number of num_steps should be {len(args.images) - 1}, but {len(args.num_steps)} were provided.")

    # Validate single vs multiple num_steps
    if len(args.num_steps) == 1:
        num_steps_list = [args.num_steps[0]] * (len(args.images) - 1)
    else:
        num_steps_list = args.num_steps

    # Run the interpolation function
    interpolate_images(args.images, num_steps_list)

if __name__ == "__main__":
    main()
