
# Contributing to Space Weather Project

## Project Objectives
This project aims to develop a comprehensive web application for monitoring various space weather indices and phenomena. It integrates backend Python scripts for data retrieval and processing with a frontend interface for visualization and user interaction.

## Task List
1. Wrap Data Fetching Scripts: Convert existing Python scripts for data fetching into callable functions.
2. API Endpoint Processing: Write Python functions to process and interpret data for each API endpoint.
3. Flask Backend Setup: Establish a Flask server and define the necessary routes for API data handling.
4. Frontend Redesign: Evaluate the possibility of adopting a frontend framework like React.
5. Frontend-Backend Integration: Implement the API calls between the frontend and backend.
6. Search and Filters: Implement frontend features for data searching and filtering.
7. Interactive Visualizations: Add interactive data visualizations on the frontend.
8. Documentation Expansion: Add to the existing API usage guide and codebase documentation.
9. Testing Strategy: Develop unit tests, integration tests, and outline user testing methods.
10. Deployment Preparation: Prepare the codebase for eventual deployment, following best practices.

## Iteration 3 Update
- Exploration of Python scripts related to data fetching and processing to identify areas requiring additional features or completion.

## Iteration 3 Update
- Created CONTRIBUTING.md to guide potential contributors on the project objectives and task list.

## Iteration 3 - Manual Code Inspection Update
- Conducted a thorough manual inspection of backend Python files.
- Added inline TODO comments to identify areas requiring attention or further development.

## Iteration 4 Preparations
- Added a `requirements.txt` in the backend directory for managing Python package dependencies.

## Revised Task List
1. Backend Data Wrapping: Convert existing Python scripts for data fetching into callable functions and modules.
2. Backend API Development: Create Flask routes to serve as API endpoints for the frontend to access backend data.
3. Frontend Data Fetching: Implement AJAX or Fetch API calls in JavaScript to retrieve data from backend API endpoints.
4. Frontend Design Overhaul: Evaluate and potentially adopt a frontend framework like React or Vue.js for a more responsive design.
5. Search and Filter Functionality: Add frontend features to enable data searching and filtering.
6. Data Visualization: Implement interactive charts and graphs using libraries such as D3.js or Chart.js.
7. Error Handling and Validations: Add necessary validations and error-handling both on the frontend and backend.
8. Documentation and Comments: Keep README.md, development_log.md, and CONTRIBUTING.md updated. Add inline comments and function docstrings in the code.
9. Testing: Develop a testing strategy including unit tests for backend and frontend, and outline steps for user acceptance testing.
10. Deployment: Prepare the codebase for deployment, ensuring best practices in security and performance.

## Iteration 4 - Manual Code Inspection Update (Frontend)
- Conducted a meticulous manual inspection of frontend files (HTML, CSS, JavaScript).
- Added inline TODO comments to highlight areas requiring further development or optimization.

## Iteration 5 - Backend Data Wrapping
- Identified `data_retrieval.py` as the primary backend file for data fetching.
- Outlined subtasks including function wrapping, modularization, API key management, and error handling.


## Iteration 6 - Function Wrapping
- Created `modularized_data_retrieval.py` to host modular functions for data retrieval.
- Implemented a skeleton function for API data fetching.


## Iteration 7 - Backend Modularization
- Created three new Python modules to better organize backend functionalities.


## Iteration 8 - Secure API Key Management
- Enhanced security by fetching the API key from an environment variable in `modularized_data_retrieval.py`.


## Iteration 9 - Error Handling and Logging
- Implemented basic error handling and logging in `modularized_data_retrieval.py`.


## Iteration 10 - Frontend Refinement
- Identified and implemented refinements based on inline TODO comments in the frontend HTML files.


## Iteration 11 - Backend Placeholder Implementations
- Identified and started refining placeholder implementations in the backend Python files.


## Iteration 12 - Writing Unit Tests
- Initiated the process of writing unit tests by creating a sample for the `get_a_index` function in `data_retrieval.py`.


## Iteration 13 - Preparing for Deployment
- Created a Deployment Guide to facilitate the application's deployment process.


## Iteration 14 - Implementing Additional Features
- Added error logging for API calls in the `get_a_index` function.


## Iteration 15 - Optimizing Performance and Memory Usage
- Focused on optimizing the `get_a_index` function by incorporating lazy-loading techniques.


## Iteration 16 - Implementing Data Caching
- Added data caching to the `get_a_index` function using a simple dictionary for caching API responses.

