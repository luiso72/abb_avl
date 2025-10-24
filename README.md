# Binary Search Tree API

Simple Binary Search Tree (BST) project with REST API using FastAPI.

**Built from scratch without additional libraries** - Only FastAPI for the REST API.

## What is a Binary Search Tree?

It's a data structure where:
- Each node has a value
- Smaller values go to the **left**
- Greater values go to the **right**

## Installation

### Option 1: Using Virtual Environment (Recommended)

1. Create and activate virtual environment:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate
```

2. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

3. Run the server:
```bash
python -m uvicorn main:app --reload
```

### Option 2: Using the provided script (Windows)

```bash
# Double-click or run:
run_server.bat
```

### Option 3: Direct execution

```bash
# If Python and dependencies are in PATH:
python -m uvicorn main:app --reload
```

4. Open in browser:
```
http://localhost:8000/docs
```

## Troubleshooting

### ModuleNotFoundError: No module named 'fastapi'

**Problem:** FastAPI or other dependencies not found.

**Solutions:**
1. **Use the provided script:** `run_server.bat` (installs dependencies automatically)
2. **Check Python version:** `python --version` (should be 3.8+)
3. **Reinstall dependencies:** `python -m pip install -r requirements.txt`
4. **Use virtual environment:** Follow Option 1 in Installation

### ImportError in IDE

**Problem:** IDE shows import errors but code works.

**Solutions:**
1. **Restart IDE** - Often resolves false import errors
2. **Configure Python interpreter** in your IDE settings
3. **Use virtual environment** - Set IDE to use `.venv` environment
4. **Clear IDE cache** - Restart Python language server

### Port 8000 already in use

**Problem:** Port 8000 is occupied by another process.

**Solution:** Change port:
```bash
python -m uvicorn main:app --reload --port 8001
```

### Multiple Python installations

**Problem:** Different Python versions causing conflicts.

**Solution:** Use virtual environment (Option 1) to isolate dependencies.

## Available Endpoints

### 1. Insert a value
```
POST /tree/insert?value=10
```

### 2. Search for a value
```
POST /tree/search?value=10
```

### 3. Prune (delete) a value
```
DELETE /tree/prune?value=10
```

### 4. View tree structure
```
GET /tree/structure
```

### 5. Inorder traversal (left -> root -> right)
```
GET /tree/traversal/inorder
```

### 6. Preorder traversal (root -> left -> right)
```
GET /tree/traversal/preorder
```

### 7. Postorder traversal (left -> right -> root)
```
GET /tree/traversal/postorder
```

### 8. View saved data
```
GET /tree/saved-data
```

### 9. Clear the tree
```
DELETE /tree/clear
```

## Example Usage

### Using curl:
```bash
# Insert values
curl -X POST "http://localhost:8000/tree/insert?value=50"
curl -X POST "http://localhost:8000/tree/insert?value=30"
curl -X POST "http://localhost:8000/tree/insert?value=70"

# View structure
curl "http://localhost:8000/tree/structure"

# Search for a value
curl -X POST "http://localhost:8000/tree/search?value=30"

# Delete a value
curl -X DELETE "http://localhost:8000/tree/prune?value=30"
```

### Using the web interface:
1. Go to: http://localhost:8000/docs
2. Click on an endpoint to expand it
3. Click "Try it out"
4. Enter parameters and execute

## Usage Example

1. Insert values:
   - Insert 50
   - Insert 30
   - Insert 70
   - Insert 20
   - Insert 40

2. View the structure (you'll see how the tree is organized)

3. View inorder traversal (you'll see the sorted values: 20, 30, 40, 50, 70)

## Project Structure

```
windsurf-project-3/
├── app/
│   ├── services/        # Tree logic (built from scratch)
│   └── controllers/     # API endpoints
├── main.py             # Main file
└── requirements.txt    # Only FastAPI and Uvicorn
```

## What was built from scratch

- ✅ Node class with **children** array (no libraries)
- ✅ BinarySearchTree class with **root** (no libraries)
- ✅ **insert()** function with recursion
- ✅ **search()** function with recursion
- ✅ **prune()** function (delete) with recursion
- ✅ Traversals (inorder, preorder, postorder)
- ✅ Data storage in list
- ✅ Conversion to dictionary for JSON

**No Pydantic or other additional libraries were used**

## Terminology Used

- **root**: The first node of the tree
- **children**: Array of 2 elements [left_child, right_child]
- **insert**: Add a new value to the tree
- **search**: Find a value in the tree
- **prune**: Remove (delete) a value from the tree
