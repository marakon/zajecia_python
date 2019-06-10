def search_email(email_list, email):
    for email in email_list:
        if email == email_input:
            return True
    return False

email_list = ["Elo", "Gitara siema", "Cześć"]
email = input("Podaj mail: ")

search_email(email_list, email)