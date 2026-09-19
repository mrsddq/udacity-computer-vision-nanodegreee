# Udacity Computer Vision Nanodegree Archive

Archived coursework and project material from the Udacity Computer Vision Nanodegree.

This repository is intentionally kept as a learning record. Separate focused experiments live in repos such as `yolov8-detection`, `medical-segmentation`, `vit-robustness-xai`, `ocr-pipeline`, `clip-image-captioning`, and `pose-estimation-qa`.

### Program outline:

**This Nanodegree program is broken into three main sections:**

1- Intro to Computer Vision, which covers topics like image processing, feature extraction done manually or through training a convolutional neural network (CNN) using PyTorch.

2- Advanced Computer Vision and Deep Learning, which is all about advances in deep learning architectures like region-based CNN's, YOLO and single-shot detection algorithms, and CNN's used in combination with recurrent neural networks.

3- Object Tracking and Localization, which covers how a robot can move and sense the world around it, creating a visual representation of the world as it navigates.

 **Nanodegree Link:**
> https://www.udacity.com/course/computer-vision-nanodegree--nd891


## Completion Notes

- Key Python exercise files for facial keypoint detection and SLAM robot sensing include completed reference implementations.
- Notebooks may still contain Udacity prompt text and exercise instructions because they are preserved as course artifacts.
- This repo should remain archived and should not be presented as a production codebase.
- Use [docs/ARCHIVE_NAVIGATION.md](docs/ARCHIVE_NAVIGATION.md) to connect course topics to the focused CV repos.

## Provenance and credentials

This is Udacity coursework. Course prompts, starter code, existing project licenses, and original attribution remain with their respective authors. Individual exercise implementations do not imply authorship of the whole curriculum. The README does not use a third-party hosted certificate image as evidence of the repository owner's qualification.

## Lightweight verification

From the repository root, use an isolated Python 3.11 environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install 'nbformat>=5.10,<6'
python scripts/check_notebooks.py
```

CI checks that notebook JSON and notebook schemas are readable; it does not execute cells, train models, download datasets, or establish model accuracy. Historical checkpoint duplicates are excluded. Saved error outputs are reported rather than silently erased: some exercises intentionally demonstrate errors, and others still need repair. Existing outputs are historical, not fresh experiment results.

To run an experiment, inspect its imports, dataset paths, and course instructions first; then use a separate environment and record package versions, random seeds, train/test split, and fresh results. There is no single verified environment for every notebook in this archive.
