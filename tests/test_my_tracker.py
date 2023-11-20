from lib.my_tracker import *

def test_track_my_task():
    result = track_my_task("The previous chapter was completed. #TODO Complete exercise 1 with the challenges of a new chapter. #TODO  Few more drills left. All challenges are done. #TODO Complete Chapter 3  drills and challenges.Phase 1 is completed.")
    assert result == True
# result shows boolean value if #TODO is there in the text