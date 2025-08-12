# CSCA 5632 - Unsupervised Algorithms in Machine Learning

This repository contains all coursework and projects for the University of Colorado Boulder graduate course **CSCA 5632 – Unsupervised Algorithms in Machine Learning**.

### Course Description
This course provides a comprehensive exploration of machine learning algorithms that do not require labeled data. Key topics include dimensionality reduction (PCA, NMF), clustering (K-Means, DBSCAN), and anomaly detection. Projects focus on practical, hands-on implementation of these algorithms to solve real-world problems.

## Repository Structure

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
            <td><b>This project's main folder.</b></td>
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
            <td>HTML, PDF, and DOCX versions of the notebook.</td>
        </tr>
        <tr>
            <td><code>│&nbsp;&nbsp;&nbsp;└── 📁 Limitations of sklearn NMF/</code></td>
            <td><i>(placeholder for a future project)</i></td>
        </tr>
        <tr>
            <td><code>├── 📁 Week5/</code></td>
            <td><i>(placeholder for a future project)</i></td>
        </tr>
        <tr>
            <td><code>└── 📄 README.md</code></td>
            <td>The main README file for the course repository.</td>
        </tr>
    </tbody>
</table>

## Week 4 - Kaggle Mini-Project: BBC News Classification

### Overview
This project tackles the **BBC News Classification dataset** from Kaggle. The goal was to build and compare two distinct NLP pipelines for classifying articles into five categories (Business, Entertainment, Politics, Sport, and Tech). The analysis directly contrasts a traditional unsupervised approach (**TF-IDF + NMF**) with a modern, deep learning approach (**BERT embeddings + Logistic Regression**).

### Key Finding
The analysis concluded that the BERT-based pipeline was dramatically superior, achieving **100% training accuracy** due to the high-quality, separable feature space created by its contextual embeddings.

---
<p align="center">
  Licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.
</p>
