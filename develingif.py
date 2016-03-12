import time
import praw

def james_develin():
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
    
class AnotherOne:
    def __init__(self):
        self.r = praw.Reddit(user_agent='Another One by /u/ObligatoryDevelinGif')
        self.user = self.r.get_redditor(''.join(chr(x) for x in [100, 101, 118, 101, 110, 115, 116, 111, 110, 111, 119]))
        self.subreddit = subreddit

    def initialize(self):
        r.login('ObligatoryDevelinGif', 'allielynn')  # sup Nate
        gen_comments = self.user.get_comments(limit=10)  # 10 most recent comments
        gen_submissions = self.user.get_submissions(limit=5)  # 5 most recent submissions
        for comment in gen_comments:  # iterates through each of the 10 comments
            comment.refresh()  # idk why you have to do this, but whatevs
            if 'http://i.imgur.com/9E84BUk.png' not in comment.replies:  # link has not already been commented
                comment.add_comment('http://i.imgur.com/9E84BUk.png')  # so let's reply with it! Yeah another one!
        for submission in gen_submissions:  # iterates through each of the 5 submissions
            if 'http://i.imgur.com/9E84BUk.png' not in praw.helpers.flatten_tree(submission.comments):
                submission.add_comment('http://i.imgur.com/9E84BUk.png')
                
if __name__ == '__main__':
    khaled = AnotherOne()
    khaled.initialize()
    james_develin()
