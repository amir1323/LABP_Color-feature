# Local Average Binary Pattern (LABP) Texture Construction & Color Extraction Method
This repository presents an innovative approach for image retrieval and pattern recognition, with potential applications in fields such as medical imaging and large-scale dataset analysis. The proposed method integrates two novel features:

1. **Local Average Binary Pattern (LABP)**: This model constructs image textures by simultaneously leveraging information from two layers of neighboring pixels. It enhances texture analysis and pattern extraction, leading to more accurate results in identifying and distinguishing image features.

2. **Probabilistic Color Extraction Method**: A color extraction technique based on the discrete joint probability distribution of the RGB channels. This probabilistic approach allows for more precise color feature extraction, contributing to the overall robustness of the model.

In addition, the algorithm incorporates the **Extended Canberra Distance** for comparing feature vectors, improving the precision of image retrieval.

The effectiveness of this method has been validated on benchmark datasets, including **Wang (Corel-1k)** and **Corel-10k**, demonstrating superior precision in comparison with other existing methods.

## 1K images
![1K](images/1K/293.jpg)
![1K](images/1K/302.jpg)
![1K](images/1K/422.jpg)
![1K](images/1K/554.jpg)
![1K](images/1K/630.jpg)

## 10K images
![10K](images/10k/246.jpg)
![10K](images/10k/3827.jpg)
![10K](images/10k/58.jpg)
![10K](images/10k/635.jpg)
![10K](images/10k/883.jpg)

## How to Set Up and Run the Project

### 1. Clone the Repository

Start by cloning the repository to your local machine:


git clone https://github.com/your-username/image-feature-extraction.git

cd image-feature-extraction

### 2. Install Dependencies
Make sure you have Python 3.x installed. Then, install the required dependencies using pip

pip install -r requirements.txt

