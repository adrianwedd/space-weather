
# Starting Point for Each Iteration: Space Weather Dashboard Project

## Pre-Iteration Housekeeping

0. **Extract Attached ZIP File**: Extract the attached ZIP file to the local repository located at `/mnt/data/space-weather`.

## Pre-Iteration Housekeeping

1. **Review Documentation**: Navigate to `/mnt/data/space-weather` and read the following markdown files to understand the project's current state and objectives:
    - `README.md`
    - `CONTRIBUTING.md`
    - `DEPLOYMENT_GUIDE.md`
    - `TASK_LIST.md`

## Analyze, Document, and Implement Across Entire Codebase in `/mnt/data/space-weather`

1. **Preparation and Initial Review**:
    - Examine each directory and file in the local repository, focusing on:
        - `backend/`
        - `frontend/`
        - `docs/`

2. **Codebase Scan for Todos and Documentation**:
- Identify areas lacking but requiring TODOs.  # Updated TODO: Please elaborate on the implementation details.
    - Spot opportunities to enrich inline documentation.

3. **Todo Articulation and Inline Documentation**:
- For each area or existing TODO:  # Updated TODO: Please elaborate on the implementation details.
        1. Understand the context.
2. Articulate or edit the TODO for clarity.  # Updated TODO: Please elaborate on the implementation details.
        3. Improve inline documentation.

4. **Coding and Implementation**:
- Implement the most complete code possible based on the TODOs.  # Updated TODO: Please elaborate on the implementation details.
    - If complete code is unfeasible, include a verbose placeholder.

5. **Validation and Testing**:
    - Validate the implemented code or placeholders.

6. **Final Documentation Check**:
- Ensure all new TODOs and inline comments align with `TASK_LIST.md` and `iteration_logs`.  # Updated TODO: Please elaborate on the implementation details.

## Update Documentation and Development Logs

1. **Update `TASK_LIST.md`**: 
    - List completed tasks and plan the next iteration.
    - Create explicit subtasks.

2. **Development Log Updates**:
    - Generate a new markdown file in `iteration_logs`.
    - Document developments, challenges, and resolutions.

3. **Guides and README Updates**:
    - Update `CONTRIBUTING.md`, `DEPLOYMENT_GUIDE.md`, and `README.md`.

4. **Generate Detailed Commit and Tag Messages**:
    - Prepare comprehensive messages for Git commit and tag.

## Final Steps

1. **Zip the Updated Repository**: Compress the updated repository into a ZIP file.
2. **Download Link**: Provide a download link for the ZIP file.

## Git Commands Template

Detailed Git commands template for verbose commit and tag messages is provided separately.

## Proceed Without Awaiting Confirmation

Once a task is outlined, proceed to execute it without awaiting further permission.

### Git Commands Template for Each Iteration

#### Initial Housekeeping

1. **Switch to the Main Branch and Pull Latest Changes**
    ```bash
    git checkout main
    git pull origin main
    ```

#### Create a New Version Branch

1. **Create and Checkout a New Branch for the Upcoming Version**
    ```bash
    git checkout -b version-x.x.x
    ```

#### Staging, Committing, and Tagging

1. **Stage All Modified Files**
    ```bash
    git add .
    ```

2. **Commit Changes with a Verbose Message**
    ```bash
    git commit -m "Version x.x.x: [Brief Summary]
    
    Detailed changes include:
    - Enhanced [File/Feature 1]: [Description]
    - Improved [File/Feature 2]: [Description]
    - Fixed [File/Feature 3]: [Description]
    - Updated [File/Feature 4]: [Description]
    
    Documentation updates:
    - Updated README.md to reflect [changes]
    - Revised DEPLOYMENT_GUIDE.md for [new steps]
    - Modified CONTRIBUTING.md to include [guidelines]
    
    See TASK_LIST.md and iteration_logs for more details."
    ```

3. **Create a Tag with a Detailed Message**
    ```bash
    git tag -a "v.x.x.x" -m "Version x.x.x focuses on [main feature improvements].
    
    Highlights:
    - Introduced [New Feature/Improvement 1]
    - Enhanced [Existing Feature/Improvement 2]
    
    For a comprehensive list of changes, refer to the commit message and documentation."
    ```

#### Push to Remote Repository

1. **Push the New Version Branch and Tags**
    ```bash
    git push origin version-x.x.x
    git push origin --tags
    ```

In this template, `x.x.x` should be replaced with the appropriate incremental version number. The commit and tag messages are designed to be verbose, detailing not just what changes were made but also why they were necessary, thereby providing a complete narrative of the iteration.

---

## Important Notes for Next Iteration
- Comments, docstrings, TODOs, etc., should be manually expanded, not programmatically.  # Updated TODO: Please elaborate on the implementation details.
- Git commands should be specific to the version and ready for execution, displayed in a code block.