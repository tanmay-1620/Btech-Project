import pandas as pd
# Load one of the CSV files in a subfolder (adjust the path)
df_disaster1 = pd.read_csv('D:/BTP/Data/Raw/crisis_text/CrisisLexT26-v1.0/CrisisLexT26/2012_Colorado_wildfires/2012_Colorado_wildfires-tweets_labeled.csv')
print(df_disaster1.head())
print(df_disaster1.columns)
# Encoding informativeness and information_type
df_disaster1['informativeness_encoded'], _ = pd.factorize(df_disaster1[' Informativeness'])
df_disaster1['information_type_encoded'], _ = pd.factorize(df_disaster1[' Information Type'])
# Save cleaned dataset to a new CSV file
df_disaster1.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster1.csv.txt', index=False)
df_disaster2 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Costa_Rica_earthquake\2012_Costa_Rica_earthquake-tweets_labeled.csv')
print(df_disaster2.head())
df_disaster2['informativeness_encoded'], _ = pd.factorize(df_disaster2[' Informativeness'])
df_disaster2['information_type_encoded'], _ = pd.factorize(df_disaster2[' Information Type'])
df_disaster2.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster2.csv.txt', index=False)
df_disaster3 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Guatemala_earthquake\2012_Guatemala_earthquake-tweets_labeled.csv')
print(df_disaster3.head())
df_disaster3['informativeness_encoded'], _ = pd.factorize(df_disaster3[' Informativeness'])
df_disaster3['information_type_encoded'], _ = pd.factorize(df_disaster3[' Information Type'])
df_disaster3.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster3.csv.txt', index=False)
df_disaster4 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Italy_earthquakes\2012_Italy_earthquakes-tweets_labeled.csv')
print(df_disaster4.head())
df_disaster4['informativeness_encoded'], _ = pd.factorize(df_disaster4[' Informativeness'])
df_disaster4['information_type_encoded'], _ = pd.factorize(df_disaster4[' Information Type'])
df_disaster4.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster4.csv.txt', index=False)
df_disaster5 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Philipinnes_floods\2012_Philipinnes_floods-tweets_labeled.csv')
print(df_disaster5.head())
df_disaster5['informativeness_encoded'], _ = pd.factorize(df_disaster5[' Informativeness'])
df_disaster5['information_type_encoded'], _ = pd.factorize(df_disaster5[' Information Type'])
df_disaster5.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster5.csv.txt', index=False)
df_disaster6 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Typhoon_Pablo\2012_Typhoon_Pablo-tweets_labeled.csv')
print(df_disaster6.head())
df_disaster6['informativeness_encoded'], _ = pd.factorize(df_disaster6[' Informativeness'])
df_disaster6['information_type_encoded'], _ = pd.factorize(df_disaster6[' Information Type'])
df_disaster6.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster6.csv.txt', index=False)
df_disaster7 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Venezuela_refinery\2012_Venezuela_refinery-tweets_labeled.csv')
print(df_disaster7.head())
df_disaster7['informativeness_encoded'], _ = pd.factorize(df_disaster7[' Informativeness'])
df_disaster7['information_type_encoded'], _ = pd.factorize(df_disaster7[' Information Type'])
df_disaster7.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster7.csv.txt', index=False)
df_disaster8 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Alberta_floods\2013_Alberta_floods-tweets_labeled.csv')
print(df_disaster8.head())
df_disaster8['informativeness_encoded'], _ = pd.factorize(df_disaster8[' Informativeness'])
df_disaster8['information_type_encoded'], _ = pd.factorize(df_disaster8[' Information Type'])
df_disaster8.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster8.csv.txt', index=False)
df_disaster9 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Australia_bushfire\2013_Australia_bushfire-tweets_labeled.csv')
print(df_disaster9.head())
df_disaster9['informativeness_encoded'], _ = pd.factorize(df_disaster9[' Informativeness'])
df_disaster9['information_type_encoded'], _ = pd.factorize(df_disaster9[' Information Type'])
df_disaster9.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster9.csv.txt', index=False)
df_disaster10 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Bohol_earthquake\2013_Bohol_earthquake-tweets_labeled.csv')
print(df_disaster10.head())
df_disaster10['informativeness_encoded'], _ = pd.factorize(df_disaster10[' Informativeness'])
df_disaster10['information_type_encoded'], _ = pd.factorize(df_disaster10[' Information Type'])
df_disaster10.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster10.csv.txt', index=False)
df_disaster11 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Boston_bombings\2013_Boston_bombings-tweets_labeled.csv')
print(df_disaster11.head())
df_disaster11['informativeness_encoded'], _ = pd.factorize(df_disaster11[' Informativeness'])
df_disaster11['information_type_encoded'], _ = pd.factorize(df_disaster11[' Information Type'])
df_disaster11.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster11.csv.txt', index=False)
df_disaster12 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Brazil_nightclub_fire\2013_Brazil_nightclub_fire-tweets_labeled.csv')
print(df_disaster12.head())
df_disaster12['informativeness_encoded'], _ = pd.factorize(df_disaster12[' Informativeness'])
df_disaster12['information_type_encoded'], _ = pd.factorize(df_disaster12[' Information Type'])
df_disaster12.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster12.csv.txt', index=False)
df_disaster13 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Colorado_floods\2013_Colorado_floods-tweets_labeled.csv')
print(df_disaster13.head())
df_disaster13['informativeness_encoded'], _ = pd.factorize(df_disaster13[' Informativeness'])
df_disaster13['information_type_encoded'], _ = pd.factorize(df_disaster13[' Information Type'])
df_disaster13.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster13.csv.txt', index=False)
df_disaster14 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Glasgow_helicopter_crash\2013_Glasgow_helicopter_crash-tweets_labeled.csv')
print(df_disaster14.head())
df_disaster14['informativeness_encoded'], _ = pd.factorize(df_disaster14[' Informativeness'])
df_disaster14['information_type_encoded'], _ = pd.factorize(df_disaster14[' Information Type'])
df_disaster14.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster14.csv.txt', index=False)
df_disaster15 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_LA_airport_shootings\2013_LA_airport_shootings-tweets_labeled.csv')
print(df_disaster15.head())
df_disaster15['informativeness_encoded'], _ = pd.factorize(df_disaster15[' Informativeness'])
df_disaster15['information_type_encoded'], _ = pd.factorize(df_disaster15[' Information Type'])
df_disaster15.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster15.csv.txt', index=False)
df_disaster16 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Lac_Megantic_train_crash\2013_Lac_Megantic_train_crash-tweets_labeled.csv')
print(df_disaster16.head())
df_disaster16['informativeness_encoded'], _ = pd.factorize(df_disaster16[' Informativeness'])
df_disaster16['information_type_encoded'], _ = pd.factorize(df_disaster16[' Information Type'])
df_disaster16.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster16.csv.txt', index=False)
df_disaster17 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Manila_floods\2013_Manila_floods-tweets_labeled.csv')
print(df_disaster17.head())
df_disaster17['informativeness_encoded'], _ = pd.factorize(df_disaster17[' Informativeness'])
df_disaster17['information_type_encoded'], _ = pd.factorize(df_disaster17[' Information Type'])
df_disaster17.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster17.csv.txt', index=False)
df_disaster18 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_NY_train_crash\2013_NY_train_crash-tweets_labeled.csv')
print(df_disaster18.head())
df_disaster18['informativeness_encoded'], _ = pd.factorize(df_disaster18[' Informativeness'])
df_disaster18['information_type_encoded'], _ = pd.factorize(df_disaster18[' Information Type'])
df_disaster18.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster18.csv.txt', index=False)
df_disaster19 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Queensland_floods\2013_Queensland_floods-tweets_labeled.csv')
print(df_disaster19.head())
df_disaster19['informativeness_encoded'], _ = pd.factorize(df_disaster19[' Informativeness'])
df_disaster19['information_type_encoded'], _ = pd.factorize(df_disaster19[' Information Type'])
df_disaster19.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster19.csv.txt', index=False)
df_disaster20 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Russia_meteor\2013_Russia_meteor-tweets_labeled.csv')
print(df_disaster20.head())
df_disaster20['informativeness_encoded'], _ = pd.factorize(df_disaster20[' Informativeness'])
df_disaster20['information_type_encoded'], _ = pd.factorize(df_disaster20[' Information Type'])
df_disaster20.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster20.csv.txt', index=False)
df_disaster21 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Sardinia_floods\2013_Sardinia_floods-tweets_labeled.csv')
print(df_disaster21.head())
df_disaster21['informativeness_encoded'], _ = pd.factorize(df_disaster21[' Informativeness'])
df_disaster21['information_type_encoded'], _ = pd.factorize(df_disaster21[' Information Type'])
df_disaster21.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster21.csv.txt', index=False)
df_disaster22 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Savar_building_collapse\2013_Savar_building_collapse-tweets_labeled.csv')
print(df_disaster22.head())
df_disaster22['informativeness_encoded'], _ = pd.factorize(df_disaster22[' Informativeness'])
df_disaster22['information_type_encoded'], _ = pd.factorize(df_disaster22[' Information Type'])
df_disaster22.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster22.csv.txt', index=False)
df_disaster23 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Singapore_haze\2013_Singapore_haze-tweets_labeled.csv')
print(df_disaster23.head())
df_disaster23['informativeness_encoded'], _ = pd.factorize(df_disaster23[' Informativeness'])
df_disaster23['information_type_encoded'], _ = pd.factorize(df_disaster23[' Information Type'])
df_disaster23.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster23.csv.txt', index=False)
df_disaster24 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Spain_train_crash\2013_Spain_train_crash-tweets_labeled.csv')
print(df_disaster24.head())
df_disaster24['informativeness_encoded'], _ = pd.factorize(df_disaster24[' Informativeness'])
df_disaster24['information_type_encoded'], _ = pd.factorize(df_disaster24[' Information Type'])
df_disaster24.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster24.csv.txt', index=False)
df_disaster25 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Typhoon_Yolanda\2013_Typhoon_Yolanda-tweets_labeled.csv')
print(df_disaster25.head())
df_disaster25['informativeness_encoded'], _ = pd.factorize(df_disaster25[' Informativeness'])
df_disaster25['information_type_encoded'], _ = pd.factorize(df_disaster25[' Information Type'])
df_disaster25.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster25.csv.txt', index=False)
df_disaster26 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_West_Texas_explosion\2013_West_Texas_explosion-tweets_labeled.csv')
print(df_disaster26.head())
df_disaster26['informativeness_encoded'], _ = pd.factorize(df_disaster26[' Informativeness'])
df_disaster26['information_type_encoded'], _ = pd.factorize(df_disaster26[' Information Type'])
df_disaster26.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster26.csv.txt', index=False)
# df_disaster27 = pd.read_csv(r'D:\BTP\Data\Raw\crisis_text\Disaster Response messages\disaster_messages.csv')
# print(df_disaster27.head())
# df_disaster27.to_csv(r'D:\BTP\Data\processed\crisislex26\crisis_text_cleaned_disaster27.csv.txt', index=False)
import pandas as pd
import os
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download necessary NLTK data (only needs to be done once)
nltk.download('stopwords')
nltk.download('punkt')

