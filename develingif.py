import time
import praw
r = praw.Reddit('James Develin Beast Run Auto-Gif by /u/MoistNate')
r.login('ObligatoryDevelinGif','allielynn')
already_done = []
jd_words = ['develin']

while True:
    subreddit = r.get_subreddit('patriots')
    for submission in subreddit.get_new(limits=10):
        op_text = submission.title.lower()
        has_jd = any(string in op_text for string in jd_words)

        if submission.id not in already_done and has_jd:
            submission.add_comment('[ObligatoryDevelinGif](http://a.video.nfl.com/films/s2013/nflcom/w13/131201_phl_wk_13_bp_ne_james_develin_1_yd_td_3200k.mp4)')
            already_done.append(submission.id)
    
