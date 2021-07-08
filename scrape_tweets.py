
# Using Python Wrapper

import snscrape.modules.twitter as sntwitter
import pandas as pd 

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:naval').get_items()):
    if i>1000:
        break
    if tweet.content[0] !="@":
        tweets_list1.append([tweet.date, tweet.content])
        # print(tweet.content[0])
    
## Creating a dataframe from the tweets list above 
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Text'])
# print(tweets_df1.loc[:, "Text"])

# tweets_df1.to_csv('Naval-tweets.csv')
print("\n---------------Task Completed-------------------")



# ## Scraping tweets from a text search query:
# for i,tweet in enumerate(sntwitter.TwitterSearchScraper('its the elephant since:2020-06-01 until:2020-07-31').get_items()):
#     if i>500:
#         break
#     tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
# # Creating a dataframe from the tweets list above
# tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])