#!/bin/bash

# ================================
# Environment Setup Script
# ================================

echo "Setting up Python environment..."

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install pyspark==3.5.0 pandas numpy matplotlib scikit-learn

echo "Environment setup completed successfully."
