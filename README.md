# root-activity-detector
Automated alerts when AWS root user activity is detected. 
This Lambda function listens for AWS CloudWatch API calls made by the **root user**.  
If detected, it sends an **email alert** through Amazon SNS.

### Architecture
CloudTrail -> Cloudwatch -> EventBridge Rule -> Lambda -> SNS -> Email alert
![Untitled Diagram](https://github.com/user-attachments/assets/5484f680-e418-4c78-a041-c99e5b681abe)

## Process
It is advisable to create the integrations from right to left, as CloudTrail immediately starts sending API events. 

**Step-1:** Create email to which alerts are to be delivered. Ensure this email can be used for subscription confirmation.

**Step-2:** Create SNS topic and add a subscription to the email address created in step-1.

**Step-3:** Create an AWS Lambda function using the code found in lambda-code.py. Assign execution role as per the policy present within IAM policies folder. You can also have the function log to CloudWatch in a different log group for troubleshooting.

**Step-4:** Create EventBridge rule using the pattern present in eventpattern.json. Assign a role during the creation of the rule. Policy details are present in the iAM policies folder.

**Step-5:** You may either use an existing S3 bucket or create one during configuring CloudTrail. If you want to use an existing S3 bucket, make sure to update the bucket policy so that CloudTrail can put events. Bucket policy can be found in the IAM policies folder.

**Step-6:** Create CloudWatch log group. Most of the time, its better off to have the service create a new log group for proper segregation. But its fine if you want to use an existing log group. 

**Step-7:** Create CloudTrail new trail and configure the respective destinations created in Step-5 & 6. Ensure the role for CloudTrail is updated as per the policy present in IAM policies folder.
