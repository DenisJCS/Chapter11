from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak ?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('english')
    assert 'english' in language_survey.responses


python3 -m pytest
========================================== test session starts ===========================================
platform darwin -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/denis_jcs/Documents/Chapter11/Classes
collected 1 item                                                                                         

test_survet.py .                                                                                   [100%]

=========================================== 1 passed in 0.00s ============================================

