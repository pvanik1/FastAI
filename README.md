# FastAI
Homeworks and experiments from the Fast.ai (2019) course by Jeremy Howard

Practice Apparel problem notes:
- normalising the images by defaults according to imagenet worsened accuracy
- applying default transforms worsened accuracy as well as training time because the transforms were not relevant to the image set. Even resnet50 had faster training time
- Leaderboard: #50 (11/3/2019) with accuracy 91.1% accuracy https://datahack.analyticsvidhya.com/contest/practice-problem-identify-the-apparels/lb
