# **CSCA 5632: Unsupervised Algorithms in Machine Learning**

This repository contains my work for Weeks 4 and 5 of the ***University of Colorado Boulder*** graduate course **CSCA 5632: Unsupervised Algorithms in Machine Learning**.

The focus in these weeks was on hands-on projects using real datasets. Topics include text classification with traditional and deep learning methods, evaluation of recommender system algorithms, and an in-depth unsupervised analysis of autonomous vehicle trajectory data.

## **Repository Structure**

<table>
    <thead>
        <tr>
            <th align="left">Path</th>
            <th align="left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>CSCA-5632-Unsupervised-Algorithms-in-Machine-Learning/</code></td>
            <td>Main repository for the course.</td>
        </tr>
        <tr>
            <td><code>├── 📁 Week4/</code></td>
            <td>Contains all projects for Week 4.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;└── 📁 Kaggle Mini-Project: BBC News Classification/</code></td>
            <td><b>Week 4 Part 1</b> <b><i>Peer-graded Assignment</i></b>.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📁 datasets/</code></td>
            <td>Raw data from the Kaggle competition.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📁 embeddings/</code></td>
            <td>Pre-computed BERT embeddings and metadata.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📁 models/</code></td>
            <td>Saved trained model objects (.joblib files).</td>
        </tr>
       <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📁 plots/</code></td>
            <td>Saved images of key visualizations.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📁 submissions/</code></td>
            <td>Final submission files (.csv).</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📄 Week4_Kaggle_BBC_News_Classification.ipynb</code></td>
            <td>The main Jupyter Notebook for the project.</td>
        </tr>
       <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 📄 (other exports)</code></td>
            <td>HTML and PDF versions of the final notebook. </td>
        </tr>
       <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 🖼️ kaggle_submission_screenshot_combined.png</code></td>
            <td>Screenshot of final NMF and BERT submission scores on Kaggle.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;└── 📁 Limitations of sklearn NMF/</code></td>
            <td><b>Week 4 Part 2</b> <b><i>Peer-graded Assignment</i></b>.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📁 artifacts/</code></td>
            <td>Saved model outputs (factors, predictions, metadata).</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📁 datasets/</code></td>
            <td>The MovieLens datasets used for the project.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📁 plots/</code></td>
            <td>Saved images of key visualizations from the notebook.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📄 Week4_Limitations_of_sklearn_NMF.ipynb</code></td>
            <td>The main Jupyter Notebook for the project.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 📄 (other exports)</code></td>
            <td>HTML and PDF versions of the final notebook.</td>
        </tr>
        <tr>
            <td><code>├── 📁 Week5/</code></td>
            <td>Contains the final project for the course.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;├── 📁 plots/</code></td>
            <td>Saved images, Scenario Cards, and visualizations from the notebook.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;├── 📁 results/</code></td>
            <td>Final summary spreadsheets comparing the two pipelines (CSV and XLSX).</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;├── 📁 scenario_replays/</code></td>
            <td>Animated MP4 video replays of representative scenarios.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;├── 📄 CSCA5632_Final_Project_Lyft.ipynb</code></td>
            <td>The main Jupyter Notebook for the final project.</td>
        </tr>
       <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;└── 📄 (other exports)</code></td>
            <td>HTML and PDF versions of the final notebook. </td>
        </tr>
        <tr>
            <td><code>└── 📄 README.md</code></td>
            <td>The main README file for the course repository.</td>
        </tr>
    </tbody>
</table>

**Note:** Datasets for Week 5 are not tracked in git due to size limits. The full dataset is about 23.7 GB. See the Kaggle data pages linked below.
> Week 5 Dataset: https://www.kaggle.com/competitions/lyft-motion-prediction-autonomous-vehicles/data

---

## **Week 5 - Final Project: Unsupervised Discovery of Driving Behaviors**

### Overview
This project reframes the Lyft Level 5 motion prediction dataset for an unsupervised learning task. It develops and compares two distinct pipelines for discovering behavioral archetypes from raw trajectory data:
- **Pipeline A**: A classical approach using hand-engineered features with PCA and KMeans.
- **Pipeline B**: A deep learning approach using a GRU-based autoencoder to learn embeddings, followed by KMeans.

### Key Finding
The deep learning pipeline (Pipeline B) proved decisively superior. Its learned embeddings produced clusters that were both quantitatively better (Silhouette score of **0.935** vs. 0.558) and more stable (ARI of **0.996** vs. 0.779). The final comparison revealed that while both pipelines agreed on complex maneuvers, the deep learning approach was able to discover more nuanced sub-groups within simpler, high-speed behaviors, demonstrating its advanced representational power.

---

## **Week 4 - Kaggle Mini-Project: BBC News Classification**

### Overview
This project tackles the **BBC News Classification dataset** from Kaggle. The goal was to build and compare two distinct NLP pipelines for classifying articles into five categories (Business, Entertainment, Politics, Sport, and Tech). The analysis directly contrasts a traditional unsupervised approach 
- **TF-IDF + NMF**: A traditional unsupervised topic modeling approach. 
- **BERT embeddings + Logistic Regression**: A modern method using contextual embeddings. 

### Key Finding
The analysis concluded that the BERT-based pipeline was dramatically superior, achieving **100% training accuracy** due to the high-quality, separable feature space created by its contextual embeddings.

---

## **Week 4 – Limitations of sklearn NMF**

### Overview 
This project tested **Non-negative Matrix Factorization (NMF)** and **Truncated SVD** from ***scikit-learn*** on the MovieLens dataset and compared them to the best model from Week 3 collaborative filtering with Jaccard similarity. The goal was to see how these standard matrix factorization tools hold up in a sparse data setting.

### Key Finding 
The Jaccard similarity model from Week 3 achieved an RMSE of 0.9509. The best NMF run (k=30) and the best Truncated SVD run (k=20) came in at 1.018 and 1.017, roughly 0.07 higher. The main reason for the drop in accuracy is that scikit-learn’s NMF and SVD require a complete matrix. Since over 96% of the ratings were missing, they were filled with the global mean before training, which diluted the real patterns in the data.

### ***Suggested Fix*** Use methods built for sparse recommendation data, like Alternating Least Squares (ALS) with bias terms, or other algorithms that can train only on the actual ratings without filling in the rest.

---
<p align="center">
  Licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.
</p>
