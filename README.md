# Summarizing NDTV's latest stories using LangChain and OpenAI

<p align="center">
  <img src="https://github.com/SwamiKannan/Langchain---Summarizing-NDTV-top-stories/blob/main/cover.png">
  <br><i>The unofficial NDTV news summarizer</i>
</p>

## Description:
This repo seeks to scrape the latest news from the NDTV website (ndtv.com/latest) and provide summaries for the readers of the latest headlines in those areas. This repo
covers:
<ol>
  <li> <a href="ndtv.com">The main NDTV website</a></li>
  <li> <a href="Gadgets360.com">Gadgets 360</a></li>
  <li> <a href="food.ndtv.com">NDTV food</a></li>
  <li> <a href="doctor.ndtv.com">Doctor NDTV</a></li>
</ol>

## Requirements:
1. You will need Python and pip installed to install the required libraries
2. You will also need to register an OpenAI account and obtain an API key. If you don't have one, find how to <a href="https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/">here</a>
## Install:
1. Download the repo
2. Navigate into the main folder and run:<br>
   `pip install -r requirements.txt`

## Run code:
There are two ways to run the code:
### A. Simple Way: Run
`python main.py`
### B. Hands-on Way:
#### Scrape:
1. Go to the src folder and run the following commands one after another:
2. Run the news extraction script using the following code
   ```
   python "ndtv_class.py"
   ndtv_content = ndtv_test.run_extraction()
   hl, summ, art, urls = ndtv_content
   ```
#### Summarize:
3. Summarize each article and all the articles by running the following code:
   ```
   python summarizer.py
   ```
#### Generate web page:
4. Create the newspaper by running:
   ```
   python create_newspaper.py"
   ```
This should display a webpage that shows the following:
1. A bulleted summary of all articles
2. Summary of each article with the corresponding headline and url

<b> This repo has no affiliation whatsoever with NDTV. It is not officially sanctioned, nor is there any collaboration / partnership whatsoever. This is only a personal project </b>
