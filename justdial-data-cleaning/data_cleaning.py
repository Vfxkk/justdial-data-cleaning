import pandas as pd

# Load the data
df = pd.read_csv("justdial.csv")

# Drop unwanted column: plus icon
df.drop(columns=["jsx-4e78e4eb4856e501"], inplace=True)

# Rename columns (you can customize these)
df.columns = [
    'link', 'rating_icon', 'rating', 'rating_count', 'company_name',
    'rating_value', 'review_text', 'address', 'tagline',
    'category', 'phone_number', 'contact_option', 'cta_text'
]

# Drop rows with no company name
df.dropna(subset=["company_name"], inplace=True)

# Export cleaned data
df.to_csv("justdial_cleaned.csv", index=False)

print("✅ Data cleaning complete. File saved as justdial_cleaned.csv")
