# Dynamic Wallpaper Interpolator

Dynamic Wallpaper Interpolator(DWI) interpolates images between two existing images to create a smoother dynamic wallpaper experience. At least two images with the same dimension are required for inputs, you can define the number of interpolations between each image pair. DWI can be used to enhance dynamic wallpaper files (HEIC) on macOS with smoother transitions. This project uses Computer Vision (`cv2`) in `opencv-python` library and `numpy` to generate interpolated images.

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

For more details on the arguments:

```
python main.py -h
```

Help message:

```
usage: main.py [-h] [-img IMAGES [IMAGES ...]] [-num NUM_STEPS [NUM_STEPS ...]]

Interpolate images between two images with customizable order and number of inter-images for each image-pairs.

options:
-h, --help            show this help message and exit
-img IMAGES [IMAGES ...], --images IMAGES [IMAGES ...]
                        Paths of the input images, separated by spaces.
-num NUM_STEPS [NUM_STEPS ...], --num_steps NUM_STEPS [NUM_STEPS ...]
                        Number of images between two images. If only one number is provided, it will be used for all image-pairs.
```

## Examples

1. Generate `2` images between all pairs of images (the file name ending with "\_0" is the original image):
   ```
   python main.py -img desert_sands_1.png desert_sands_2.png desert_sands_3.png -num 2
   ```
   Interpolated images in `./interpolated_images`:
   ```
    image_1_0.png
    image_1_1.png
    image_1_2.png
    image_2_0.png
    image_2_1.png
    image_2_2.png
    image_3_0.png
   ```
2. Generate `2` images between the first pair and `3` between the second pairs of images:
   ```
   python main.py -img desert_sands_1.png desert_sands_2.png desert_sands_3.png -num 2 3
   ```
   Interpolated images in `./interpolated_images`:
   ```
    image_1_0.png
    image_1_1.png
    image_1_2.png
    image_2_0.png
    image_2_1.png
    image_2_2.png
    image_2_3.png
    image_3_0.png
   ```

## Create Dynamic Wallpaper

Use [Equinox](https://github.com/rlxone/Equinox) created by [rlxone](https://github.com/rlxone) to create dynamic wallpapers from the interpolated images.

## Contributing

Feel free to fork the repository and make a pull request if you have improvements or fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://raw.githubusercontent.com/Ender-Wang/Dynamic-Wallpaper-Interpolator/master/LICENSE) file for details.
