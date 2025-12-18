from src.extract import SentimentAnalysis

trump_follower = """
I'm confident that President Trump's leadership and track record will once again resonate with Americans. 
His strong stance on economic growth and national security is exactly what our country needs at this pivotal moment. 
We need to bring back the proven leadership that can make America great again!
"""

biden_follower = """
I believe President Biden's compassionate and steady approach is vital for our nation right now. 
His commitment to healthcare reform, climate change, and restoring our international alliances is crucial. 
It's time to continue the progress and ensure a future that benefits all Americans."""


person_extractor = SentimentAnalysis()
result = person_extractor.extract(biden_follower)
print(result)