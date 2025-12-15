# 02 – Python Basics for Generative AI 🐍

> **Learn only the Python you need for GenAI - Nothing more, nothing less**

---

## 🎯 Important Note

This is **NOT a complete Python course**.

We focus **exclusively** on Python concepts used in:

- NLP pipelines
- ML workflows
- GenAI applications

**If you know Python basics**, skim this chapter.  
**If you're new to Python**, pay close attention!

---

## 🐍 Why Python for GenAI?

### Python Dominates AI/ML/GenAI

```
┌─────────────────────────────────────┐
│   Why Python is the AI Standard     │
└─────────────────────────────────────┘

✅ Simple, readable syntax
✅ Massive AI/ML ecosystem
✅ Powerful libraries (NumPy, Pandas, PyTorch)
✅ Industry standard (Google, OpenAI, Meta)
✅ Huge community support
✅ Fast prototyping
```

### GenAI Frameworks (All Python-First):

- **Transformers** (Hugging Face)
- **LangChain**
- **LlamaIndex**
- **TensorFlow / PyTorch**
- **OpenAI API**
- **NLTK / spaCy**

**Bottom line:** If you want to work with GenAI, you need Python.

---

## 📌 Essential Python Concepts for GenAI

### 1️⃣ Functions

**Why they matter in GenAI:**

GenAI pipelines are built with functions:

- `preprocess_text()` - Clean input
- `tokenize()` - Break into tokens
- `embed()` - Convert to vectors
- `generate_response()` - Get output

**Example:**

```python
def clean_text(text):
    """Remove special characters and lowercase"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

# Usage
user_input = "Hello!!! How are YOU?"
cleaned = clean_text(user_input)
# Output: "hello how are you"
```

**Key takeaway:** Functions make code reusable and organized.

---

### 2️⃣ Lambda Functions (Anonymous Functions)

**Why they matter:**

Common in data transformations and pipelines.

**Example - Text preprocessing:**

```python
# Instead of defining a full function:
messages = ["Hello!", "Hi!!", "Hey!!!"]

# Use lambda for quick transformations:
cleaned = list(map(lambda x: x.replace('!', ''), messages))
# Output: ['Hello', 'Hi', 'Hey']
```

**Real GenAI use case:**

```python
# Applying preprocessing to entire dataset
df['text'] = df['text'].apply(lambda x: x.lower().strip())
```

**When to use:**

- ✅ Quick, one-line transformations
- ✅ Inside map(), filter(), apply()
- ❌ Complex logic (use regular functions)

---

### 3️⃣ Exception Handling (try-except-finally)

**Why critical in GenAI:**

GenAI apps deal with:

- 📁 File uploads (may fail)
- 🌐 API calls (network issues)
- 👤 User inputs (unpredictable)

**Your app must not crash!**

**Example - API call handling:**

```python
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    result = response['choices'][0]['message']['content']

except openai.error.RateLimitError:
    result = "API rate limit exceeded. Please try again."

except openai.error.APIError as e:
    result = f"API error occurred: {str(e)}"

finally:
    # Always log the attempt
    log_request(user_input)
```

**Key pattern:**

```python
try:
    # Attempt risky operation
except SpecificError:
    # Handle known errors
except Exception as e:
    # Catch-all for unexpected errors
finally:
    # Cleanup (always runs)
```

---

### 4️⃣ File Handling

**Why essential:**

GenAI workflows involve:

- 📖 Reading datasets (CSV, JSON, TXT)
- 💾 Saving embeddings / models
- 📝 Logging outputs
- ⚙️ Loading configurations

**Common file operations:**

```python
# Reading text files
with open('data.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Reading line by line (memory efficient)
with open('large_dataset.txt', 'r') as file:
    for line in file:
        process_line(line)

# Writing outputs
with open('results.txt', 'w') as file:
    file.write(generated_text)

# JSON for structured data
import json

with open('config.json', 'r') as file:
    config = json.load(file)
```

**Pro tip:** Always use `with` statement - it automatically closes files!

---

### 5️⃣ List Comprehensions

**Why they're everywhere in NLP:**

Cleaner, faster than loops for transformations.

**Example - Text cleaning:**

```python
# Instead of this:
cleaned_words = []
for word in words:
    if word not in stopwords:
        cleaned_words.append(word.lower())

# Write this:
cleaned_words = [word.lower() for word in words if word not in stopwords]
```

**Real NLP example:**

```python
# Tokenize multiple sentences
sentences = ["Hello world", "Python is great", "GenAI rocks"]
tokenized = [sent.split() for sent in sentences]
# Output: [['Hello', 'world'], ['Python', 'is', 'great'], ['GenAI', 'rocks']]

# Filter short words
long_words = [word for word in words if len(word) > 3]
```

