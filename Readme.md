# Super Octo Computing SE

## Project Overview

Welcome to the Super-Octo-Computing Search Engine project! This is a framework for building a powerful search engine that combines a custom web crawler with a meta-search aggregator. The project is designed to provide comprehensive, high-quality search results by leveraging both its own indexed data and results from other search providers.

### Core Components
*   **Web Crawler (Spider):** Systematically crawls the web to build a proprietary index of web pages. It respects `robots.txt` rules and is designed for scalability and efficiency.
*   **Indexer:** Processes the raw data extracted by the spider, creating a structured, inverted index for fast and relevant search queries.
*   **Meta-Search Aggregator:** Queries multiple search engines (including our own index) and intelligently merges and ranks the results to provide the best possible output.
*   **Search Interface:** A user-friendly web interface for performing searches and viewing the aggregated results.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python (version 3.12.3)
*   Docker and Docker-Compose (recommended)
*   [Npm, Venv, ]

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/indivisiblefoundation/super-octo-computing-se.git
    cd super-octo-computing-se
    ```

2.  **Set up environment variables:**
    Copy the example environment file and fill in your details, such as API keys for third-party search engines.
    ```sh
    cp .env.example .env
    source /env/bin/activate
    ```

3.  **Run with Docker Compose (Recommended):**
    The easiest way to start all services is by using Docker Compose.
    ```sh
    docker-compose up --build
    ```

4.  **Manual Installation (Alternative):**
   Manual setup instructions
1. Clone the repository and create a virtual environment
First, set up your local project directory and a virtual environment to isolate the project's Python dependencies.

    Clone the project:
    sh

    git clone https://github.com/your-username/super-octo-computing-se.git
    cd super-octo-computing-se

    Use code with caution.

Create and activate a virtual environment:
sh

python -m venv venv
# On macOS and Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

Use code with caution.
Install Python dependencies:
sh

pip install -r requirements.txt

Use code with caution.

2. Install and run Elasticsearch
You will need to manually download and run Elasticsearch.

    Download Elasticsearch: Get the appropriate version (e.g., 8.14.0 for this project) from the official Elasticsearch download page.
    Extract the files: Unzip or untar the downloaded file to a preferred location.
    Configure Elasticsearch (for development):
        Navigate to the extracted Elasticsearch directory.
        Edit the config/elasticsearch.yml file.
        For a simple setup, you can set xpack.security.enabled: false and discovery.type: single-node.
    Run Elasticsearch:
        Open a new terminal window or command prompt.
        Navigate to the Elasticsearch directory and run the executable.
        On macOS and Linux: ./bin/elasticsearch
        On Windows: bin\elasticsearch.bat
        Elasticsearch will start and be available at http://localhost:9200. 

3. Set up environment variables
Unlike the Docker version, you will need to manually set your environment variables for each terminal session.

    Create a .env file: Create this file in your project's root directory.
    Load the file for each terminal:
        On macOS and Linux: export $(cat .env)
        On Windows (PowerShell): Get-Content .env | ForEach-Object { $var = $_.Split('='); Set-Item -Path Env:\$($var[0]) -Value ($var[1]) } 

4. Run the web interface (FastAPI)
The search interface runs on a web server like Uvicorn.

    Open a new terminal and activate your virtual environment.
    Run the Uvicorn server:
    sh

    uvicorn app.main:app --reload

    Use code with caution.

Your web interface will be available at http://localhost:8000. 

5. Run the web crawler (Scrapy)
The crawler can be run as a separate process from your terminal.

    Open a new terminal and activate your virtual environment.
    Execute the Scrapy crawler command:
    sh

    scrapy crawl [your_spider_name]

    Use code with caution.

You can monitor the output in the terminal to see its progress and any errors. 

Troubleshooting tips for a manual setup

    Port conflicts: Ensure that no other services are using ports 9200 (for Elasticsearch) or 8000 (for FastAPI).
    Environmental issues: The manual setup is more sensitive to environmental factors. Make sure the correct paths to Elasticsearch and Python are used.
    Dependency mismatches: Unlike a containerized build, manual installation could lead to version differences. The requirements.txt file helps, but it's important to use a virtual environment to prevent conflicts with your system's Python packages. 
## Usage

### Starting a Crawl

To start populating your index, you can use the built-in spider.
```sh
# Example command
python spider.py --seed-url "https://example.com"
