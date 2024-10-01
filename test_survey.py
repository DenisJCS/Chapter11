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


from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak ?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('english')
    assert 'english' in language_survey.responses

def test_store_three_responses():
    """Test that individual responses stored are stored properly."""
    question = "What language did you first learn to speak ?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses

python3 -m pytest 
========================================== test session starts ===========================================
platform darwin -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/denis_jcs/Documents/Chapter11/Classes
collected 2 items                                                                                        

test_survet.py ..                                                                                  [100%]

=========================================== 2 passed in 0.01s ============================================
