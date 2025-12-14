---
title: "Predicting Rio de Janeiro's Rental Market: What Data Reveals About Housing Prices"
categories:
  - regression
mathjax: true
toc: true
teaser: false
---

![Zap Imóveis rental price dataset sample](/assets/images/projects/rental_prices/zap-imoveis-image.webp)

## Introduction

The rental housing market in Rio de Janeiro is notoriously unpredictable. Landlords struggle to set fair prices, tenants hunt endlessly for affordable options, and investors wonder where to place their capital. What if data could illuminate this murky landscape?

Over the past months, I've collected and analyzed thousands of rental listings across Rio's neighborhoods—from the bustling Zona Sul to the emerging Zona Oeste. Using machine learning, I've uncovered the hidden patterns that drive rental prices. The results are surprising, sometimes counterintuitive, and potentially valuable for anyone involved in Rio's housing market.

This is the story of how data science turned chaos into clarity.

---

## The Data Challenge

Rio de Janeiro's real estate market spans a vast geographic and economic landscape. To build a reliable predictive model, I needed comprehensive data capturing the diversity of the market. The data was scraped from a Zap Imoveis, a major Brazilian real estate portal.

**What I Collected:**
- 3,000+ rental listings across Rio's neighborhoods
- Property attributes: size (meterage), rooms, bathrooms, parking spaces, amenities
- Financial data: condo fees, property taxes, rental prices
- Geographic coordinates converted to polar coordinates for spatial analysis
- Building features: balconies, gardens, air conditioning, furnished status, etc

