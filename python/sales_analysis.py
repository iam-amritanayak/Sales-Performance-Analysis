df = df[
    df["ItemName"].notna() &
    df["RestaurantName"].notna() &
    df["Category"].notna() &
    df["KOTDate"].notna()
]
df["Rate"] = pd.to_numeric(df["Rate"], errors="coerce")
df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")
df["TotalAmount"] = pd.to_numeric(df["TotalAmount"], errors="coerce")
df["KOTDate"] = pd.to_datetime(df["KOTDate"], errors="coerce")
df["ItemName"] = df["ItemName"].str.strip()
df["RestaurantName"] = df["RestaurantName"].str.strip()
df["Category"] = df["Category"].str.strip()
df["Qty"].sum()
df["TotalAmount"].sum()
df.to_excel("Sales_Dashboard_Cleaned.xlsx", index=False)
