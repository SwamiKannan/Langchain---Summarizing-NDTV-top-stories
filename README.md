# Summarizing NDTV's latest stories using LangChain and OpenAI

<p align="center">
  <img src="https://github.com/SwamiKannan/Langchain---Summarizing-NDTV-top-stories/blob/main/cover.png">
  <br><i>The unofficial NDTV news summarizer</i>
</p>

## Description:
This repo seeks to scrape the latest news from the NDTV website (ndtv.com/latest) and provide summaries for the readers of the latest headlines in those areas. This repo
covers:
<ol>
  <li> <a href="ndtv.com">the main NDTV website</a></li>
  <li> <a href="Gadgets360.com">Gadgets 360</a></li>
  <li> <a href="food.ndtv.com">NDTV food</a></li>
  <li> <a href="doctor.ndtv.com">Doctor NDTV</a></li>
</ol>

## Requirements:
1. You will need Python and pip installed to install the required libraries
2. You will also need to register an OpenAI account and obtain an API key. If you don't have one, find how to <a href="https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/">here</a>
## Execute:
### Install:
1. Download the repo
2. Navigate into the main folder and run:<br>
   `pip install -r`
### Scrape:
4. Go to the src folder and run the following commands one after another:
5. Run the news extraction script using the following code
   ```
   python "ndtv_class.py"
   ndtv_content = ndtv_test.run_extraction()
   hl, summ, art, urls = ndtv_content
   ```
6. Summarize each article and all the articles by running the following code:
   ```
   python summarizer.py
   ```
7. Create the newspaper by running:
   ```
   python create_newspaper.py"
   ```
