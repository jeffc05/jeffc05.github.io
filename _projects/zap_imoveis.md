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

1. **Data collection**: Web scraping of Zap Imóveis, a major Brazilian real estate portal; raw JSON stored with listing details.
2. **Cleaning & normalization**: Handle missing values, lowercasing, standardize categories, parse coordinates, and numeric extraction for prices/fees.
3. **Feature engineering**: Expand nested amenities to booleans; extract counts (rooms, baths, parking, suites); derive ratios (meterage per room/bath/suite); convert coordinates to polar; handle missing values via regex extraction and targeted fills.
4. **Exploratory analysis**: Distributions, outlier filtering (rental_price < 120k, condo_fee < 10.5k, property_tax < 75k), correlation heatmaps.
5. **Geospatial analysis**: Project coordinates (UTM 23S) for accurate geometry; map rental prices over Rio districts using GeoPandas/Matplotlib.
6. **Modeling**: Encode features with DictVectorizer; train Linear Regression, Random Forest, and XGBoost; evaluate via RMSE on training data.

## Findings

- Median rent tops out for penthouses (cobertura), bottoms out for studios (kitnet), and spikes for houses (casa).
![Rental price distribution by category](/assets/images/projects/rental_prices/box_rental_by_category.png)
- South district (sul) median rent runs higher, but the peak prices are in the west district (oeste).
![Rental price distribution by district](/assets/images/projects/rental_prices/box_rental_by_district.png)
- Not only does the median rent run higher in the south district (sul), but the same pattern is also observable when property types are analyzed individually.
![Rental price distribution by category and district](/assets/images/projects/rental_prices/box_rental_by_category_and_district.png)
- South (sul) and west (oeste) districts command materially higher rents than inland districts.
![Rio de Janeiro rental price geospatial analysis](/assets/images/projects/rental_prices/rj_rental_prices.png)

## Results
- Clean, enriched dataset with engineered numeric, categorical, and geospatial features.
- Models trained; XGBoost achieved the lowest validation RMSE among tested models, outperforming the linear baseline and Random Forest.
- Rio de Janeiro Rent Pricer App deployed using Streamlit

### Feature Importances (XGBoost)

![Feature importances from XGBoost model](/assets/images/projects/rental_prices/feature_importances_xgb.png)

### Model Performance: Actual vs Predicted Rental Prices

![Actual vs predicted log rental prices](/assets/images/projects/rental_prices/scatter_actual_vs_pred_log.png)