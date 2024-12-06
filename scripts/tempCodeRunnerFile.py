  output_path = "D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Colorado_wildfires".replace("Raw", "processed/crisislex26").replace(".csv", "_cleaned.csv")
    df.to_csv(output_path, index=False)
    print(f"Processed and saved: {output_path}")