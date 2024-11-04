# Startups Profit Analysis and Predictive Modelling

An analysis and a Machine Learning-based web application that predicts startup profitability based on R&D, Administration, and Marketing spend in different states using a trained model deployed with Streamlit.

---

## Project Overview

In the competitive business environment, predicting profitability can guide investment decisions. This project is designed to forecast a startup's profit based on spending in critical areas like R&D, administration, and marketing, with consideration of geographical impact by state. 

## Problem Statement

Given the expenditure data across R&D, Administration, and Marketing for 50 startups, **can we predict their profit and understand spending efficiency for optimal resource allocation**?

## Project Objective

1. **Build a predictive model** to forecast startup profit based on expenditure data.
2. **Identify key spending areas** that influence profit maximization.
3. **Deploy an interactive application** that allows users to input their startup spending and receive a profit prediction.

## Table of Contents

- [Data Overview](#data-overview)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Preprocessing](#data-preprocessing)
- [Model Building](#model-building)
- [Model Evaluation](#model-evaluation)
- [Deployment](#deployment)
- [Conclusion](#conclusion)
- [Acknowledgments](#acknowledgments)

---

## Data Overview

The dataset was sourced from Kaggle, named `50_Startups.csv`, includes the following variables:

- **R&D Spend**: Expenditure on research and development.
- **Administration**: Expenditure on administrative activities.
- **Marketing Spend**: Expenditure on marketing.
- **State**: Location of the startup (California, Florida, or New York).
- **Profit**: Target variable representing the startup's profit.

## Exploratory Data Analysis

Key observations and visualizations were created to understand the data better:

1. **Profitability Analysis**: Scatterplots for each spending category and correlarion matrix heatmap were made to check for their relationship with the profit.
2. **Comparison Across States**: Barplots and Boxplots to analyze profit differences across California, Florida, and New York.
3. **Developing Investment Strategies**: Correlation heatmaps and Regression plots to reinforce that strategic investments in R&D and marketing are key drivers of profitability across these states


**Profitability Analysis**

![Scatterplots](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/0e95c70354c56cef5b50a3839c44ac21e3b17353/50%20start%20ups%20profitability%20analysis.png)

**Key insights**
**R&D Spend vs. Profit**:

 - **Clear Positive Correlation**: The more a company spends on R&D, the higher the profit. The data points forming a tight cluster around a straight line indicates a strong correlation. This suggests that investment in innovation and development is paying off well.

**Administration vs. Profit**:

 - **No Clear Relationship**: The wide scattering of data points with no discernible pattern suggests that spending on administration does not significantly impact profitability. This could mean that companies' profitability may be more influenced by other factors than administrative expenses.

**Marketing Spend vs. Profit**:

 - **Moderate Positive Correlation**: While there's a positive relationship, it's not as strong as R&D spend. The points are more spread out, indicating that while marketing investment does contribute to profit, it's less consistently impactful compared to R&D. This might suggest varying returns on marketing investments depending on strategies or market conditions.


![Correlation Matrix Heatmaps](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/92e39a7dabf282c997f852345abcbeb5ec708e26/corr%20matrix.png)

**Key insights**
 - **R&D Spend and Profit**: Strong correlation (0.97). This further emphasizes that higher R&D investment leads to higher profits. Innovation drives success.

 - **Marketing Spend and Profit**: Also a strong correlation (0.75), though slightly less than R&D. Effective marketing campaigns clearly boost profits.

 - **Administration Spend and Profit**: Weak correlation (0.20). As suspected, administrative costs don’t impact profitability significantly.

 - **State and Profit**: Negligible correlation (0.05). Location seems to have minimal direct impact on profitability.


**Comparison Across States**

![Barplot](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/92e39a7dabf282c997f852345abcbeb5ec708e26/comparison%20across%20states.png)

**Key insights**
 - **Florida** leads the pack with the highest average profit. Looks like Sunshine State startups are basking in profitability.

 - **New York** comes in second. The city's hustle clearly translates to healthy profits, albeit slightly trailing Florida.

 - **California** is in third place, which is interesting given its prominent tech industry. Possibly intense competition or higher costs might be influencing this.

These differences might reflect varying business environments, costs of operation, or even market sizes.


![Barplot](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/92e39a7dabf282c997f852345abcbeb5ec708e26/spend%20by%20cat%20and%20state.png)

**Key insights**
 - **Marketing Spend**: Florida leads with an astonishing average spend of around 250,000, followed by New York at about 200,000, and California at 150,000. It’s clear that marketing is a top priority, particularly in Florida.

 - **Administration Costs**: These are relatively consistent across states, averaging around 100,000 for New York and California, and slightly higher at 125,000 for Florida.

 - **R&D Spend**: Also quite uniform, with all three states hovering around the 50,000 to 75,000 mark.

Florida's substantial investment in marketing and administrative expenses stands out as a potential driver for its higher profitability. Meanwhile, R&D spend remains steady across the board.


![Boxplot](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/92e39a7dabf282c997f852345abcbeb5ec708e26/boxplot.png)

**Key insights**
**R&D Spend**:

 - **New York and California**: Similar spread and medians around 75,000. Suggests consistency in R&D investment.

 - **Florida**: Slightly higher median at 100,000. This aligns with Florida's top profitability rank; higher R&D might be a factor.


**Administration Spend**:

 - **New York and California**: Median at 125,000, with some outliers. A larger consistent investment here.

 - **Florida**: Slightly lower median at 100,000, but still has outliers. Indicates a potential strategy to reduce admin costs while maintaining profitability.


**Marketing Spend**:

 - **New York and Florida**: Higher medians around 200,000. This could explain their strong performance.

 - **California**: Lower median at 150,000 with more variability. Perhaps diverse strategies lead to different returns on marketing investment.


**Developing Investment Strategies**

![corrheatmap](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/92e39a7dabf282c997f852345abcbeb5ec708e26/corr%20heatmap%20for%20NY.png)

**Key insights**
 - **R&D Spend and Profit**: A near-perfect correlation of 0.98 underscores the significant impact of R&D investment on profitability in New York. Prioritizing R&D seems to be a critical driver for startups here.

 - **Marketing Spend and Profit**: A robust correlation of 0.81, suggesting that strategic marketing investments also play a major role in boosting profits.

 - **Administration and Profit**: Moderate correlation of 0.40, indicating that administrative spending is less impactful on profitability compared to R&D and Marketing, but still worth considering.

 - **R&D and Marketing Spend**: The strong correlation of 0.80 between these two suggests companies that invest in R&D also tend to invest heavily in marketing. This alignment might hint at integrated strategies to innovate and then promote those innovations effectively.

Overall, investing in R&D and Marketing stands out as the most effective strategy for driving profit in New York.


![corrheatmap](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/92e39a7dabf282c997f852345abcbeb5ec708e26/corr%20heatmap%20for%20cali.png)

**Key insights**
 - **R&D Spend and Profit**: Strong correlation of 0.98, indicating once again that high R&D investment directly correlates to higher profits. Investing in innovation is a must in California.

 - **Marketing Spend and Profit**: Robust correlation of 0.79. Effective marketing strategies are pivotal here, though slightly less impactful than R&D.

 - **Administration and Profit**: Low correlation of 0.16. Administrative costs don't have much of an impact on profitability, similar to what we saw in New York.

 - **R&D and Marketing Spend**: Strong correlation of 0.74 between these. Companies that invest heavily in R&D also tend to allocate significant resources to marketing, aiming to leverage their innovations effectively.

These insights highlight the importance of balanced investment between R&D and marketing to drive profitability in California.


![corrheatmap](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/92e39a7dabf282c997f852345abcbeb5ec708e26/corr%20heatmap%20for%20florida.png)

**Key insights**
 - **R&D Spend and Profit**: A very high correlation of 0.97. Like in other states, R&D investment significantly drives profitability. This emphasizes the importance of innovation.

 - **Marketing Spend and Profit**: Moderate correlation of 0.57. While marketing spend has a notable impact, it’s not as strong as R&D. Effective marketing still plays a crucial role, though.

 - **Administration and Profit**: A weak negative correlation of -0.04. Administrative spending doesn't seem to contribute much to profitability and may sometimes slightly detract.

 - **R&D and Marketing Spend**: Positive correlation of 0.55. Companies that invest in R&D also tend to spend on marketing, though not as strongly correlated as in other states.

 - **Administration and Marketing Spend**: A negative correlation of -0.35. Companies that spend more on administration might be spending less on marketing, possibly hinting at different strategic priorities.

Florida's profitability also leans heavily on R&D with significant support from marketing investments. Quite the balanced yet innovation-focused approach.


![regplot](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/92e39a7dabf282c997f852345abcbeb5ec708e26/regplot%20for%20NY.png)

**Key insights**
Our regression plots paint a more vivid picture:

**R&D Spend vs Profit**:

 - Clear, strong positive relationship. The more you invest in R&D, the higher the profit margin.

**Administration Spend vs Profit**:

 - Mild positive trend. Administration spend does contribute to profit, but not as decisively.

**Marketing Spend vs Profit**:

 - Strong positive correlation. Effective marketing strategies significantly boost profits.

New York startups should definitely keep ramping up R&D and marketing investments to maximize their profits.


![regplot](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/92e39a7dabf282c997f852345abcbeb5ec708e26/regplot%20for%20cali.png)

**Key insights**
**R&D Spend vs Profit**:

 - A strong positive relationship. More R&D spend means higher profit, clear as day.

**Administration Spend vs Profit**:

 - Mild positive trend. Admin costs do contribute, but they’re not the big driver.

**Marketing Spend vs Profit**:

 - Solid positive correlation. Marketing dollars are making a significant impact on profits.

Turns out that in California, just like in New York, R&D and marketing are where the money’s at for maximizing profit


![regplot](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/92e39a7dabf282c997f852345abcbeb5ec708e26/regplot%20for%20florida.png)

**Key insights**
**R&D Spend vs Profit**:

 - Very strong positive correlation. The more you invest in R&D, the better the returns. Consistent with other states, but particularly pronounced here.

**Administration Spend vs Profit**:

 - No significant relationship. Administrative costs seem to have little to no direct impact on profitability, reinforcing previous observations.

**Marketing Spend vs Profit**:

 - Strong positive correlation. Effective marketing leads to higher profits. A significant factor but not as strong as R&D investment.

Our visualizations reinforce that strategic investments in R&D and marketing are key drivers of profitability across these states.

 ---

## Investment Strategies Based on Analysis

**Overview**: 

Our analysis of 50 startup companies across New York, California, and Florida reveals the following key insights:

 - Strong positive correlation between R&D spending and profitability.

 - Notable positive correlation between marketing spending and profitability.

 - Minimal impact of administrative spending on profitability.


**State-Specific Insights and Strategies**

**New York**:

 - **R&D Investment**: Highest correlation with profit. Significant budget should be allocated towards R&D to drive innovation and competitive advantage.

 - **Marketing Spend**: Effective marketing strategies are crucial. A robust marketing plan to promote products/services must be put in place.

 - **Administration Costs**: While necessary, they have less direct impact on profit. Optimizing these costs to free up resources for R&D and marketing should be focused on.


**California**:

 - **R&D Investment**: Just like New York, prioritize R&D spending to leverage the strong positive correlation with profit.

 - **Marketing Spend**: Strategic marketing is vital. Tailor marketing efforts to target demographics effectively.

 - **Administration Costs**: Less impactful on profitability. Streamline administrative processes to improve efficiency without overburdening the budget.


**Florida**:

 - **R&D Investment**: Essential for driving profits. Continue to invest heavily in R&D.

 - **Marketing Spend**: Strong impact on profitability. Maintain or increase marketing budgets to capitalize on this trend.

 - **Administration Costs**: Minimal impact on profits. Optimize administrative spending to support other critical areas.

## General Recommendations:
**Balance Investment in R&D and Marketing**:

 - R&D drives innovation, leading to product/service enhancements and new offerings.

 - Marketing ensures that these innovations reach the target audience effectively, boosting sales and market presence.


**Optimize Administrative Spending**:

 - Focus on efficiency in administrative functions to reduce costs without compromising operations.

 - Reallocate savings towards R&D and marketing for higher returns.


**Tailor Strategies by State**:

 - Recognize the unique business environments and market conditions in each state.

 - Adapt investment strategies to suit the specific needs and opportunities in New York, California, and Florida.


**Actionable Steps**:
**Conduct Regular Performance Reviews**:

- Evaluate the effectiveness of R&D and marketing investments quarterly.

- Adjust budgets based on performance metrics and market changes.


**Innovate and Adapt**:

 - Stay ahead of industry trends by continuously innovating through R&D.

 - Adapt marketing strategies to leverage new platforms and technologies.

 ---

## Data Preprocessing

1. **State Encoding**: Mapped categorical values to numerical format for the `State` column.
2. **Feature Scaling**: Standardized spending columns to ensure uniform influence on model training.

## Model Building

- **Algorithm**: Linear Regression
- **Libraries**: Scikit-Learn for model training, pickle for saving the model.
- **Steps**:
    - Split the data into training and testing sets.
    - Train the model on the training set.
    - Evaluate performance using the test set.

## Model Evaluation

The model achieved satisfactory results with a focus on:

- **Interpretability**: Linear regression offers insights into feature importance.
- **Accuracy**: High R-squared value indicated a strong fit for predicting profit.

## Deployment

The model was deployed using **Streamlit** with a user-friendly interface:

1. **Input Fields**: For R&D, Administration, and Marketing spend, plus state selection.
2. **Prediction**: Displays profit prediction based on user inputs.
3. **Styling**: Applied custom CSS for a refined interface.

 ---

### Running the Application

To run the app locally:

```bash
streamlit run app.py
```

---

## Conclusion

This project provides valuable insights into the relationship between startup spending and profit, offering predictions that can assist in investment decisions. The model indicates R&D spending is a critical factor, with a higher impact on profitability compared to other areas. This interactive application serves as a practical tool for potential startups and investors.

```