# Define the text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)  # Remove punctuation and special chars
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

# List of all file paths
file_paths = [
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Colorado_wildfires\2012_Colorado_wildfires-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Costa_Rica_earthquake\2012_Costa_Rica_earthquake-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Guatemala_earthquake\2012_Guatemala_earthquake-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Italy_earthquakes\2012_Italy_earthquakes-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Philipinnes_floods\2012_Philipinnes_floods-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Typhoon_Pablo\2012_Typhoon_Pablo-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Venezuela_refinery\2012_Venezuela_refinery-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Alberta_floods\2013_Alberta_floods-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Australia_bushfire\2013_Australia_bushfire-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Bohol_earthquake\2013_Bohol_earthquake-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Boston_bombings\2013_Boston_bombings-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Brazil_nightclub_fire\2013_Brazil_nightclub_fire-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Colorado_floods\2013_Colorado_floods-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Glasgow_helicopter_crash\2013_Glasgow_helicopter_crash-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_LA_airport_shootings\2013_LA_airport_shootings-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Lac_Megantic_train_crash\2013_Lac_Megantic_train_crash-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Manila_floods\2013_Manila_floods-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_NY_train_crash\2013_NY_train_crash-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Queensland_floods\2013_Queensland_floods-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Sardinia_floods\2013_Sardinia_floods-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Savar_building_collapse\2013_Savar_building_collapse-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Singapore_haze\2013_Singapore_haze-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Spain_train_crash\2013_Spain_train_crash-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_Typhoon_Yolanda\2013_Typhoon_Yolanda-tweets_labeled.csv',
    r'D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2013_West_Texas_explosion\2013_West_Texas_explosion-tweets_labeled.csv'
]

for file_path in file_paths:
    # Print the path for debugging
    print(f"Processing file: {file_path}")
    
    try:
        # Load the CSV file
        df = pd.read_csv(file_path)
        
        # Check if 'Tweet Text' column exists
        if ' Tweet Text' in df.columns:
            # Apply cleaning to create 'cleaned_text' column
            df['cleaned_text'] = df[' Tweet Text'].apply(clean_text)
        else:
            print(f"Error: 'Tweet Text' column missing in {file_path}")
            continue
        

        # Encode informativeness and information type
        df['informativeness_encoded'], _ = pd.factorize(df[' Informativeness'])
        df['information_type_encoded'], _ = pd.factorize(df[' Information Type'])
        
        # Define the output path
        output_path = "D:\BTP\Data\Raw\crisis_text\CrisisLexT26-v1.0\CrisisLexT26\2012_Colorado_wildfires\2012_Colorado_wildfires-tweets_labeled.csv".replace("Raw", "processed/crisislex26").replace(".csv", "_cleaned.csv")

        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save the processed DataFrame
        df.to_csv(output_path, index=False)
        print(f"Processed and saved: {output_path}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

        
