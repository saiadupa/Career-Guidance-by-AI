---

# Career Guidance by AI

## Overview

**Career Guidance by AI** is a web application designed to provide personalized career guidance based on users' areas of interest and current professional stages. The application uses OpenAI's GPT-3.5 Turbo model to generate customized career roadmaps and estimated timeframes for achieving career goals.

## Features

- **Select Area of Interest**: Users can choose from various fields such as Technology, Healthcare, Business, Education, Engineering, Finance, Creative Arts, Science, and Hospitality and Tourism.
- **Select Job**: Based on the selected area of interest, users can select from a list of suggested jobs.
- **Current Stage Details**: Users can specify their current professional stage and receive a personalized roadmap for reaching their desired job, including estimated timeframes.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- Pip (Python package installer)
- An OpenAI API key (sign up at [OpenAI](https://beta.openai.com/signup/))

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/saiadupa/Career-Guidance-by-AI.git
   cd Career-Guidance-by-AI
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Place your OpenAI API key in `.env` file in the project directory:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

   Open your web browser and go to `http://localhost:8501` to start using the application.

## Techniques Used

- **OpenAI GPT-3.5 Turbo**: For generating personalized career roadmaps based on user inputs.
- **Streamlit**: A framework for creating interactive web applications with Python.
- **dotenv**: For managing environment variables.

## Technologies Used

- **Python 3.7+**
- **Streamlit**: Web framework for creating interactive apps.
- **OpenAI GPT-3.5 Turbo**: AI model for generating text-based responses.
- **dotenv**: For handling environment variables securely.

## Project Structure

```
├── app.py                  # Main application file
├── .env                    # Environment variables
├── requirements.txt        # List of dependencies
└── README.md               # This README file
```

## Usage

1. **Navigate to the 'Select Area of Interest' page** and choose an area that aligns with your interests.
2. **Move to the 'Select Job' page** to view and select a job related to the chosen area.
3. **Go to the 'Current Stage Details' page** to provide your current professional stage and generate a personalized career roadmap.

## Troubleshooting

- **Issue with OpenAI API Key**: Ensure that your API key is correctly added to the `.env` file and that you have access to the OpenAI API.
- **Application Errors**: Check the error messages in the terminal for troubleshooting.

## Contributing

Feel free to submit issues or pull requests. Contributions to improve the application are welcome!

## Note

Place your OpenAI API key in the `.env` file to ensure the application functions correctly.

---