**Data Quality Challenges:**
- Missing values in financial data (many listings don't disclose fees)
- Outliers in price and property sizes (luxury penthouses vs. studios)
- Inconsistent property categorization (casa, apartamento, cobertura, sobrado)
- Sparse data from certain neighborhoods

The cleaning process alone revealed the messy reality of how real estate data is recorded in Brazil. But once normalized, the data told a clear story.

---

## What Drives Rental Prices? The Distribution Story

Let's start with the fundamentals. How are rental prices distributed across Rio?

**The Rental Price Distribution** shows that prices follow a log-normal pattern —- most properties cluster in the middle range, with a long tail of expensive luxury rentals. This is typical for housing markets: plenty of mid-range options, fewer budget apartments, and exclusive high-end properties pulling the average upward.

![Distribution of rental prices](/assets/images/projects/rental_prices/hist_log_rental_price.png)

**Financial Obligations Vary Wildly:**
- Condo fees show extreme variation —- some buildings charge minimal fees, others expect thousands in monthly maintenance costs

![Distribution of condo fees](/assets/images/projects/rental_prices/hist_condo_fee.png)

- Property taxes (IPTU) follow a similar pattern, with many properties marked as "isento" (exempt)

![Distribution of property tax](/assets/images/projects/rental_prices/hist_property_tax.png)

These hidden costs often surprise tenants and can swing a property's desirability. A cheap rent with R$ 500 condo fees beats an affordable rent with R$ 1,500 in additional expenses.

---

## Geography Matters: The District Effect

Rio divides into distinct zones -— Norte, Sul, Oeste, Leste, Centro. Each has its character, history, and price point.

**The Rental Price by District** visualization reveals:

![Rental price distribution by district](/assets/images/projects/rental_prices/box_rental_by_district.png)

- **Zona Sul (South)**: The premium zone. Leblon, Ipanema, Copacabana command the highest rents. Proximity to beaches, established infrastructure, and social prestige push prices up 30-40% above the city average.

- **Zona Oeste (West)**: The emerging frontier. Barra da Tijuca and surrounding areas offer newer, modern apartments at lower costs than traditional south-zone neighborhoods. Young professionals are migrating here, and prices are rising accordingly.

- **Zona Norte (North)**: The value zone. More affordable, less touristy, home to working-class and middle-class families. Growing infrastructure improvements are slowly attracting younger renters seeking better value.

- **Centro**: Historic but declining. Once the heart of Rio, it struggles with safety concerns and aging infrastructure. Rental prices reflect this -— low relative to location.

![Rio de Janeiro rental price geospatial analysis](/assets/images/projects/rental_prices/rj_rental_prices.png)

**The Key Insight:** Geography explains perhaps 20-30% of price variance. But it's not just coordinates -— it's the infrastructure, services, and social capital attached to each zone.

---

## Property Type: The Category Question

Rio's real estate categories reflect its history and architecture:

- **Apartamentos**: Apartment buildings, the dominant form. Efficient and standard.
- **Casas**: Standalone houses. Less common in prime areas, more common in suburbs.
- **Coberturas**: Penthouses and top-floor units. Premium pricing for views and exclusivity.
- **Sobrados**: Two-story houses. A middle ground between apartments and mansions.

**The Rental Price by Category** data shows clear stratification:

![Rental price distribution by category](/assets/images/projects/rental_prices/box_rental_by_category.png)

- **Coberturas** command premium prices -- 2-3x apartments in the same district
- **Apartamentos** are the market standard with tight price clustering
- **Casas and Sobrados** offer variety—some are luxury, some are modest, creating wider price spreads
  
![Rental price distribution by category and district](/assets/images/projects/rental_prices/box_rental_by_category_and_district.png)

For landlords, the property type constrains your market segment. You can't price a apartment like a penthouse, no matter the location. For tenants, understanding these categories helps calibrate expectations.

---

## The Secret Ingredient: Meterage and Amenities

Beyond location and type, what else matters?

**Meterage (Property Size)** is crucial. The relationship between square footage and rental price isn't linear —- a 100m² apartment costs more than double a 50m² one because of layout efficiency and amenity requirements.

**Amenities** create the final layer of differentiation:
- Air conditioning (highly valued in Rio's tropical climate)
- Furnished vs. unfurnished (massive price difference)
- Kitchen quality
- Parking spaces (often undervalued but essential in congested areas)
- Outdoor space (gardens, balconies)

The **Feature Correlation Matrix** reveals that size, financial obligations, and amenities cluster together -— larger properties tend to have more amenities and higher fees.

![Feature correlation matrix](/assets/images/projects/rental_prices/feature_correlation.png)

But notably, some features show surprising independence. A small, unfurnished apartment in Zona Sul can outrent a spacious furnished casa in Zona Oeste, simply due to geographic prestige.

---

## Building the Machine: Modeling Rio's Market

With data in hand, I built three predictive models:

**Linear Regression (Baseline)**
- RMSE: High variance
- Interpretable but unable to capture non-linear relationships
- Useful for understanding feature importance in isolation

**Random Forest (Middle Ground)**
- RMSE: Improved, capturing non-linear interactions
- Better at handling outliers
- But still missing the full picture

**XGBoost (The Winner)**
- RMSE: Lowest error, consistent across train and validation sets
- Handles feature interactions brilliantly
- Captures the nuanced pricing logic of Rio's market

Why XGBoost? It iteratively builds decision trees, focusing on the hardest-to-predict cases. This is exactly what a housing market demands—standard cases are easy, but predicting luxury properties or bargain finds requires sophisticated pattern recognition.

**Top Features by Importance (XGBoost):**

![Feature importances from XGBoost model](/assets/images/projects/rental_prices/feature_importances_xgb.png)

1. Meterage (25%) - Size dominates pricing
2. Condo fees (15%) - Financial burden directly impacts rental value
3. Property tax (12%) - Another form of hidden cost
4. Number of rooms (10%) - Directly tied to usable space
5. Geographic location (7%) - Important but less dominant than expected
6. Spatial coordinates (6%) - Captures local micro-geography

The data speaks: **size and costs are king**. Location matters, but a massive cheap apartment in a secondary zone can compete with a tiny expensive one in prime real estate.

---

## Model Validation: Can We Trust These Predictions?

The litmus test: **Actual vs. Predicted Log Rental Price** scatter plot. The closer points hug the diagonal line, the better the model.

![Actual vs predicted log rental prices](/assets/images/projects/rental_prices/scatter_actual_vs_pred_log.png)

Our XGBoost model shows:
- Tight clustering around the diagonal for most properties
- Better accuracy for mid-range prices
- Some drift in extreme cases (ultra-luxury and budget options)

This is expected and acceptable. The model captures the mainstream market excellently, which is where 80% of activity happens anyway. Predicting outliers requires more data or specialized expertise.

**Confidence Interval Analysis:**
- Standard error: ~0.12 log-units = ~13% on prices
- Translation: For a R$ 3,000 apartment, we predict within ~R$ 350-400
- Acceptable for market analysis, though investors want tighter predictions

---

## Insights for Different Stakeholders

### For Landlords

Your rental price should consider:
1. **Get the basics right**: Size is non-negotiable. A 100m² apartment in Zona Oeste should rent for significantly more than a 60m² one, even if both are nice.
2. **Disclose all fees**: Apartments with high condo fees need to offset this with location prestige or amenities. Don't hide costs -— they become negotiating weapons.
3. **Zone positioning**: Decide if you're competing on location prestige (Zona Sul premium) or value (Zona Oeste/Norte emerging). Mixed positioning confuses the market.

### For Tenants

Don't just look at rent:
1. **Calculate total housing cost**: Rent + condo + tax + utilities. Often the "cheap" apartment isn't actually cheap.
2. **Understand your zone**: You're not paying for just the apartment -— you're paying for the neighborhood. Be intentional about this trade-off.
3. **Check assumptions**: If an apartment seems underpriced, investigate. Missing amenities, problematic building, or data errors often explain bargains.

### For Investors

Three strategies emerge:
1. **Zona Sul premiumization**: Buy undervalued properties in established zones, improve, and capture location uplift
2. **Zona Oeste growth**: Acquire properties as infrastructure improves and migration accelerates
3. **Off-type arbitrage**: Find casas and sobrados priced like apartments; repositioning drives returns

---

## The Limitations: What the Model Doesn't Capture

Machine learning is powerful but not omniscient. Here's what this analysis misses:

- **Macro economics**: Interest rates, currency fluctuations, and capital flows shift demand
- **Neighborhood transitions**: A zone's trajectory (improving vs. declining) isn't captured by static data
- **Social factors**: Crime, schools, culture create intangibles that pricing adjusts for but data doesn't explain
- **Individual stories**: The model knows averages, not why *you* specifically need an apartment
- **Temporal effects**: This analysis is a snapshot; the rental market evolves

The model is a powerful tool, not a crystal ball. It illuminates patterns but requires human judgment to apply.

---

## Real-time prediction

Built a web tool that returns instant rental valuations from user inputs.

## What's Next?

This analysis opens doors:

1. **Temporal analysis**: Track how prices evolve over months and years
2. **Neighborhood clustering**: Use unsupervised learning to identify micro-markets beyond geographic zones
3. **Market simulation**: Test "what-if" scenarios —- how would a new metro line affect prices?

The data foundation is solid. The next chapter is turning these insights into actionable tools.

---

## Conclusion

Rio de Janeiro's rental market is complex, but not random. Size matters, location matters, costs matter. The precise interplay between these factors follows patterns that machine learning can illuminate.

The big takeaway: **The housing market has logic**. It's not magical or mysterious -— it's physics applied to human choices. When you understand the underlying patterns, you stop being a passive participant and become a strategic player.

Whether you're a landlord setting prices, a tenant negotiating rent, or an investor hunting opportunities, data-driven thinking gives you an edge. In a market as competitive as Rio's, that edge matters.

---

## Technical Details

**Models Used**: Linear Regression, Random Forest, XGBoost  
**Dataset Size**: ~3,000 cleaned rental listings  
**Features**: 22 engineered variables capturing property, financial, and geographic dimensions  
**Validation**: 80-20 train-test split with stratified sampling  
**Tool Stack**: Python, Pandas, Scikit-learn, XGBoost, Plotly, Selenium