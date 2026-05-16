
import streamlit_authenticator as stauth

def setup_auth():

    names = ["Srishti Rao"]

    usernames = ["admin"]

    passwords = ["admin123"]

    hashed_passwords = [
        stauth.Hasher.hash(password)
        for password in passwords
    ]

    authenticator = stauth.Authenticate(
        {
            "usernames": {
                usernames[0]: {
                    "name": names[0],
                    "password": hashed_passwords[0]
                }
            }
        },
        "ai_dashboard",
        "abcdef",
        cookie_expiry_days=1
    )

    return authenticator

