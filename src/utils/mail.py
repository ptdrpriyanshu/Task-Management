from fastapi_mail import FastMail,MessageSchema,ConnectionConfig,MessageType
from pydantic import EmailStr,BaseModel
from typing import List

 
 

conf = ConnectionConfig(
    MAIL_USERNAME = "nverma404496@gmail.com",
    MAIL_PASSWORD = "xkfr qmoa isrq wxik",
    MAIL_FROM = "nverma404496@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="NV Foundation",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)


async def send_email(emails: List[str]):
    html = """<p> Thanks for Listening me ,you will give thanks to me ,#learn backend from TechSimplus Fastapi series </p> """

    message = MessageSchema(
        subject=" Gaining Skills in backend",
        recipients=emails,  # Removed the extra square brackets here
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return {"message": "email has been sent"}
