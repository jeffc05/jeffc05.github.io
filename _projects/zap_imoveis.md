---
title: "Rio de Janeiro Rental Property Analysis & Price Prediction"
categories:
  - regression
mathjax: true
toc: true
teaser: false
---

![Zap Imóveis rental price dataset sample](/assets/images/projects/rental_prices/zap-imoveis-image.webp)

## Problem Statement

Rio de Janeiro’s rental market varies widely across neighborhoods, property types, and amenities. Renters and investors need a data-driven way to estimate fair rental prices and compare listings. This project builds predictive models to estimate rental prices (`rental_price`) from property characteristics, location, and amenities.

## Business Value

- **Pricing guidance**: Provides an estimated fair rent for new or existing listings, reducing under/over-pricing risk.
- **Market transparency**: Highlights drivers of rent (size, location, amenities) to inform negotiations and investment decisions.
- **Operational efficiency**: Automates feature extraction and prediction, enabling faster portfolio screening.
- **Geospatial insight**: Maps price patterns across districts to target high-demand, high-yield areas.

## Methodology

1. **Data collection**: Web scraping of a major Brazilian real estate portal; raw JSON stored with listing details.
2. **Cleaning & normalization**: Handle `N/A`, lowercasing, standardize categories, parse coordinates, and numeric extraction for prices/fees.
3. **Feature engineering**: Expand nested amenities to booleans; extract counts (rooms, baths, parking, suites); derive ratios (meterage per room/bath/suite); convert coordinates to polar; handle missing values via regex extraction and targeted fills.
4. **Exploratory analysis**: Distributions, outlier filtering (rental_price < 120k, condo_fee < 10.5k, property_tax < 75k), correlation heatmaps.

### Rental Price Distribution by Category

<iframe src="/assets/images/projects/rental_prices/box_rental_by_category.html" width="100%" height="500px" style="border: none;"></iframe>

### Rental Price Distribution by District

<iframe src="/assets/images/projects/rental_prices/box_rental_by_district.html" width="100%" height="500px" style="border: none;"></iframe>

### Rental Price Distribution by Category and District

<iframe src="/assets/images/projects/rental_prices/box_rental_by_category_and_district.html" width="100%" height="500px" style="border: none;"></iframe>

### Geospatial Price Analysis: Rio de Janeiro

![Rio de Janeiro rental price geospatial analysis](/assets/images/projects/rental_prices/rio_de_janeiro.png)

5. **Geospatial analysis**: Project coordinates (UTM 23S) for accurate geometry; map rental prices over Rio districts using GeoPandas/Matplotlib.



6. **Modeling**: Encode features with DictVectorizer; train Linear Regression, Random Forest, and XGBoost; evaluate via RMSE on training data.

## Findings

- **Price drivers**: Meterage, number of bathrooms/suites, and condo_fee show strong positive correlation with rent; parking spaces add value but with diminishing returns.
- **Geography matters**: Coastal and west zones (e.g., Barra da Tijuca) show higher rents; inland districts trend lower.
- **Amenities**: Presence of key amenities (e.g., pool, gym, security) aligns with higher rents; amenity columns converted to boolean indicators reduced noise.
- **Data quality**: Many listings lacked explicit counts; regex-based extraction from descriptions recovered missing rooms/parking/floor_level values.

## Results

- **Clean dataset**: Deduplicated, standardized, and enriched with engineered features and geospatial transforms.
- **Models trained**: Linear Regression (baseline), Random Forest, and XGBoost; tree-based models fit training data best (lowest RMSE on train), indicating non-linear relationships.
- **Visualization outputs**: Histogram/boxplots for fees and rent, correlation heatmaps, and geospatial scatter over district polygons.
- **Actionable use**: The pipeline can score new listings to suggest fair rent and identify outlier pricing; geospatial views guide area targeting.

### Feature Importances (XGBoost)

<iframe src="/assets/images/projects/rental_prices/feature_importances_xgb.html" width="100%" height="500px" style="border: none;"></iframe>

### Model Performance: Actual vs Predicted Rental Prices

<iframe src="/assets/images/projects/rental_prices/scatter_actual_vs_pred_log.html" width="100%" height="500px" style="border: none;"></iframe>

## Next Steps

- Add cross-validation and hold-out test metrics for robust generalization estimates.
- Hyperparameter tune RF/XGBoost; calibrate predictions.
- Incorporate time-based features (listing date) if available; add neighborhood socioeconomic indicators to improve location signal.
- Package the pipeline into a reusable script or service for batch scoring of new listings.
