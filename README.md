# Cronos-Sentiment

Repository for our automated process of our internship assignment of Epic Data. <br>
Link to our full project: [Cronos Sentiment Analysis](https://github.com/davidwong19/cronos-sentiment-analyse.git)

## Short Introduction
1. **Scrapers**: This folder contains the scrapers for the 3 languages on GlassDoor.
2. **Scrapers**: This folder contains extra data needed for our dashboard.
3. **img**: This folder contains images needed for our dashboard and for our README.md.
4. **check_dup.py**: This python script will check for duplicates, after running above script.
5. **requirements.txt**: A text file containing the required packages for running both scripts, needed for running our workflow.
6. **cronos_reviews.csv**: Our csv file containing all our gathered reviews, from different sources.

## Usage
This is an repository with an GitHub Workflow, accesible via the **Actions** tab.
The workflow is called **'Update data'**, this workflow will check for new reviews **every sunday at 00:00**.
This can be changed, by changing the cron schedule expression, in the `main.yml`. This is located in this repository at **/.github/workflows/main.yml**.
Below you can find a handy tool, to get the correct cron schedule expression.
[CRONTAB](https://crontab.guru/#0_0_*_*_0)

### Running the workflow manually
1. Go to [Actions](https://github.com/Rehtsecp/Cronos-Sentiment/actions/workflows/main.yml)
2. Click on **Run workflow**
![Run Workflow 1](img/workflow1.png)
3. Click on **Run workflow**, once more
![Run Workflow 2](img/workflow2.png)
4. After waiting a couple seconds, you'll see an orange loading icon, that means the process is starting
![Start Workflow](img/w3.png)
Wait a max. of 1 minute to allow it to complete the whole process of scraping, assigning score/sentiment and to update the CSV file.
![Complete](img/w4.png)

Now you should be able to find the new reviews in **cronos_reviews.csv**.

### EXTRA
If you want to check if the script found new reviews and/or if there were any duplicates found. 

1. Click on **Update data**
![Extra 1](img/extra1.png)

2. Click on **execute**
![Extra 2](img/extra2.png)

3. Click on **Check duplicates**
![Extra 3](img/x3.png)
Here you'll see how many duplicates and new reviews were found.
