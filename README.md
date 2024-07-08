# QuizGenie

![Banner](/assets/banner.jpg)

## Overview

An AI-powered quiz platform crafted to offer students and learners an interactive way to solidify their grasp of different subjects. Using advanced AI, the tool generates quizzes from documents users provide, giving immediate feedback and thorough explanations to aid in better understanding and memory retention, thereby enriching the learning process.

## Objective:

The lack of accessible and effective means for students and learners to reinforce their understanding of various topics. Recognizing the challenge of obtaining timely feedback and engaging in unlimited practice, the team is developing an AI-generated assessment and quiz tool. This tool aims to provide users with instant feedback and comprehensive explanations, thus facilitating deeper comprehension and retention of knowledge. By dynamically generating quizzes based on user-provided documents, ranging from textbooks to scholarly papers, the tool offers a tailored learning experience. The end result will be a user-friendly platform that empowers individuals to hone their skills, solidify their understanding, and ultimately excel in their academic pursuits.

## Features:

- **AI-Generated Assessments and Quizzes:** Utilizing artificial intelligence, the tool will dynamically generate quizzes and assessments based on user-provided documents, such as textbooks and scholarly papers.
- **Instant Feedback:** Users will receive immediate feedback on their quiz performance, allowing them to quickly identify areas of strength and areas needing improvement.
- **Comprehensive Explanations:** Detailed explanations will be provided for each question, enabling users to understand the reasoning behind correct answers and learn from mistakes.
- **Tailored Learning Experience:** The quizzes will be customized to the content of the user-provided documents, ensuring relevance and alignment with the topics being studied.

## Technologies Used

- **Python** serves as the foundational language for crafting Gemini Quizify's backend logic.
- **Langchain** is harnessed for proficient natural language processing, empowering the tool to adeptly understand and dissect textual content.
- **ChromaDB** stands as the robust database management system, ensuring swift storage and retrieval of user data and quiz content.
- **Google Gemini** plays a pivotal role in AI-driven content analysis and generation, enabling the tool to dynamically craft quizzes from user-supplied documents.
- **Streamlit** enriches the user experience by facilitating the creation of interactive web applications with Python, enhancing the accessibility and usability of Gemini Quizify.

## Implementation

### Agentic Workflow (RAG)
![Task 9 Overview](/assets/implementation.png)

*RAG implementation Architecture*

### Snapshots

**1. PDF Input**

![Generate Quiz Algorithm Input](/assets/pdf_input.png)


**2. Generated Questions**

![Screen State Handling](/assets/generated_question.png)

## Setup Steps
Sure, here are the detailed setup steps for your project, including creating a Google Cloud account, setting up a project, creating a service account with the necessary permissions, and organizing your project directory:

### 1. Create a Google Cloud Account

1. **Visit Google Cloud**: Go to the [Google Cloud website](https://cloud.google.com/).
2. **Sign Up/In**: Click on the "Get started for free" button and follow the instructions to sign up or sign in with your Google account.
3. **Free Trial**: If you're new to Google Cloud, you will receive a free trial with $300 in credits.

### 2. Create a Google Cloud Project

1. **Go to the Google Cloud Console**: Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
2. **Create a New Project**:
   - Click on the project drop-down menu at the top of the page.
   - Click "New Project".
   - Enter your project name, select a billing account, and choose a location.
   - Click "Create".

### 3. Enable Required APIs

1. **Navigate to APIs & Services**:
   - In the left-hand menu, go to "APIs & Services" > "Library".
2. **Enable APIs**:
   - Search for and enable the following APIs:
     - AI Platform API
     - Google Gemini API (if applicable)
     - Any other related APIs your project might need (e.g., Cloud Storage, Compute Engine).

### 4. Create a Service Account and Key

1. **Navigate to IAM & Admin**:
   - In the left-hand menu, go to "IAM & Admin" > "Service accounts".
2. **Create a Service Account**:
   - Click "Create Service Account".
   - Enter a name and description for the service account.
   - Click "Create and continue".
3. **Grant Permissions**:
   - In the "Grant this service account access to project" section, add the necessary roles:
     - AI Platform Admin
     - Google Gemini User
     - Other roles as needed (e.g., Storage Admin for Cloud Storage).
   - Click "Continue".
4. **Create a Key**:
   - Click "Done" to finish creating the service account.
   - In the service account list, find the newly created service account and click on it.
   - Go to the "Keys" tab.
   - Click "Add Key" > "Create new key".
   - Select "JSON" and click "Create".
   - Download the JSON key file. This is your service account key.

### 5. Set Up Your Project Directory

1. **Create a /secrets Directory**:
   - In the root folder of this repository, create a directory named `secrets`.

2. **Place the Service Account Key File**:
   - Move the downloaded JSON key file to the `secrets` directory.

### 6. Create `.env` file
- We will make use of this file to store environment variables for the projects.
- In the `/app` directory we will create and `.env` file.
    ```
    GCLOUD_SERVICE_ACCOUNT_KEY_PATH=<service-account-json-file-name>
    PROJECT_ID=<your-gcp-project-id>
    PROJECT_LOCATION=<your-gcp-project-location>
    ```

Sure, here is the final step to create a Conda environment using the `env.yml` file inside your repository:

### 7. Create a Conda Environment Using `env.yml`

1. **Ensure Miniconda/Anaconda is Installed**:
   - Make sure you have Miniconda or Anaconda installed on your system. You can download and install it from the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) websites.

2. **Navigate to Your Project Directory**:
   - Open a terminal or PowerShell window and navigate to the root of your project directory where the `env.yml` file is located.

   ```sh
   cd /Gemini-Quizify
   ```

3. **Create the Conda Environment**:
   - Use the `conda env create` command to create the environment from the `env.yml` file.

   ```sh
   conda env create -f env.yml
   ```

4. **Activate the Conda Environment**:
   - After the environment is created, activate it using the `conda activate` command followed by the name of the environment (which is defined in the `env.yml` file).

   ```sh
   conda activate gemini
   ```

By following these steps, you will have a fully configured project environment, ready to interact with Google Cloud services and use the necessary Python packages specified in your `env.yml` file.

## Tasks Completed

The project files encompass the following tasks:

1. Integration of Google Service Account for authentication.
2. Implementing a PDF loader for document ingestion.
3. Processing documents using Google Gemini.
4. Generating text embeddings using Langchain.
5. Building a user interface with Streamlit.
6. Creating quizzes based on user-specified topics.
7. Supplying explanations for quiz answers.
8. Handling errors and performing validation.

## Issues Faced
### ⚠️ Question Quality

The current iteration of Gemini-pro predominantly produces JSON markdown results, which occasionally leads to suboptimal question generation. As a remedy, a straightforward prompt engineering methodology has been experimented with and found effective. It has been observed that implementing this prompt engineering approach can significantly enhance the success rate to approximately 80%.
