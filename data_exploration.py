import kaggle
import pandas as pd


kaggle.api.authenticate()
kaggle.api.dataset_download_file(
        dataset = "nguyenletruongthien/mental-health",
        file_name = "conversations_training.csv",
        path = ".",
        force = True    
)

csv_df = pd.read_csv("conversations_training.csv")
print(csv_df.shape)
print(csv_df.head(2))
print(csv_df.isnull().values.any())





import pdfplumber

text = ""
with pdfplumber.open("MentalHealthAtlas.pdf") as pdf:
    for page in pdf.pages:
        text += (page.extract_text() or "")


print("num of chars:", len(text))

pdf_df = pd.DataFrame({'text': [text], 'source': 'who_pdf'})





import requests
import bs4
#most forum  will block direct Python Request / scraping

#instead, I just found a dataset containing posts from online mental health forums and blogs 

df_blog = pd.read_csv("mental_health_blog_dataset.csv")
df_blog = df_blog[['title', 'post', 'category']].dropna() 
print(df_blog.shape)
print(df_blog.head(2))




dataset = {
    "Mental Health Counseling Converstion": csv_df,
    "WHO Publicaiton": pdf_df,
    "Mental Health blog": df_blog
}