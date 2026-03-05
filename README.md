# Project Overview

This project is set up to demonstrate a basic structure for a Python application using FastAPI.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/harrywphilpotts/M-M.git
   cd M-M
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn app:app --reload
   ```