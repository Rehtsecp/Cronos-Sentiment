# Import necessary packages
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from googletrans import Translator
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

sia = SentimentIntensityAnalyzer()

df = pd.read_csv("final_reviews.csv")
id = df["id"].iloc[-1]

# Function for extracting the page
def extract():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
    }  # For additional information with request
    # List of URL's with Cronos Review page on Glassdoor, it contains a link to the FR, NL & EN version of the page.
    # url = f"hhttps://nl.glassdoor.be/Reviews/Cronos-Reviews-E871033.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=nld"
    # url = f"https://www.glassdoor.co.uk/Reviews/Cronos-Reviews-E871033.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng"
    url = f"https://fr.glassdoor.be/Reviews/Cronos-Reviews-E871033.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=fra"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

 
# Function for transforming the page content to a dictionary
def transform(soup):
    # Div with all the reviews inside
    divs = soup.find_all("div", class_="gdReview")

    # Going over each review in the div
    for item in divs:
        rating = item.find(
            "span", class_="ratingNumber mr-xsm"
        ).text.strip()  # Get Rating
        author_info = item.find(
            "span", class_="authorJobTitle"
        ).text.strip()  # Get AuthorInfo

        index = author_info.find(" -")  # Get index of '-'
        date = author_info[:index]  # Get the date from 0 index
        date_clean = datetime.strptime(
            date, "%b %d, %Y"
        ).date()  # Convert date to datetime object, %Y %m %d
        date_clean_str = date_clean.strftime(
            "%d/%m/%Y"
        )  # Convert datetime to str with format of dd/mm/yyyy

        pros = (
            item.find("span", {"data-test": "pros"}).text.strip().replace("\r\n", "")
        )  # Get pros
        cons = (
            item.find("span", {"data-test": "cons"}).text.strip().replace("\r\n", "")
        )  # Get cons
        opinion = pros + ", " + cons  # Combining pros and cons in one opinion string

        # This piece of code will translate the opinion in whatever language to EN
        translator = Translator()
        opinion_tr = translator.translate(opinion).text  # Get only the translated text

        new_id = int(id) + 1  # Assigning an id

        # Giving the opinion an compound score and sentiment
        score = sia.polarity_scores(opinion_tr)["compound"]
        if score >= 0.05:
            sentiment = "positive"
        elif score <= -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        # Putting it in a dictionary
        review = {
            "\n" "id": new_id,
            "company": "TEST",
            "opinion": opinion_tr,
            "date": date_clean_str,
            "rating": rating,
            "source": "glassdoor",
            "score": score,
            "sentiment": sentiment,
        }
        reviewlist.append(review)
    return


reviewlist = []


c = extract()
transform(c)

# Writing to a CSV
df = pd.DataFrame(reviewlist)  # List to pandas dataframe
print(df.head())  # Printing the first few entries of the pandas dataframe, to check
df.to_csv("final_reviews.csv", index=False, mode="a", header=False)  # Converting pandas dataframe to a CSV file
