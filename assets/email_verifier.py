import quickemailverification 

def email_verifier():

    # client = quickemailverification.Client('API_Key_Here')
    api_key = input ('Enter Your API Key(******):') #for tests
    client = quickemailverification.Client(api_key)
    quickemailverification = client.quickemailverification()

    # PRODUCTION MODE
    # response = quickemailverification.verify('test@example.com')

    # SANDBOX MODE
    verify_this = input ('>>> Enter email to verify:')
    response = quickemailverification.sandbox(verify_this)

    print(response.body) # The response is in the body attribute

email_verifier()
