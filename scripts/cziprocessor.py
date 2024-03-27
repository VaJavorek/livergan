import numpy as np
from pathlib import Path
# import scaffan
import os
import cv2
from wsitools.tile_image import ImageSplitterMerger
import matplotlib.pyplot as plt
import torch
import torchvision.transforms as transforms
from models.networks import define_G
from collections import OrderedDict

def process_tileA(tile: np.array) -> np.array:
    if tile.shape[2] != 3:
        raise ValueError("Image ndarray must have 3 channels for RGB.")

    # Create a copy of the image to avoid modifying the original array
    result_tile = np.copy(tile)
    
    isBorder = False
    if np.mean(tile) >= 157: # Tresholding - checking if the tile is at the border of the sample
        isBorder = True

    with torch.no_grad():
            generator_model.eval()
            
            to_tensor = transforms.ToTensor()
            result_tile = to_tensor(result_tile)
            result_tile = generator_model(result_tile)
    
    result_tile = result_tile.cpu().permute(1, 2, 0).numpy()
    result_tile = (result_tile - result_tile.min()) / (result_tile.max() - result_tile.min()) # normalize

    # Postprocessing
    if isBorder:
        gray_tile = cv2.cvtColor(np.copy(tile), cv2.COLOR_BGR2GRAY)
        mask = gray_tile >= np.percentile(gray_tile, 90)
        result_tile[mask] = tile[mask] # painting the background with the original colors

    # Draw the red square
    # red_color = [255, 0, 0]
    # result_tile[5:5 + 50, 5:5 + 50, :] = red_color

    result_tile = np.clip(result_tile, 0, 1)
    return result_tile

def process_tileB(tile: np.array) -> np.array:
    if tile.shape[2] != 3:
        raise ValueError("Image ndarray must have 3 channels for RGB.")

    # Create a copy of the image to avoid modifying the original array
    result_tile = np.copy(tile)

    with torch.no_grad():
            generator_model.eval()
            
            to_tensor = transforms.ToTensor()
            result_tile = to_tensor(result_tile)
            result_tile = generator_model(result_tile)

    result_tile = result_tile.cpu().permute(1, 2, 0).numpy()
    result_tile = (result_tile - result_tile.min()) / (result_tile.max() - result_tile.min()) # normalize

    # Postprocessing
    gray_tile = cv2.cvtColor(result_tile, cv2.COLOR_BGR2GRAY)
    mask = gray_tile >= np.percentile(gray_tile, 10)
    target_brightness = 0.82
    current_brightness = np.mean(result_tile[mask])
    adjustment_ratio = target_brightness / current_brightness

    result_tile[mask] = result_tile[mask] * adjustment_ratio # adjust the result's background to the targeted brightness

    # Draw the red square
    # red_color = [255, 0, 0]
    # result_tile[5:5 + 50, 5:5 + 50, :] = red_color

    result_tile = np.clip(result_tile, 0, 1)
    return result_tile