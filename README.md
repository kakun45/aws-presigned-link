# AWS Video Clip Download
## Author - Xeniya Shoiko, All rights reserved.

This project is a solution to a take-home assignment that involves utilizing my knowledge of AWS services to implement a secure video clip download system. And was built purely to satisfy my AWS curiosity!
![Screen Shot of one button UI](https://github.com/kakun45/aws-presigned-link/assets/53381916/58af35b4-f652-4d64-9639-0f1ccea488bd)

Requirements:
- Manually dropping a video clip into an S3 repository.
- Writing a Lambda function triggered by user action to generate a secure download URL for the video clip.
- Generating a clickable link in the Lambda function response.
- Send an email containing the download link to the authorized recipients.
- Allowing the recipient to securely download the video clip by clicking the link.
- Implementing API restrictions to only allow HTTP requests from authorized domains.
- Implementing checks to ensure that only authorized recipients can access the video clip.
  


## Technologies Used
The solution utilizes the following AWS services:![Screen Shot of my AWS Console Home](https://github.com/kakun45/aws-presigned-link/assets/53381916/c45fcea6-2a4e-409a-8c1b-5cb099559f38)

- S3 (Simple Storage Service) for storing the video clip.
- SES (Simple Email Service) for sending emails to the recipients.
- Lambda for executing the serverless function to generate the download link.

## Architecture Overview
The architecture for the solution involves the following components:

- S3 Bucket: A bucket is created to store the video clip. The video clip can be manually dropped into this bucket.
- Lambda Function: A Lambda function is triggered by user action (e.g., a button click on a web page) or by a direct invocation. The function generates a secure download URL for the video clip and sends an email containing the download link `presigned_url` to the authorized recipients.

  ![Screen Shot of Lambda generating presigned_url](https://github.com/kakun45/aws-presigned-link/assets/53381916/c3c33481-2381-44d3-8e9c-8e2dd2b93775)


- SES: SES is used to send emails to the recipients. The Lambda function utilizes SES to send the verified email containing the download link.

  ![Screen Shot of SES verified email field](https://github.com/kakun45/aws-presigned-link/assets/53381916/2cfb83b2-dae9-4624-859a-b4d7f2c0be93)

- Authorization Checks: The Lambda function implements checks to ensure that only authorized recipients can access the video clip. This can include checking recipient email addresses against a predefined list of authorized emails.![Screen Shot list of authorized emails](https://github.com/kakun45/aws-presigned-link/assets/53381916/9a7a41a0-b024-44fa-bd82-c061da68648f)

- API Gateway: API Gateway can be used to restrict HTTP requests to the Lambda function to only authorized domains.
![Screen Shot of API Gateway trigger](https://github.com/kakun45/aws-presigned-link/assets/53381916/0208651a-dfd3-4b22-a3c2-6597d60b5117)

## How did I build it
To implement this solution, I broke it down into the following steps:

- Set up an S3 bucket to store the video clip. Manually drop the video clip into the bucket.
- Create a Lambda function(Python) that generates a secure download URL for the video clip and sends an email containing the link to the authorized recipients.
- Configure SES to enable email sending from the Lambda function.
- Implement the necessary authorization checks in the Lambda function to ensure only authorized recipients can access the video clip.
- Set up API Gateway and configure it to only allow HTTP requests from authorized domains.
- Trigger the Lambda function either through user action (e.g., a button click on a web page) or by direct invocation.
- Recipients will receive an email containing the download link. When they click the link, the video clip will be securely downloaded.
- Optionally, I added an expiration time to the download link to make it expire after a certain period (e.g., 24 hours).

## Conclusion
This take-home assignment, which required quick self-study to figure out, utilizes AWS services such as S3, SES, and Lambda to implement a secure video clip download system. By following the outlined steps and customizing the solution based on specific requirements, I can create a functional system that allows authorized recipients to securely download videos. I remembered to consider security best practices and implemented necessary measures to protect the video clips and ensure that only authorized individuals can access them.

All Rights Reserved. Xeniya Shoiko
