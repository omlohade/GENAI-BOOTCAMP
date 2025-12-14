# 03 – NLP Fundamentals

Generative AI works with **language**.

Machines do NOT understand language naturally.
They only understand **numbers**.

NLP is the bridge between:

> Human language → Machine numbers

---

## 📘 Important NLP Terminology

### Corpus

A corpus is a **collection of text**.
It can be:

- A paragraph
- A document
- Multiple documents

---

### Document

A document is usually:

- One sentence
- One message
- One email

---

### Vocabulary

Vocabulary = all **unique words** in the corpus.

Example:
"I like apple juice. I like mango juice."

Vocabulary:
`I, like, apple, mango, juice`

---

## 🔹 Tokenization

Tokenization = breaking text into smaller units.

### Types:

1. Paragraph → Sentences
2. Sentence → Words

Example:

```
"I love NLP."
→ ["I", "love", "NLP"]
```

Each token becomes a **unit for processing**.

---

## ❓ Why Tokenization Matters

GenAI models:

- Don't read sentences
- Don't read paragraphs

They process:

- Tokens
- Vectors
- Embeddings

Tokenization is the **first mandatory step**.

---

## ✅ Key Takeaway

If you don't understand tokenization,
you will NEVER understand GenAI internals.