**Syntax:**

```python
[expression for item in iterable if condition]
```

---

### 6️⃣ Essential Libraries Overview

You don't need mastery yet - just understand **why they exist:**

| Library        | Purpose                | GenAI Use Case                 |
| -------------- | ---------------------- | ------------------------------ |
| **NumPy**      | Numerical computation  | Vector operations, matrix math |
| **Pandas**     | Data manipulation      | Loading/cleaning datasets      |
| **OS**         | File & path operations | Navigate folders, check files  |
| **re** (regex) | Pattern matching       | Text cleaning, extraction      |
| **json**       | JSON handling          | API responses, configs         |
| **requests**   | HTTP requests          | API calls to LLMs              |

**Installation:**

```bash
pip install numpy pandas
```

**Quick examples:**

```python
# NumPy - Vector operations
import numpy as np
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
similarity = np.dot(vector1, vector2)  # Dot product

# Pandas - Load CSV dataset
import pandas as pd
df = pd.read_csv('spam.csv')
print(df.head())

# OS - Check if file exists
import os
if os.path.exists('model.pkl'):
    load_model()
```

---

## 🔄 Python in a Typical GenAI Pipeline

```python
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from transformers import pipeline

# 1. File Handling - Load data
df = pd.read_csv('user_inputs.csv')

# 2. Function - Define preprocessing
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

# 3. Lambda + List Comprehension - Apply to all
df['clean_text'] = df['text'].apply(lambda x: preprocess(x))

# 4. Exception Handling - Safe API call
try:
    generator = pipeline('text-generation', model='gpt2')
    results = generator(df['clean_text'].tolist())
except Exception as e:
    print(f"Error: {e}")
    results = []

# 5. File Handling - Save results
with open('outputs.txt', 'w') as f:
    for result in results:
        f.write(result['generated_text'] + '\n')
```

**See how everything connects?**

---

## 🎯 What You DON'T Need (Yet)

❌ Object-Oriented Programming (classes) - Covered later if needed  
❌ Advanced decorators - Not essential for beginners  
❌ Multithreading - Optional optimization  
❌ GUI development - GenAI is often API-based

**Focus on the essentials first!**

---

## ✅ Practice Exercises

### Exercise 1: Text Cleaner

```python
# Write a function that:
# 1. Converts to lowercase
# 2. Removes punctuation
# 3. Splits into words
# 4. Filters words shorter than 3 characters

def clean_and_filter(text):
    # Your code here
    pass

# Test
text = "Hello!!! This is a TEST. AI is great!"
# Expected output: ['hello', 'this', 'test', 'great']
```

### Exercise 2: Safe File Reader

```python
# Write a function that:
# 1. Tries to read a file
# 2. Returns content if successful
# 3. Returns error message if file doesn't exist
# 4. Handles encoding errors

def safe_read_file(filename):
    # Your code here
    pass
```

### Exercise 3: Dataset Transformer

```python
# Given a list of sentences:
sentences = [
    "I love Python!",
    "GenAI is amazing.",
    "NLP is fun!!!"
]

# Use list comprehension to:
# 1. Remove all punctuation
# 2. Convert to lowercase
# 3. Split into words

# Your code here (1-2 lines)
```

---

## 🔑 Key Takeaways

1. **Python is a tool**, not the goal - Learn only what you need for GenAI
2. **Functions** organize your preprocessing pipelines
3. **Exception handling** prevents crashes in production
4. **File handling** is essential for data workflows
5. **List comprehensions** make NLP code cleaner
6. **Libraries** (NumPy, Pandas) power AI/ML operations

---

## ✅ Self-Check

Before moving on, make sure you can:

- [ ] Write a function to clean text
- [ ] Use try-except to handle errors
- [ ] Read and write files safely
- [ ] Use list comprehensions for transformations
- [ ] Understand why NumPy and Pandas are important

**Ready?** Move to the next chapter! 🚀

---

## 🎯 What's Next?

Now you have Python basics. Time to learn how machines understand language!

**Next Chapter:** [03 - NLP Fundamentals](../03-nlp-fundamentals/README.md)

**What you'll learn:** How to convert text into numbers that machines can process

---

## 📚 Additional Resources

**If you want deeper Python knowledge:**

- [Python Official Docs](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science)

**But remember:** GenAI expertise > Python expertise for this bootcamp!

---

_Previous: [01 - Foundations](../01-foundations/README.md) | Next: [03 - NLP Fundamentals](../03-nlp-fundamentals/README.md)_
