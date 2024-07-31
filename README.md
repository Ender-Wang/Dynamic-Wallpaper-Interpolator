# Dynamic Wallpaper Interpolator

This project generates interpolated images between two existing images to create a smoother dynamic wallpaper experience. The script reads at least two images with the same dimension, interpolates new images between them. This can be used to enhance dynamic wallpaper files (HEIC) on macOS with smoother transitions. This project makes use of `cv2` in `opencv-python` and `numpy` to generate interpolated images.

## Requirements

- `python` 3.12 or later
- `pipenv` to create python virtual env for managing dependencies

## Setup

- Install `python` and `pipenv` via `brew`:

  ```zsh
  brew install python@3.12 && brew install pipenv
  ```

- Install dependencies and activate `pipenv` virtual environment

  ```zsh
  pipenv install && pipenv shell
  ```

## Usage

1. Generate 2 images between all pairs of images (the file name ending with "\_0" is the original image):
   ```
   python main.py -img desert_sands_1.png desert_sands_2.png desert_sands_3.png -num 2
   ```
   Interpolated images in `./interpolated_images`:
   ```
    desert_sands_1_0.png
    desert_sands_1_1.png
    desert_sands_1_2.png
    desert_sands_2_0.png
    desert_sands_2_1.png
    desert_sands_2_2.png
    desert_sands_3_0.png
   ```
2. Generate 2 images between the first pair and 3 between the second pairs of images:
   ```
   python main.py -img desert_sands_1.png desert_sands_2.png desert_sands_3.png -num 2 3
   ```
   Interpolated images in `./interpolated_images`:
   ```
    desert_sands_1_0.png
    desert_sands_1_1.png
    desert_sands_1_2.png
    desert_sands_2_0.png
    desert_sands_2_1.png
    desert_sands_2_2.png
    desert_sands_2_3.png
    desert_sands_3_0.png
   ```
3. For more details on the arguments:
   ```
   python main.py -h
   ```

## Contributing

Feel free to fork the repository and make a pull request if you have improvements or fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
