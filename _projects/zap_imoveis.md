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
Rio de Janeiro’s rental market is fragmented across districts, property types, and amenity mixes, making fair pricing unclear. We need a data-driven model to estimate monthly rent from listing attributes and location signals so owners, renters, and investors can benchmark prices and detect mispricing.

## Business Value
- Fair-pricing guidance to reduce lost revenue or vacancy from mispriced listings.
- Faster screening of large listing inventories for investors/operators.
- Transparency into top rent drivers to inform renovation and amenity investments.
- Geospatial insight to prioritize high-yield districts and flag overpriced outliers.

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
- Strongest rent correlates: meterage, bathrooms/suites, and condo_fee; parking contributes with diminishing returns.
- Geography: coastal/west districts (e.g., Barra da Tijuca) command materially higher rents than inland districts.
- Amenities: pool/gym/security align with higher prices; boolean expansion reduced noise from semi-structured text.
- Data quality: regex recovery rescued many missing structural fields, improving coverage and model stability.

## Results
- Clean, enriched dataset with engineered numeric, categorical, and geospatial features.
- Models trained; Random Forest achieved the lowest validation RMSE among tested models, outperforming the linear baseline and shallow regularized XGBoost.
- Delivered visuals: fee/rent histograms, boxplots by district/category, lower-triangle correlation heatmap, geospatial scatter, feature importances, and predicted vs actual scatter.

### Feature Importances (XGBoost)

<iframe src="/assets/images/projects/rental_prices/feature_importances_xgb.html" width="100%" height="500px" style="border: none;"></iframe>

### Model Performance: Actual vs Predicted Rental Prices

<iframe src="/assets/images/projects/rental_prices/scatter_actual_vs_pred_log.html" width="100%" height="500px" style="border: none;"></iframe>

## Next Steps

- Add cross-validation and hold-out test metrics for robust generalization estimates.
- Hyperparameter tune RF/XGBoost; calibrate predictions.
- Incorporate time-based features (listing date) if available; add neighborhood socioeconomic indicators to improve location signal.
- Package the pipeline into a reusable script or service for batch scoring of new listings.
