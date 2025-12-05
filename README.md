# genai-project-template

A minimal, open source, extensible blueprint for building projects that integrate with conversational AI (PandasAI for demo) and Web app(streamlit for demo) services. Use this template as a starting point for proof-of-concepts, demos, or production projects that leverage streamlit and conversational AI capabilities. We can incorporate paid OpenAI or similar versions for faster results but this utility is designed to act as a starting point and blueprint only.

Why this template exists
- Provide a consistent project layout and developer workflow.
- Document common setup steps and security considerations for working with data exploration with AI and Web App.
- Make it easier to share and reproduce examples.
- Talk to your data (single or multiple datasets) easily instead of writing SQL queries

Table of contents
- Project overview
- Features
- Prerequisites
- Quick start (clone & run)
- Usage examples
- Project structure
- Development workflow
- Testing
- CI / Deployment
- Security & best practices
- Contributing
- License
- Support / Contact

Project overview
This repository is a generic project scaffold for integrating Generative AI into an application. It is intentionally lightweight and language-agnostic so you can adapt it to Python, Node.js, or other stacks.

Features
- Opinionated project layout suitable for demos and prototypes
- Guidance for setting up infrastructures for Ollama
- Examples and placeholder files for model calls, request/response handling, and local testing
- Guidance on CI and deployment for common environments

Prerequisites
- git and your preferred runtime (Python 3.10+) installed locally. (verify the library versions from the CI file)
- Familiarity with environment variables and secrets management.
- Familiarity with Pandas dataframes and streamlit

Quick start (example)
1. Clone the repo
   git clone https://github.com/kaulabbasu/genai-project-template.git
   cd genai-project-template

2. Choose a runtime (examples below show Python)
   - Python (example)
     python -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt

3. Install Ollama in local system
    https://ollama.com/download

4. Have a Python IDE installed (preferred VSCode)
5. Run the programs
     a. Smartdataframe (single dataframe operation) :
         python -m streamlit run smartdf_streamlit.py

     b. Agent (multi dataframe operation) :
         python -m streamlit run agent_streamlit.py


Usage examples
This template includes example text files that one can use as input datasets from streamlit app

1. Agent app - (Talk to multiple datasets and retrieve/manufacture desired output)

   Upload multiple(with related entity, so that you get to talk to both the datasets simultaneously) datasets:
   
   <img width="560" height="327" alt="image" src="https://github.com/user-attachments/assets/34c6658a-94dd-45c3-9c75-28fcb1d7846a" />

   First 5 records for both the datasets
   
   <img width="454" height="285" alt="image" src="https://github.com/user-attachments/assets/e6dbfda7-2a34-4cc2-9c95-44f489f94cb0" />

   Start the conversation
   
   <img width="479" height="164" alt="image" src="https://github.com/user-attachments/assets/b43a9652-907a-4705-9867-d35a6f56a770" />

   The desired result

   <img width="458" height="176" alt="image" src="https://github.com/user-attachments/assets/1b9f4758-89d8-4695-85c9-c3842fd85ab2" />



Project structure (recommended)
- /examples                 # runnable examples that call GenAI APIs
- /src or /app              # application source code
- /tests                    # unit and integration tests
- /.github/workflows        # CI workflows (lint, test, build)
- /docs                     # additional documentation and design notes
- README.md                 # this file
- LICENSE

Development workflow
1. Create a feature branch from main.
2. Implement your changes and add tests.
3. Run unit tests and linters locally.
4. Push the branch and open a pull request.
5. CI will run automated checks; once green, request reviews and merge.

Testing
- Keep unit tests small and focused.
- Use mocks for network calls (do not hit GenAI APIs in unit tests).
- For integration tests, use a separate GCP project or service account and ensure costs/quotas are acceptable.
- Add test cases for prompt formatting, response parsing, and safety/error handling.

CI / Deployment
- Add a workflow in .github/workflows to run linting, tests, and optionally a build step.
- For deployments (Cloud Run, App Engine, GKE), prefer Workload Identity and avoid storing service account keys in the repo.
- Example workflow steps:
  - Checkout
  - Set up runtime
  - Install dependencies
  - Run tests
  - Build and deploy (conditional on branch or tag)

Security & best practices
- Never commit service account JSON keys or API keys.
- Use secret managers (GitHub Secrets) for CI/CD.
- Validate and sanitize user inputs before sending them to a model.
- Implement safety checks on model responses (e.g., content filtering, rate limiting).

Cost considerations
- Generative AI models may incur substantial charges depending on usage, model choice, and response size. (In case of paid vrsions only)
- Test with small inputs and monitor billing dashboards during experiments. (In case of paid vrsions only)

Contributing
Contributions are welcome. Please:
1. Fork the repository.
2. Create a feature branch.
3. Open a pull request with a clear description and test coverage.

Suggested contribution checklist:
- Add or update examples to demonstrate a concrete integration.
- Improve docs with step-by-step setup for a given runtime (Python).
- Add test cases that mock GenAI responses and validate your parsing code.

License
Specify a license for this template (e.g., MIT, Apache 2.0). Update this section with the chosen license text or a reference to the LICENSE file.

Support / Contact
- Open an issue in this repository for bugs, feature requests, or questions.

Acknowledgements
- This template draws on common patterns for working with conversational models and aims to simplify starting a new project.

Next steps
- Customize sections above with concrete instructions for your chosen runtime (install commands, sample code, required dependencies).
- Consider adding example code files in /examples for Python if you want runnable demonstrations.
