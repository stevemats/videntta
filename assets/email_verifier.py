import quickemailverification


def email_verifier():

    # client = quickemailverification.Client('API_Key_Here')
    api_key = input(
        'Enter Your API Key(******) from https://quickemailverification.com/apisettings:')  # for tests
    client = quickemailverification.Client(api_key)
    verifymail = client.quickemailverification()

    # get client email to verify
    verify_this = input('>>> Enter email to verify:')

    # PRODUCTION MODE
    response = verifymail.verify(verify_this)

    # SANDBOX MODE
    # response = quickemailverification.sandbox(verify_this)

    print(response.body)  # The response is in the body attribute
