# Python AI Agent

This project is a Python AI Agent designed to assist users by providing accurate information about world population statistics and details about specific countries using Retrieval Augmented Generation (RAG). It has features such as note-taking and interacting with AI models to query data from PDF and CSV files.

## Features

- **Data Querying**: Retrieve information about world population, Canada, and Singapore from structured data sources.
- **Note Taking**: Save notes through a custom note-taking engine.

## Modules

- `main.py`: Sets up the AI agent with the relevant tools and runs a loop to allow users to interact with the agent.
- `note_engine.py`: Contains functionality to save notes to a text file.
- `pdf.py`: Uses `VectorStoreIndex` for creating searchable indexes of PDFs and provides query engines for accessing data from the indexed PDFs.

## Installation

1. Clone the repo
2. Setup virtual environment and activate venv:

```powershell
py -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies: `pip install -r requirements.txt`
4. Setup env:
    
    Create a .env file in the root directory and add your environment variables:
    
    `OPENAI_API_KEY=your-openai-api-key`
    

## Usage

1. Run the application: `python main.py`
2. Interact with the AI Agent:
    - Enter prompts to query world population data, detailed information about Canada and Singapore, or to save notes.
    - Type `q` to quit the application.
