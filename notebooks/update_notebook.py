import nbformat
from nbformat.v4 import new_markdown_cell

nb_path = r'e:\trader-sentiment-analysis\notebooks\01_data_analysis.ipynb'
nb = nbformat.read(nb_path, as_version=4)

new_cells = []

# Section 1
new_cells.append(new_markdown_cell('# Market Sentiment vs. Trader Performance Analysis\n## 1. Data Loading\nFirst, we import the necessary libraries and load our raw sentiment and trading transaction data.'))

# Add existing imports
new_cells.append(nb.cells[3]) 

# Add markdown
new_cells.append(new_markdown_cell('## 2. Data Understanding\nIn this section, we inspect the shape, types, and summary statistics of our raw datasets.'))
for i in range(4, 15):
    new_cells.append(nb.cells[i])

new_cells.append(new_markdown_cell('## 3. Data Cleaning\nRaw data often contains missing values, inconsistent datetime formats, and miscellaneous anomalies. \n**Why we do this**: To ensure our aggregations are accurate, we must standardize date formats and handle null entities that might skew the calculations.'))

for i in range(15, 27):
    new_cells.append(nb.cells[i])

new_cells.append(new_markdown_cell('## 4. Feature Engineering: Behavioral Metrics\nTo understand *how* sentiment impacts trading, we must aggregate individual transactions into daily user profiles.'))

for i in range(27, 39):
    new_cells.append(nb.cells[i])

new_cells.append(new_markdown_cell('## 5. Aggregated Analysis & Summaries\nWith our features engineered, we compare averages across the different sentiment regimes.'))

for i in range(39, 44):
    new_cells.append(nb.cells[i])

new_cells.append(new_markdown_cell('## 6. Visualizations & Insights\nWe now visualize the generated features to uncover actionable behavioral trends.'))

# Combine visualizations with insights
idx = 44
metrics = ['Average Daily PnL', 'Win Rate Distribution', 'Trade Frequency', 'Average Trade Size', 'Long vs Short Bias']
for m in metrics:
    if idx < len(nb.cells) - 6:
        new_cells.append(nb.cells[idx])
        new_cells.append(new_markdown_cell(f'### ?? Insight: {m}\n* Analyzing {m} provides insights into trader behavior across varying market sentiments.'))
        idx += 1

# Remaining cells
while idx < len(nb.cells):
    new_cells.append(nb.cells[idx])
    idx += 1

nb.cells = new_cells
nbformat.write(nb, nb_path)
print('Notebook updated!')
