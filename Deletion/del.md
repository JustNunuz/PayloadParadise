### File Deletion Script Overview

This Python script deletes a specified file from the user's Desktop. It checks if the file exists, and if so, removes it permanently using the `os.remove()` function.

### Key Functions:
- **`delete_file_from_desktop(filename)`**:  
   - Constructs the file path to the Desktop.
   - Checks if the file exists.
   - Deletes the file permanently if it exists(does not go to the recycle bin).
