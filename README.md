# autoLambdadeployusinggithubaction
automatic AWS Lambda Deploy using Github Action


https://medium.com/@ivangomezarnedo/automating-aws-lambda-deployments-with-github-actions-cc632138d069

Automating AWS Lambda Deployments with GitHub Actions
A guide on how to automatically update your AWS Lambda functions when something changes in your GIT repository

https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3E9Ak2nY3CpZFfFRMDTR5Q.png![image](https://github.com/RahulBendale/autoLambdadeployusinggithubaction/assets/40611128/5dd15074-e37b-41ef-a8ed-eb98aa513476)

Introduction
To deploy a Lambda function in AWS we have two options:
Upload the .zip file containing the code and the Python environment in which that code has to be executed.
Create a container (containers provide an encapsulated environment for your function).
In this article, we’ll focus on the first option. This method allows the supplementary use of Lambda Layers to incorporate bulkier libraries such as Pandas or scikit-learn. However, this approach has historically posed a challenge: the deployment process to AWS Lambda has been painstakingly manual. It required:
Set up the Python environment (.zip file).
Integrate the changed code.
Upload the package to S3.
Configure Lambda to use this new package.
Such a labor-intensive method was not just time-consuming but also riddled with potential for human errors. Consequently, this often resulted in delays in rolling out new features, addressing bugs, and posed complications in tracking and scaling deployments.
Our objective is simple: Transform this cumbersome process. By leveraging Github Actions, our aim is to expedite continuous development cycles and bolster continuous integration practices. Throughout this article, we’ll guide you on automating the deployment of modified files to AWS Lambda. By embracing this method, each time you commit to the main branch — a common practice to signal stable, production-ready changes — the deployment is automated, sidestepping the previously tedious procedures and enhancing the entire workflow.
Lambda Layers and .zip files
For Lambda functions that use the Python runtime, a dependency can be any Python package or module. When you deploy your function using a .zip archive, you can either add these dependencies to your .zip file with your function code or use a Lambda layer.
For a deeper understanding of deployment sizes, their limitations within AWS Lambda, and a comprehensive guide on using Lambda Layers, refer to our previous article:

In essence, the .zip file houses the main codebase and lighter libraries, while Lambda Layers encapsulate larger, more static libraries. This separation ensures that frequent code updates remain independent of bulky, often unchanging dependencies, culminating in a more efficient deployment mechanism.


How To
Requirements
The keys of an AWS user with permissions to modify the Lamda and S3 bucket to be used. You can attach the following policies to the newly created user:

A Github repository with your Python code and with a ‘main’ branch (In this repository you only need to upload your code, not the list of your used libraries).
Configuration of these keys as Github Secrets of the previous repository (use the following names as they will be used in the script):

An already created S3 bucket that contains a .zip file with the Python environment to be used in your Lambda function.
An already created AWS Lambda (in the same region of that S3 bucket)
Code
In your root project folder, add the following file in the path: “.github/workflows/deploy-lambda.yml” and it will be automatically taken by Github when you commit to the repository.


The steps that it will perform are:
‘Checkout Repository’ section. It will fetch the current and the previous commit, so we can compare which files have changed.
‘SetUp AWS CLI’ section. It will configure the AWS CLI with the previously defined Github secrets.
‘Deploy Modified files’ section. It will download the .zip file that is currently being used in the Lambda and it will uncompress it. Then, it will loop over all the modified files and it will overwrite (or add) them to the uncompressed directory. Finally, it will compress again that directory (with the modified files) and it will upload it to S3 and it will update the Lambda function.
The previous file is configured to search for modified Python files. But you can modified the file extension that it will have to look for so it could be used with other programming languages or files.
Results
Then, the next time that you commit something to your main branch, click in the Actions tab on Github and you will see something like:


And you should see the list of changed files in the section ‘Print changed files’:

To ensure that the correct version of the file is being used, you could check the content of the changed files in the execution log of the section ‘Deploy Modified Files’:

Conclusion
During this article we have seen how to automatically update and deploy a Lambda function when you commit to a Github repository by using Github Actions. Some advantages of this approach:
Automated Efficiency: Removes the tedious task of manual deployments, making updates swift and consistent.
Rapid Iteration: Immediate deployment of code changes ensures quick releases and responsive bug fixes.
Traceability: Each deployment is tied to a specific Git commit, offering clarity on what’s deployed and by whom.
Scalability: As projects grow, our automated system seamlessly handles more frequent and complex deployments.
In essence, this approach turns a cumbersome, error-prone process into a streamlined, efficient, and traceable deployment mechanism.
