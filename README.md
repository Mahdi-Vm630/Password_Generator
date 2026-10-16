# Password Generator
A Python project that generates different types of passwords using an object-oriented approach with an abstract base class.

## Features
1. PinGenerators - generates a numeric PIN
2. RandomPasswordGenerator - generates a random password with optional numbers and symbols.
3. MemorablePasswordGenerator - generate random words using nltk vocabulary.

## Requirements

- Python 3.7+
- NLTK

to install NLTk, use pip:

```bash
pip install nltk
```

after installing NLTK, you need to download th 'words' corpus. Run python and type these commands:

```python
import nltk
nltk.download('words')
```

That's all you need to know to get started with this project. Enjoy this project.


## Running the project

Make sure you've installed all the required dependencies. You can then set your PYTHONPATH, navigate to the 'source' directory and run the project:

```python
export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory"
cd source
python app.py
```

## Testing

the `app.py` scripts also includes test cases for each password generator. The script will print out a test password for each generator and run checksto make sure the password matches the expected format.