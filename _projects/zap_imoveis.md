---
title: "Rio de Janeiro Rental Property Analysis & Price Prediction"
categories:
  - regression
mathjax: true
toc: true
teaser: false
---

![Zap Imóveis rental price dataset sample](/assets/images/projects/rental_prices/zap-imoveis-image.webp)

# Problem Statement
Rio de Janeiro’s rental market is fragmented across districts, property types, and amenity mixes, making fair pricing unclear. We need a data-driven model to estimate monthly rent from listing attributes and location signals so owners, renters, and investors can benchmark prices and detect mispricing.

# Business Value
- Fair-pricing guidance to reduce lost revenue or vacancy from mispriced listings.
- Faster screening of large listing inventories for investors/operators.
- Transparency into top rent drivers to inform renovation and amenity investments.
- Geospatial insight to prioritize high-yield districts and flag overpriced outliers.

# Methodology
1) **Data acquisition**: Scrape portal listings; ingest newline-delimited JSON and wrap into a valid array.
2) **Cleaning/normalization**: Lowercase/strip text; standardize categories; parse coordinates; extract numerics for rental_price/condo_fee/property_tax.
3) **Feature engineering**: Expand nested amenities to booleans; regex-recover missing counts (rooms, baths, parking, suites, floor); create density ratios (meterage per room/bath/suite); convert lon/lat to polar (r, theta); targeted fills/sentinels; deduplicate and remove extreme outliers.
4) **EDA & geospatial**: Plot fee/rent distributions with box marginals; boxplots by district/category; masked correlation heatmap; GeoPandas scatter over district polygons.
5) **Modeling**: Train/val/test split; DictVectorizer for categorical/boolean features; models: Linear Regression (baseline), Random Forest, XGBoost; metric: RMSE on log_rental_price.

# Findings
- Strongest rent correlates: meterage, bathrooms/suites, and condo_fee; parking contributes with diminishing returns.
- Geography: coastal/west districts (e.g., Barra da Tijuca) command materially higher rents than inland districts.
- Amenities: pool/gym/security align with higher prices; boolean expansion reduced noise from semi-structured text.
- Data quality: regex recovery rescued many missing structural fields, improving coverage and model stability.

# Results
- Clean, enriched dataset with engineered numeric, categorical, and geospatial features.
- Models trained; Random Forest achieved the lowest validation RMSE among tested models, outperforming the linear baseline and shallow regularized XGBoost.
- Delivered visuals: fee/rent histograms, boxplots by district/category, lower-triangle correlation heatmap, geospatial scatter, feature importances, and predicted vs actual scatter.

# Next Steps
- Add cross-validation and hold-out test metrics for robustness.
- Hyperparameter-tune RF/XGBoost and consider simple ensembling.
- Incorporate time-based and external socioeconomic/location features.
- Package the pipeline for batch scoring or an API; persist the best model and vectorizer for reuse.
- Convert remaining static plots (e.g., geospatial) to interactive variants if deeper exploration is needed.
