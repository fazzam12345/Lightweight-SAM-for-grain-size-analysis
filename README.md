# Lightweight-SAM-for-grain-size-analysis

This repository contains code for applying and evaluating **lightweight variants of the Segment Anything Model (SAM)** for **grain size analysis** in petrographic images.

It provides a framework to perform automatic mask generation, extract quantitative grain properties, and evaluate performance against ground truth data, including segmentation accuracy and grain size distribution similarity.

## Key Features

*   Implementation examples for various lightweight SAM variants (MobileSAM demonstrated by default).
*   Automated segmentation of grains in images.
*   Extraction of quantitative grain properties (area, length, width, perimeter).
*   Matching of predicted grains to ground truth annotations using centroid proximity and IoU.
*   Evaluation of segmentation performance (Precision, Recall, F1).
*   Analysis and comparison of grain size distributions (Area and Length) using histograms, CDFs, KS test, and NRMSE.
*   Saving of results (metrics and distribution data) to CSV/Excel.

## Prerequisites

*   Python 3.12
*   Install core libraries:
    ```bash
    pip install torch torchvision numpy matplotlib opencv-python pandas scipy scikit-learn openpyxl
    ```
*   Install necessary SAM libraries. For MobileSAM (used in default config):
    ```bash
    pip install git+https://github.com/ChaoningZhang/MobileSAM.git
    ```
    (Adjust or add installations based on which specific SAM variants you intend to run, e.g., `pip install segment_anything` for original SAM).
*   Download pre-trained model checkpoints for the SAM variants you will use (e.g., `mobile_sam.pt`). Place them in a `weights` directory or update the `CHECKPOINT_PATH` in the notebook.
*   Prepare input image(s) and corresponding ground truth annotations (expected in a JSON format compatible with the provided loading function). Place them in `images` and `annotations` directories or update paths in the notebook.

## Repository Structure

*   `./`: Root directory.
*   `Evaluation_pipeline.ipynb`: The main analysis notebook containing the workflow.
*   `weights/`: Directory to store downloaded model checkpoints.
*   `images/`: Directory for input petrographic images.
*   `annotations/`: Directory for ground truth JSON annotation files.
*   `results/`: Output directory for metrics and distribution data (created automatically).

## How to Run

1.  Clone this repository.
2.  Ensure all [Prerequisites](#prerequisites) are met (Python environment, libraries, data, checkpoints).
3.  Open the notebook file (`Evaluation_pipeline.ipynb`) in a Jupyter environment (Jupyter Lab, VS Code with Python extension, etc.).
4.  Review and update the **Configuration and Setup** section at the beginning of the notebook:
    *   Select the `MODEL_VARIANT`.
    *   Specify `CHECKPOINT_PATH`, `EXAMPLE_IMAGE_PATH`, `GROUND_TRUTH_ANNOTATION_PATH`, and `OUTPUT_RESULTS_DIR`.
    *   Adjust `SCALE_FACTOR` for your image resolution.
    *   Tune `AMBG_PARAMS` and evaluation thresholds (`IOU_THRESHOLD`, `CENTROID_MATCH_DISTANCE`) as needed for your data and chosen model.
5.  Run the notebook cells sequentially.

The notebook will guide you through the process, visualize intermediate and final results, and save quantitative metrics and distribution data to the specified output directory.
