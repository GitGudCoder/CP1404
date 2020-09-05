
def main():
    emails_dict = {}
    email_lengths = []
    name_lengths = []
    new_email = str(input("Email: "))

    while new_email != "":
        name = get_name_from_email(new_email)
        emails_dict[new_email] = name
        name_lengths.append(len(name))
        email_lengths.append(len(new_email))
        new_email = str(input("Enter another email: "))

    # Prints sorted email list
    for item in emails_dict.items():
        print(f"{item[1]:<{max(name_lengths)}} ({item[0]:<{max(email_lengths)}})")


def get_name_from_email(new_email):
    email_split_by_dots = new_email.split(".")
    email_further_split_by_ats = email_split_by_dots[1].split("@")
    name = email_split_by_dots[0].title() + " " + email_further_split_by_ats[0].title()

    is_name = str(input("Is your name {}? (y/n): ".format(name)))
    if is_name == "n":
        name = str(input("Name: "))
    return name


main()