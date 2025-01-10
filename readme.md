# Documently_Model

## Overview
Documently_Model is a machine learning model trained for document processing and analysis tasks. The model demonstrates strong performance across multiple evaluation metrics including BLEU and ROUGE scores.

## Model Performance

### Training Metrics
- **Training Loss**: 4.8842 (at step 100)
- **BLEU Score**: 0.5603 (56.03%)
- **ROUGE Scores**:
  - ROUGE-1: 0.7260 (72.60%)
  - ROUGE-2: 0.7232 (72.32%)
  - ROUGE-L: 0.7260 (72.60%)

These metrics indicate strong performance in text generation and similarity tasks, with particularly high ROUGE scores suggesting good accuracy in content matching.

## Model Registration Details

### Version Information
- **Model Name**: Documently_Model
- **Version**: 1
- **Stage**: Production
- **Status**: READY
- **Creation Timestamp**: 1736519125317
- **Last Updated**: 1736519135825

### Storage Information
- **Run ID**: f430f93f0d1e4dc7b3ed33132f08709d
- **Source Path**: file:///content/mlflow/764370464625452762/f430f93f0d1e4dc7b3ed33132f08709d/artifacts/model

## Technical Details

### Evaluation Metrics Explained
- **BLEU Score**: A metric for evaluating the quality of machine-translated text, ranging from 0 to 1. Our score of 0.5603 indicates good translation quality.
- **ROUGE Scores**: Metrics for evaluating automatic summarization and translation:
  - ROUGE-1: Measures unigram overlap
  - ROUGE-2: Measures bigram overlap
  - ROUGE-L: Measures longest common subsequence

### MLflow Integration
The model is registered and tracked using MLflow, providing:
- Version control
- Model lineage tracking
- Deployment stage management
- Artifact storage

## Usage

To use this model, you can access it through MLflow using the following information:
```python
model_name = "Documently_Model"
version = "1"
stage = "Production"
```

## Model Artifacts
The model artifacts are stored in the MLflow tracking server and can be accessed using the provided source path.

## Current Status
The model is currently in Production stage and is ready for use (Status: READY).

---

*Note: This README is generated based on model training and registration results. For the most up-to-date information, please consult the MLflow tracking server.*
