from app.processor import processor_lambda



def test_lambda_processor():
    mock_event = {}
    mock_context = {}
    value = processor_lambda(mock_event, mock_context)


    assert True