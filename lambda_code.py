import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
import json
from datetime import datetime
from dotenv import load_dotenv
import os

# Load enviromental variables
load_dotenv()

# Access the variables
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_TEST1 = os.getenv("EMAIL_TEST1")
EMAIL_TEST2 = os.getenv("EMAIL_TEST2")


def lambda_handler(event, context):
    try:
        return lambda_handler2(event, context)
    except Exception as ex:
        print(ex)
        return {
            'statusCode': 500,
             'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers'
            },
            'body': json.dumps(str(ex))
        }
        

def lambda_handler2(event, context):
    if event.get("httpMethod") == "OPTIONS":
        return {
            'statusCode': 200,
             'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers'
            },
            'body': ""
        }
    
    
    print(f"event is: {event}")
    # extract the payload from the event body
    
    payload = json.loads(event['body'])
    
    # Extract tje email from the payload
    email = payload['email'].lower().strip()
    print(f'email is: {email}')
    if email == EMAIL_USER or email == EMAIL_TEST1 or email == EMAIL_TEST2:
        # body = event['body']
        # print(f"BODY is: {body}")
        # now = datetime.now() 
        # print(f"%%%%%%% I WAS CALLED @ {now} %%%%%%%")
        lambda_get_link()
        return {
            'statusCode': 200,
             'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers'
            },
            'body': json.dumps('Hello from Lambda! Your email was sent')
        }
    else:
        return {
            'statusCode': 401,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers'
            },
            'body': json.dumps('Hello from Lambda! The email is NOT correct or UNAUTHORIZED')
        }

def lambda_get_link(bucket_name='xs-take-home-assign', key_filename='murder-mystery.mp4', expires_in=3600):
    print(f"Lambda was called")
    client_method = "get_object"
    method_parameters = {'Bucket': bucket_name, 'Key': key_filename}
    s3_client = boto3.client('s3',
                           region_name="us-east-2",
                          config=Config(signature_version="s3v4"),
                          endpoint_url="https://s3.us-east-2.amazonaws.com",
                           )
    
    url = s3_client.generate_presigned_url(
            ClientMethod=client_method,
            Params=method_parameters,
            ExpiresIn=expires_in
        )
    print("===")
    print(url)
    print("===")
    # Assuming the user flow exists
    recipient = EMAIL_USER
    lambda_send_email(url, expires_in, recipient)
    print(f'Attempt to send an Email was made at: {datetime.now()}')
    return {
        'statusCode': 200,
        'body': json.dumps(url)
    }

    
def lambda_send_email(context, expires_in, RECIPIENT=None):
    SENDER = f"Xeniya S. <{EMAIL_TEST2}>"

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    if RECIPIENT is None:
        RECIPIENT = EMAIL_TEST2
    
    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-2"
    
    # The subject line for the email.
    SUBJECT = "Amazon SES from Xeniya S. with your requested link"
    
    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES from Xeniya S. (using Python)\r\n"
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto)."
                )
                
    # The HTML body of the email.
    BODY_HTML = f"""
    <html>
     <head></head>
     <body>
       <h1>Amazon SES from Xeniya S. (SDK for Python)</h1>
       <p>This email was sent with
         <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
         <a href='https://aws.amazon.com/sdk-for-python/'>
           AWS SDK for Python (Boto)</a>.
           <br>Here is your secure link, which expires in {expires_in}sec: <br>{context} </p>
     </body>
    </html>
                """            
    
    # The character encoding for the email.
    CHARSET = "UTF-8"
    
    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)
    
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])