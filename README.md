# Rapid Document Conversion using AWS (Free Tier)

## 📌 Project Overview
This project automatically converts uploaded documents into text using a serverless AWS architecture.

## 🛠 AWS Services Used
- Amazon S3
- AWS Lambda
- Amazon Textract
- IAM

## 🔄 Architecture
1. User uploads document to S3.
2. S3 triggers Lambda.
3. Lambda extracts text using Textract.
4. Output text stored in S3.

## 📂 Supported Files
- JPG
- PNG
- Small PDFs
- 
## 💡 Key Features
- Fully serverless
- Event-driven architecture
- AWS Free Tier friendly
- Automatic text extraction

## 🧪 How to Test
1. Upload an image to input S3 bucket
2. Check output bucket for `.txt` file


### See screenshots folder for execution proof.

## 👤 Author
Yash
