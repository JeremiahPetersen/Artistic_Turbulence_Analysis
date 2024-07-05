# Artistic Turbulence Analysis

## Project Overview
This project aims to analyze the turbulence-like characteristics in paintings, specifically focusing on luminance variations within artworks. Inspired by the research that applied Kolmogorov's turbulence theories to Van Gogh's paintings, this script provides tools to examine how the distribution of luminance can reflect turbulent patterns similar to those observed in fluid dynamics.

## Motivation
The project is based on the insights provided by the paper "Turbulent luminance in impassioned van Gogh paintings," which explores the analogy between the chaotic patterns in Van Gogh’s artworks and the statistical models of turbulence in fluid dynamics.

## Features
- **Luminance Conversion**: Converts digital images of paintings into luminance data.
- **Luminance Difference Calculation**: Computes the differences in luminance at multiple scales to capture local variations.
- **Log-Normal Fitting**: Fits the distribution of luminance differences to log-normal distributions, allowing for the analysis of scaling behaviors.
- **Kolmogorov’s Scaling Laws**: Applies Kolmogorov's scaling laws to the luminance data to simulate turbulence modeling.
- **Statistical Comparison**: Compares the turbulence characteristics between different paintings using statistical tests.

## Installation
Clone this repository to your local machine using:
```bash
git clone https://github.com/yourusername/artistic-turbulence-analysis.git
