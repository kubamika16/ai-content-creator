# AI Content Creator

The AI Content Creator is a tool designed to automate the generation of creative content, such as recipes, using advanced AI models. This project integrates Python with APIs from OpenAI and MidJourney to create personalized and visually appealing content, which is then posted to Instagram at [@fasthealthyrecipes123](https://www.instagram.com/fasthealthyrecipes123/).

## How It Works

### Step 1: Recipe Generation
The process starts with generating a recipe using the OpenAI API. A specific prompt is given, and the AI responds with a detailed recipe.

### Step 2: Image Prompt Creation
An image prompt is then generated for MidJourney. The AI interprets the recipe and creates a prompt for generating a corresponding image, detailing visual elements like lighting and composition.

### Step 3: Image Generation
Using the prompt, MidJourney generates a high-quality image representing the recipe. This image is fetched and prepared for posting.

### Step 4: Posting to Instagram
The generated image and recipe are posted to the Instagram account [@fasthealthyrecipes123](https://www.instagram.com/fasthealthyrecipes123/) using the Instagram Graph API. The process involves creating a media container and publishing it to the connected Instagram account.

## CI/CD Pipeline and AWS Lambda Deployment

This project employs a continuous integration and continuous deployment (CI/CD) pipeline to ensure smooth operation:

- **GitHub Integration:** Changes committed locally are automatically pushed to the GitHub repository and then deployed to an AWS Lambda function through a YAML configuration file.
- **Lambda Function Adjustments:** To ensure the project runs smoothly on AWS Lambda, several modifications were made:
  - Adjusting imports to use root folders.
  - Installing necessary packages that were not required locally but are needed in the Lambda environment.
  - Setting up environment variables directly within the Lambda function due to restrictions from `.gitignore`.
- **Automated Posting Schedule:** The Lambda function is triggered daily at around 6:00 AM via Amazon EventBridge, automating the posting of new recipes to Instagram.
