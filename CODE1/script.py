# %%
import pandas as pd

# Load dataset
df = pd.read_csv(r"D:\FUTURE_DS_02\Code\Social_Media_Advertising.csv")

# Calculate KPIs
df["CTR (%)"] = (df["Clicks"] / df["Impressions"]) * 100
df["Engagement (%)"] = (df["Engagement_Score"] / df["Impressions"]) * 100
df["Performance_Score"] = (df["CTR (%)"] + df["Engagement (%)"] + df["ROI"]) / 3

# Save results
df.to_csv(r"D:\FUTURE_DS_02\Code\Social_Media_Advertising.csv", index=False)

print("KPI calculations added successfully! CSV saved.")




# %%
!pip install matplotlib
    


# %%


# %% [markdown]
# Initial Data Analysis
# 

# %%
import pandas as pd

# Load dataset
df = pd.read_csv("Social_Media_Advertising.csv")

# ----- IDA REPORT -----
print("===== SHAPE (Rows, Columns) =====")
print(df.shape)

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

print("\n===== UNIQUE VALUES OF CATEGORICAL COLUMNS =====")
for col in df.select_dtypes(include=['object']).columns:
    print(col, ":", df[col].nunique())


# %% [markdown]
# EDA

# %%
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Distribution of Impressions
sns.histplot(df["Impressions"], kde=True)
plt.title("Distribution of Impressions")
plt.show()

# 2. Conversion Rate Distribution
sns.histplot(df["Conversion_Rate"], kde=True)
plt.title("Distribution of Conversion Rate")
plt.show()

# 3. ROI Distribution
sns.histplot(df["ROI"], kde=True)
plt.title("Distribution of ROI")
plt.show()

# 4. Bar chart – Campaign Goals comparison
sns.barplot(x="Campaign_Goal", y="Conversion_Rate", data=df)
plt.title("Conversion Rate by Campaign Goal")
plt.show()

# 5. Engagement Score vs Conversion Scatter Plot
plt.scatter(df["Engagement_Score"], df["Conversion_Rate"])
plt.title("Engagement vs Conversion Rate")
plt.xlabel("Engagement Score")
plt.ylabel("Conversion Rate")
plt.show()



# %% [markdown]
# CDA

# %% [markdown]
# 1. Best Performing Target Audience

# %%
print("ROI by Target Audience")
print(df.groupby("Target_Audience")["ROI"].mean().sort_values(ascending=False))


# %% [markdown]
# 2. Performance by Channel

# %%
print("\nConversion Rate by Channel")
print(df.groupby("Channel_Used")["Conversion_Rate"].mean().sort_values(ascending=False))


# %% [markdown]
# 3. Engagement Score by Customer Segment

# %%
print("\nEngagement Score by Customer Segment")
print(df.groupby("Customer_Segment")["Engagement_Score"].mean().sort_values(ascending=False))



# %% [markdown]
# 4. ROI by Location

# %%
print("\nROI by Location")
print(df.groupby("Location")["ROI"].mean().sort_values(ascending=False))


# %% [markdown]
# 5. Top Companies by Performance Score

# %%
print("\nTop Companies by Performance Score")
print(df.groupby("Company")["Performance_Score"].mean().sort_values(ascending=False).head(10))


# %% [markdown]
# Visual CDA

# %%
sns.barplot(x="Channel_Used", y="ROI", data=df)
plt.title("ROI by Channel")
plt.show()

sns.barplot(x="Target_Audience", y="Conversion_Rate", data=df)
plt.title("Conversion Rate by Audience Group")
plt.show()


# %%
df.to_csv("Final_Social_Media_Campaign_Data.csv", index=False)
print("Final dataset ready for Power BI")



