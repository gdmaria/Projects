# Summary
This project is a simple web service for calculating similarity of two texts.

# Metric used
**Cosine Similarity**  
Source: https://towardsdatascience.com/overview-of-text-similarity-metrics-3397c4601f50

## Prerequisites
**flask** microframework

**Installation instructions**:  
Within the activated environment, use the following command to install Flask:  
$ pip install Flask

## Project Files
1. **text_similarity_web_service.py**  
   Python script containing code for the web service.
2. **text_similarity.py**  
   Module containing functions for calculating similarity of two texts.

## Usage and testing options
1. Testing **text_similarity.py** module (flask not required).  
   Run **text_similarity.py**.  
   Sample texts and test function calls are specified in the main section.  
   
2. Testing the web service (flask required).
* Run **text_similarity_web_service.py**
* In Postman (or a similar API client) send a POST request to **http://0.0.0.0:5000/text_similarity/api**  
  **Parameters**: ?text1=<text 1>&text2=<text 2>  
  **Sample request**:  
  http://0.0.0.0:5000/text_similarity/api?text1=The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.&text2=The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you.
