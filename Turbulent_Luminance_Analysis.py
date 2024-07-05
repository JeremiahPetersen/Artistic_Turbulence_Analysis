import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.stats import lognorm, ttest_ind
import random

def load_and_convert_to_luminance(image_path):
    img = Image.open(image_path)
    print(f"Loaded image size: {img.size}")  # OUTPUT IMAGE SIZE FOR DEBUGGING
    rgb_img = img.convert('RGB')
    pixels = np.array(rgb_img)
    luminance = 0.299 * pixels[:, :, 0] + 0.587 * pixels[:, :, 1] + 0.114 * pixels[:, :, 2]
    return luminance

def calculate_luminance_differences(luminance_matrix, scales):
    height, width = luminance_matrix.shape
    differences_dict = {}
    for scale in scales:
        differences = []
        for i in range(height):
            for j in range(width):
                if j + scale < width:
                    differences.append(abs(luminance_matrix[i, j] - luminance_matrix[i, j + scale]))
                if i + scale < height:
                    differences.append(abs(luminance_matrix[i, j] - luminance_matrix[i + scale, j]))
        differences_dict[scale] = np.array(differences)
    return differences_dict

def fit_log_normal_with_lambda(differences, lambda_value=0.1):
    sigma = np.std(differences)
    mu = np.mean(np.log(differences[differences > 0]))  # TO HANDLE THE LOG OF ZERO ISSUE
    scale = np.exp(mu)
    shape = sigma / lambda_value
    return lognorm(shape, loc=0, scale=scale)

def kolmogorov_structure_functions(differences_dict, scales):
    moments = {n: [] for n in range(1, 6)}  # UP TO THE 5th ORDER MOMENT
    epsilon = 0.1  # HERE IS AN EXAMPLE VALUE, IT SHOULD BE ESTIMATED BASED ON THE IMAGE ANALYSIS OR PROVIDED DATA
    for scale in scales:
        for n in moments:
            moment = np.mean(np.power(differences_dict[scale], n))
            moments[n].append(moment * np.power(scale / epsilon, -n / 3))
    return moments

def plot_pdf(differences_dict, scales):
    plt.figure(figsize=(12, 10))
    for scale in scales:
        differences = differences_dict[scale]
        params = fit_log_normal_with_lambda(differences)
        x = np.linspace(min(differences), max(differences), 100)
        plt.plot(x, params.pdf(x), label=f'Log-Normal Fit Scale {scale}')
        plt.hist(differences, bins=50, density=True, alpha=0.6, label=f'Hist Scale {scale}')
    plt.title('Probability Distribution and Log-Normal Fit of Luminance Differences')
    plt.xlabel('Luminance Difference')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.show()

def compare_painting_statistics(stats1, stats2):
    results = {}
    for n in stats1:
        t_stat, p_value = ttest_ind(stats1[n], stats2[n])
        results[n] = {'t_stat': t_stat, 'p_value': p_value}
    return results

def plot_comparative_statistics(stats):
    fig, ax = plt.subplots(len(stats), 1, figsize=(10, 8))
    for i, n in enumerate(sorted(stats.keys())):
        ax[i].bar(['Painting 1', 'Painting 2'], [np.mean(stats[n]['Painting 1']), np.mean(stats[n]['Painting 2'])], yerr=[np.std(stats[n]['Painting 1']), np.std(stats[n]['Painting 2'])])
        ax[i].set_title(f'Moment {n} Comparison')
        ax[i].set_ylabel('Moment Value')
    plt.tight_layout()
    plt.show()

def main():
    # LOAD AND PROCESS TWO IMAGES FOR COMPARISON
    image_path1 = 'path_to_your_image1.jpg'
    image_path2 = 'path_to_your_image2.jpg'
    scales = [1, 2, 5, 10, 20]
    
    luminance_matrix1 = load_and_convert_to_luminance(image_path1)
    luminance_diffs1 = calculate_luminance_differences(luminance_matrix1, scales)
    moments1 = kolmogorov_structure_functions(luminance_diffs1, scales)
    
    luminance_matrix2 = load_and_convert_to_luminance(image_path2)
    luminance_diffs2 = calculate_luminance_differences(luminance_matrix2, scales)
    moments2 = kolmogorov_structure_functions(luminance_diffs2, scales)
    
    comparison_results = compare_painting_statistics(moments1, moments2)
    
    plot_pdf(luminance_diffs1, scales)
    plot_comparative_statistics(comparison_results)

if __name__ == "__main__":
    main()
