# 03 – NLP Fundamentals 📝

> **The bridge between human language and machine understanding**

---

## 🎯 The Core Challenge

```
┌─────────────────────────────────────┐
│  The Fundamental Problem            │
└─────────────────────────────────────┘

Humans understand: Words, sentences, meaning
Machines understand: Only numbers (0s and 1s)

How do we bridge this gap? → NLP!
```

**Natural Language Processing (NLP)** is the technology that makes GenAI possible.

---

## 🌉 NLP: The Bridge

```
Human Language                    Machine Language
     │                                  │
     │  "I love learning AI"            │
     ↓                                  ↓
┌──────────────┐              ┌──────────────┐
│  Words       │    NLP       │  Numbers     │
│  Sentences   │  ────────→   │  Vectors     │
│  Meaning     │              │  Matrices    │
└──────────────┘              └──────────────┘
```

**Without NLP, GenAI cannot exist!**

---

## 📘 Essential NLP Terminology

### 1️⃣ Corpus

**Definition:** A collection of text documents

**Think of it as:** Your entire dataset

**Examples:**

- All tweets from a user
- Complete works of Shakespeare
- Customer reviews for a product
- News articles from 2024

**Code example:**

```python
corpus = """
I love Python. Python is great for AI.
GenAI is transforming the world.
NLP makes GenAI possible.
"""
```

---

### 2️⃣ Document

**Definition:** A single unit of text within a corpus

**Typically:**

- One sentence
- One email
- One review
- One article paragraph

**Example breakdown:**

```python
corpus = "I love AI. AI is amazing."

documents = [
    "I love AI.",      # Document 1
    "AI is amazing."   # Document 2
]
```

**Why it matters:** ML models process documents separately, then learn from all of them.

---

### 3️⃣ Vocabulary (Vocab)

**Definition:** Set of all **unique words** in your corpus

**Example:**

```
Corpus: "I like apple juice. I like mango juice."

Vocabulary: {I, like, apple, juice, mango}
(5 unique words, even though corpus has 10 words total)
```

**Why important:** Vocabulary size directly affects:

- Model complexity
- Memory requirements
- Training time

**Vocabulary in real models:**

- GPT-3: ~50,000 tokens
- BERT: ~30,000 tokens

---

### 4️⃣ Token

**Definition:** The smallest unit of text that the model processes

**Tokens can be:**

- Words → `["Hello", "world"]`
- Subwords → `["un", "##believable"]`
- Characters → `["H", "e", "l", "l", "o"]`

**Modern LLMs use subword tokens** (best of both worlds!)

---

## 🔹 Tokenization - The Foundation

**Tokenization** = Breaking text into smaller units (tokens)

### Why Tokenization is Critical:

```
❌ Without Tokenization:
"Hello world" → Cannot process → Stuck!

✅ With Tokenization:
"Hello world" → ["Hello", "world"] → Can process!
```

---

### Types of Tokenization

#### 1. Sentence Tokenization

**Paragraph → Sentences**

```python
text = "I love AI. It's amazing! NLP is fun."
sentences = ["I love AI.", "It's amazing!", "NLP is fun."]
```

#### 2. Word Tokenization

**Text → Words**

```python
text = "I love NLP"
tokens = ["I", "love", "NLP"]
```

#### 3. Subword Tokenization (Used in GPT, BERT)

**Words → Subwords**

```python
word = "unbelievable"
tokens = ["un", "##believ", "##able"]
```

**Why subwords?**

- Handles rare words ✅
- Reduces vocabulary size ✅
- Better generalization ✅

---

## 🔄 The NLP Pipeline (Simplified)

```
Step 1: Raw Text
    "I LOVE learning GenAI!!!"
    ↓
Step 2: Cleaning
    "i love learning genai"
    ↓
Step 3: Tokenization
    ["i", "love", "learning", "genai"]
    ↓
Step 4: Removing Stopwords
    ["love", "learning", "genai"]
    ↓
Step 5: Stemming/Lemmatization
    ["love", "learn", "genai"]
    ↓
Step 6: Vectorization (Text → Numbers)
    [0.2, 0.8, 0.3, ...] (Vector representation)
    ↓
Step 7: Feed to Model
    ML/DL model can now process!
```

**Each step is covered in detail in Chapter 05!**

---

## ❓ Why Tokenization Matters for GenAI

