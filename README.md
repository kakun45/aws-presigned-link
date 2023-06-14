# Take-Home Assignment: AWS Video Clip Download
This project is a solution to a take-home assignment that involves utilizing AWS services to implement a secure video clip download system. The assignment requires the following functionalities:

- Manually dropping a video clip into an S3 repository.
- Writing a Lambda function triggered by user action to generate a secure download URL for the video clip.
- Generating a clickable link in the Lambda function response.
- Sending an email containing the download link to the authorized recipients.
- Allowing the recipient to securely download the video clip by clicking the link.
- Implementing API restrictions to only allow HTTP requests from authorized domains.
- Implementing checks to ensure that only authorized recipients can access the video clip.

## Technologies Used
The solution utilizes the following AWS services:

- S3 (Simple Storage Service) for storing the video clip.
- SES (Simple Email Service) for sending emails to the recipients.
- Lambda for executing the serverless function to generate the download link.

## Architecture Overview
The architecture for the solution involves the following components:

- S3 Bucket: A bucket is created to store the video clip. The video clip can be manually dropped into this bucket.
- Lambda Function: A Lambda function is triggered by user action (e.g., a button click on a web page) or by a direct invocation. The function generates a secure download URL for the video clip and sends an email containing the download link to the authorized recipients.
- SES: SES is used to send emails to the recipients. The Lambda function utilizes SES to send the email containing the download link.
- Authorization Checks: The Lambda function implements checks to ensure that only authorized recipients can access the video clip. This can include checking recipient email addresses against a predefined list of authorized emails.
- API Gateway: API Gateway can be used to restrict HTTP requests to the Lambda function to only authorized domains.

## How to Use
To use this solution, follow these steps:

- Set up an S3 bucket to store the video clip. Manually drop the video clip into the bucket.
- Create a Lambda function that generates a secure download URL for the video clip and sends an email containing the link to the authorized recipients.
- Configure SES to enable email sending from the Lambda function.
- Implement the necessary authorization checks in the Lambda function to ensure only authorized recipients can access the video clip.
- Set up API Gateway and configure it to only allow HTTP requests from authorized domains.
- Trigger the Lambda function either through user action (e.g., a button click on a web page) or by direct invocation.
- Recipients will receive an email containing the download link. When they click the link, the video clip will be securely downloaded.
- Optionally, you can add an expiration time to the download link to make it expire after a certain period (e.g., 24 hours). (I did use it)
- Please note that additional implementation details and code samples specific to your project requirements are necessary to fully implement this solution. The provided information serves as a high-level overview of the solution architecture and general steps to follow.

## Conclusion
This take-home assignment utilizes AWS services such as S3, SES, and Lambda to implement a secure video clip download system. By following the outlined steps and customizing the solution based on your specific requirements, you can create a functional system that allows authorized recipients to securely download video clips. Remember to consider security best practices and implement necessary measures to protect the video clips and ensure that only authorized individuals can access them.

My emplimentation is deployed at https://aws-presigned-link.vercel.app/  All Right Reserved. Xeniya Shoiko