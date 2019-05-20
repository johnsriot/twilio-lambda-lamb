# twilio-text-to-call
![Image of Architecture](https://github.com/johnsriot/twilio-text-to-call/blob/master/twilio-lambda-lamb.png)

Using Twilio's easy to use APIs and a few AWS services it is possible to create a multitude of text based services. In this particular configuration a user texts a number provided by Twilio. The number is configured through Twilio to send a post request containing the data of the text message to an API Gateway resource (Note: Twilio sends the request to the API gateway in XML format, it can be converted to json at the gateway). A lambda function is triggered and a phone call is made using the Twilio api. Once the call has been executed, a message is returned back through the API gateway, back through Twilio to the original user who text.

This iteration is currently used as an anonymous prank phone call app that uses other cloud resources such as an AWS S3 bucket and TWiML bins through Twilio. What is important about this application is the pattern. It could be altered in such a way to call a large variety of REST APIs. It could also be used as a form of personal information service.     
