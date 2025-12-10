---
title: "Rental Price Prediction"
categories:
  - regression
mathjax: true
toc: true
excerpt: Prediction of rental prices in Rio de Janeiro, RJ
teaser: false
---

![Zap Imóveis rental price dataset sample]({{ '/assets/images/projects/rental_prices/zap-imoveis-image.webp' | relative_url }})

# Rio de Janeiro Rental Property Analysis & Price Prediction

## Project Overview

This project presents a comprehensive analysis of the rental property market in Rio de Janeiro, Brazil, combining web scraping, data cleaning, exploratory analysis, geospatial visualization, and machine learning to predict rental prices.

### Problem Statement

Understanding rental prices in Rio de Janeiro is challenging due to the city's diverse neighborhoods, varying property types, and numerous factors affecting pricing. This project aims to build predictive models that can accurately estimate rental prices based on property characteristics, location, and amenities.

### Data Source

The dataset was collected through web scraping of a major Brazilian real estate platform, containing detailed information about rental properties across Rio de Janeiro, including:
- Property characteristics (size, rooms, amenities)
- Location data (district, neighborhood, coordinates)
- Financial information (rental price, condominium fees, property tax)
- Property descriptions and metadata

### Methodology

The project follows a systematic data science workflow:

1. **Data Collection**: Automated web scraping using SeleniumBase to extract property listings
2. **Data Cleaning**: 
   - Parsing nested JSON structures
   - Text normalization and standardization
   - Regex-based feature extraction
   - Handling missing values through intelligent imputation
3. **Feature Engineering**:
   - Converting amenities into binary features
   - Creating derived features (area ratios)
   - Transforming geographic coordinates to polar coordinates
4. **Exploratory Data Analysis**:
   - Statistical summaries and distributions
   - Outlier detection and removal
   - Correlation analysis
5. **Geospatial Visualization**:
   - Mapping property locations across Rio de Janeiro districts
   - Visualizing rental price patterns geographically
6. **Machine Learning**:
   - Training multiple regression models (Linear Regression, Random Forest, XGBoost)
   - Model comparison using RMSE metrics
   - Performance evaluation on training data

### Key Features

- **Comprehensive data preprocessing** pipeline handling real-world messy data
- **Geospatial analysis** with coordinate transformation and district mapping
- **Feature engineering** to capture meaningful property characteristics
- **Multiple ML models** to compare different approaches
- **Interactive visualizations** using Plotly and static plots with Matplotlib/Seaborn

### Technologies Used

- **Data Processing**: pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Geospatial**: GeoPandas, Shapely
- **Machine Learning**: scikit-learn, XGBoost
- **Web Scraping**: SeleniumBase (in separate scraper module)

### Expected Outcomes

The project delivers:
- Clean, analysis-ready dataset of Rio de Janeiro rental properties
- Insights into rental price distributions and geographic patterns
- Predictive models capable of estimating rental prices
- Comparative analysis of different machine learning approaches