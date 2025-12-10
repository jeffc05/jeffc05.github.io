---
title: "Rental Price Prediction"
categories:
    - regression
    - webscraping
mathjax: true
toc: true

header:
    teaser: /assets/images/projects/rental_prices/zap-imoveis-image.webp

---

## Overview

End-to-end rental price prediction for Rio de Janeiro using scraped listings from Zap Imóveis. The project covers data collection, cleaning, exploratory analysis, and a gradient-boosted tree model to estimate monthly rent from property attributes and location.

## Data

- Source: Public rental listings on Zap Imóveis (web scraping of search result pages).
- Fields captured: asking rent, condo fee, usable area, bedrooms, bathrooms, parking spots, property type, neighborhood text, and geo hints embedded in listing metadata.
- Storage: cleaned CSV/Parquet files with reproducible scraping scripts and timestamped snapshots so model training can be rerun.
- Quality steps: normalize currency/area units, drop duplicates, trim clear outliers (e.g., zero area or extreme prices), and standardize neighborhood names.

## Pipeline

- Scraping: requests + BeautifulSoup with polite delays, rotating user agents, and pagination guards to avoid hammering the site.
- Feature engineering: log-transformed target, price per square meter, room ratios, condo-fee share, encoded neighborhood, and simple lat/long centroids derived from listing hints.
- Splits: time-aware train/validation to avoid leakage from same-day listings; metrics tracked on a holdout fold.

## Modeling

- Models tried: LightGBM/GradientBoostingRegressor for tabular signals; a regularized linear baseline for sanity checks.
- Objective: minimize MAE on log-rent so large swings are tempered; convert back to currency for reporting.
- Importance summary: location proxy (neighborhood/coords), area, bedrooms, and condo-fee share dominate; bathrooms and parking add secondary lift.

## Results

- The tree model reliably beats the linear baseline on MAE and captures nonlinear location effects without heavy tuning.
- Inspecting SHAP values highlighted overpriced listings and data quirks (e.g., missing condo fees) that were then filtered from training.
- Simple price-per-sqm heuristics remain competitive for central neighborhoods but underperform in suburban zones where condo fees vary widely.

## Next Steps

- Enrich locations with open data: distance to metro/BRT, flood-risk zones, and walkability scores.
- Add temporal effects: listing month/seasonality to track price drift over time.
- Deploy: lightweight FastAPI endpoint plus a small Streamlit dashboard for scenario testing (e.g., tweak area/rooms to see price impact).
- Monitoring: retrain with fresh scrapes monthly and flag neighborhoods whose error distribution drifts beyond a set threshold.
Next, we will implement the pretrained models on downstream tasks including Sequence Classification, NER, POS tagging, and NLI, as well as compare the model's performance with some non-BERT models.

Stay tuned for our next posts! -->
