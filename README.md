# Artistic Turbulence Analysis

## Project Overview
This project aims to analyze the turbulence-like characteristics in paintings, specifically focusing on luminance variations within artworks. Inspired by the research that applied Kolmogorov's turbulence theories to Van Gogh's paintings, this script provides tools to examine how the distribution of luminance can reflect turbulent patterns similar to those observed in fluid dynamics.

## Motivation
The project is based on the insights provided by the paper "Turbulent luminance in impassioned van Gogh paintings," which explores the analogy between the chaotic patterns in Van Gogh’s artworks and the statistical models of turbulence in fluid dynamics.  This project references the paper "Turbulent luminance in impassioned van Gogh paintings" located here: https://www.arxiv.org/abs/physics/0606246

## Features
- **Luminance Conversion**: Converts digital images of paintings into luminance data.
- **Luminance Difference Calculation**: Computes the differences in luminance at multiple scales to capture local variations.
- **Log-Normal Fitting**: Fits the distribution of luminance differences to log-normal distributions, allowing for the analysis of scaling behaviors.
- **Kolmogorov’s Scaling Laws**: Applies Kolmogorov's scaling laws to the luminance data to simulate turbulence modeling.
- **Statistical Comparison**: Compares the turbulence characteristics between different paintings using statistical tests.

## Installation
Clone this repository to your local machine

## Requirements
This script requires Python 3.x along with the following libraries:

- NumPy
- PIL (Pillow)
- Matplotlib
- SciPy

You can install all required libraries using:
```bash
pip install numpy pillow matplotlib scipy
```

## Usage
To run the script, navigate to the cloned directory and execute:
```bash
Turbulent_Luminance_Analysis.py
```

## Example
Below is an example of how to use the script to analyze two different images:

- Load the images.
- Convert the images to luminance.
- Calculate luminance differences.
- Apply statistical analysis.
- Plot the results.

Detailed documentation and function descriptions are available within the script.

## Acknowledgments
- This project was inspired by the research published in [arXiv/0606246v2](https://www.arxiv.org/abs/physics/0606246).