### GenAI Models Don't Read Like Humans

**Humans:**

- Read full sentences
- Understand context instantly
- Process meaning holistically

**GenAI Models:**

- Process one token at a time
- Build context incrementally
- Work with token probabilities

**Example - How ChatGPT generates text:**

```
Prompt: "Write a poem about"

Token 1: "the" (highest probability)
Token 2: "moon" (given "the")
Token 3: "shines" (given "the moon")
Token 4: "bright" (given "the moon shines")
...and so on
```

Each token is predicted based on previous tokens!

---

## 🔢 From Text to Numbers (Preview)

### The Transformation Journey:

```
Text:    "I love AI"
   ↓
Tokens:  ["I", "love", "AI"]
   ↓
IDs:     [42, 1337, 89] (Token IDs from vocabulary)
   ↓
Vectors: [[0.1, 0.5, 0.2],
          [0.8, 0.3, 0.6],
          [0.4, 0.7, 0.9]]
   ↓
Numbers that models understand! ✅
```

**This is covered in depth in Chapter 05: ML for NLP**

---

## 🧠 Key NLP Concepts (Quick Reference)

| Term             | What It Is              | Example                    |
| ---------------- | ----------------------- | -------------------------- |
| **Corpus**       | Collection of documents | All customer reviews       |
| **Document**     | Single text unit        | One review                 |
| **Vocabulary**   | Unique words            | {good, bad, product, love} |
| **Token**        | Smallest unit           | "love", "AI", "##ing"      |
| **Tokenization** | Splitting text          | "Hello" → ["Hello"]        |
| **Embedding**    | Word as vector          | "king" → [0.2, 0.8, ...]   |

---

## 🎯 Why This Matters for GenAI

### ChatGPT's Secret (Simplified):

1. **Takes your text** → Tokenizes it
2. **Converts to vectors** → Numbers the model understands
3. **Processes through layers** → Neural network magic
4. **Predicts next token** → Probability distribution
5. **Converts back to text** → Human-readable output

**Every step relies on NLP fundamentals!**

---

## 📊 NLP vs Traditional Programming

| Traditional Code                       | NLP Approach                               |
| -------------------------------------- | ------------------------------------------ |
| `if word == "good": return "positive"` | Learn from 1M examples → predict sentiment |
| Hardcoded rules                        | Learned patterns                           |
| Breaks on new words                    | Handles unseen words                       |
| No context understanding               | Context-aware                              |

---

## ✅ Real-World NLP Applications

| Application            | NLP Task                                   |
| ---------------------- | ------------------------------------------ |
| **ChatGPT**            | Text generation (next token prediction)    |
| **Google Translate**   | Sequence-to-sequence (language → language) |
| **Spam Filter**        | Text classification (spam vs ham)          |
| **Autocomplete**       | Next word prediction                       |
| **Voice Assistants**   | Speech → Text → Understanding → Response   |
| **Sentiment Analysis** | Classify emotion (positive/negative)       |

**All powered by the fundamentals you're learning here!**

---

## 🔑 Key Takeaways

1. **NLP bridges human language and machine numbers**
2. **Corpus** = all text, **Document** = one text, **Vocabulary** = unique words
3. **Tokenization is mandatory** - Can't process text without it
4. **Tokens become vectors** - That's how machines "understand"
5. **Modern LLMs use subword tokenization** - Best balance

---

## ✅ Self-Check Questions

Before moving to the next chapter:

- [ ] Can you explain why machines can't understand text directly?
- [ ] What's the difference between corpus and document?
- [ ] Can you tokenize a sentence manually?
- [ ] Do you understand why vocabulary size matters?
- [ ] Can you explain tokenization to a friend?

**All yes?** You're ready! 🚀

---

## 🎯 What's Next?

You now understand the fundamentals. Time to see the big picture!

**Next Chapter:** [04 - GenAI Overview](../04-genai-overview/README.md)

**What you'll learn:** How all the pieces fit together in GenAI systems

---

## 💡 Pro Tip

The concepts here seem simple, but they're **critical**.

When you get to Chapter 05 (ML for NLP), you'll see these concepts in action with real code. Everything will click! 💡

---

_Previous: [02 - Python Basics](../02-python-basics/README.md) | Next: [04 - GenAI Overview](../04-genai-overview/README.md)_
