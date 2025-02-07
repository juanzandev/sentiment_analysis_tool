from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")

text_neg= "I hate everything that's going on in the world, it sucks and I wish we could leave. It disgusts me!"
text = "We have no idea what we are doing, but we are trying to solve it. I think it is cool that we are putting a lot of effort into our future to make sure we have a happy a long life"
review_pps="I went and saw this movie last night after being coaxed to by a few friends of mine. I'll admit that I was reluctant to see it because from what I knew of Ashton Kutcher he was only able to do comedy. I was wrong. Kutcher played the character of Jake Fischer very well, and Kevin Costner played Ben Randall with such professionalism. The sign of a good movie is that it can toy with our emotions. This one did exactly that. The entire theater (which was sold out) was overcome by laughter during the first half of the movie, and were moved to tears during the second half. While exiting the theater I not only saw many women in tears, but many full grown men as well, trying desperately not to let anyone see them crying. This movie was great, and I suggest that you go see it before you judge."
review_neg = "Once again Mr. Costner has dragged out a movie for far longer than necessary. Aside from the terrific sea rescue sequences, of which there are very few I just did not care about any of the characters. Most of us have ghosts in the closet, and Costner's character are realized early on, and then forgotten until much later, by which time I did not care. The character we should really care about is a very cocky, overconfident Ashton Kutcher. The problem is he comes off as kid who thinks he's better than anyone else around him and shows no signs of a cluttered closet. His only obstacle appears to be winning over Costner. Finally when we are well past the half way point of this stinker, Costner tells us all about Kutcher's ghosts. We are told why Kutcher is driven to be the best with no prior inkling or foreshadowing. No magic here, it was all I could do to keep from turning it off an hour in."
analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)
scores1 = analyzer.polarity_scores(text_neg)
scores_3 = analyzer.polarity_scores(review_pps)
scores_4 = analyzer.polarity_scores(review_neg)
print(scores)
print(scores1)
print(scores_3)
print(scores_4)