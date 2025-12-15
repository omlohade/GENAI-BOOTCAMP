# 📚 ML for NLP - Quick Reference Guide

> **One-page cheat sheet for quick revision**

---

## 🔄 The Complete NLP Pipeline

```
📝 Raw Text
    ↓
🔪 Tokenization (split into words/sentences)
    ↓
🧹 Lowercase + Remove special chars
    ↓
🚫 Remove Stopwords (is, the, a, an)
    ↓
✂️ Stemming/Lemmatization (reduce to root)
    ↓
🔢 Vectorization (convert to numbers)
    ↓
🤖 ML Model Ready!
```

---

## 🔑 Key Concepts at a Glance

### 1. Tokenization

| Type     | Input     | Output            | Use                |
| -------- | --------- | ----------------- | ------------------ |
| Sentence | Paragraph | List of sentences | Document splitting |
| Word     | Text      | List of words     | Feature extraction |

**Tool**: `sent_tokenize()`, `word_tokenize()`

---

### 2. Stemming vs Lemmatization

| Aspect       | Stemming                | Lemmatization        |
| ------------ | ----------------------- | -------------------- |
| **Output**   | Stem (may not be valid) | Dictionary word ✅   |
| **Speed**    | Fast ⚡                 | Slower 🐢            |
| **Accuracy** | Low                     | High ✅              |
| **Example**  | history → histori ❌    | history → history ✅ |
| **Use case** | Spam detection, search  | Chatbots, QA systems |

**Best Stemmer**: Snowball > Porter  
**Lemmatization requires**: POS tag for accuracy!

---

### 3. Stopwords

**What**: Common words (is, am, the, a, an, of, in)

**Why remove**: Reduce noise, decrease feature space

**⚠️ Warning**: Don't remove words like "not" in sentiment analysis!

**Tool**: `stopwords.words('english')`

---

### 4. POS Tagging

**Purpose**: Assign grammar labels (noun, verb, adjective)

**Common Tags**:

- NN = Noun
- VB = Verb
- JJ = Adjective
- RB = Adverb
- NNP = Proper Noun

**Why important**: Needed for accurate lemmatization!

**Tool**: `pos_tag(words)`

---

### 5. Named Entity Recognition (NER)

**Purpose**: Find real-world entities

**Common Entities**:

- PERSON → Elon Musk
- GPE → India, France
- ORGANIZATION → Google, Microsoft
- DATE → 2024, January 1st
- MONEY → $1 million

**Tool**: `ne_chunk(pos_tagged_words)`

**Difference from POS**: POS = grammar, NER = meaning

---

## 🔢 Vectorization Methods

### Bag of Words (BoW)

**Concept**: Count word frequencies

**Types**:

- Binary: Present=1, Absent=0
- Count: Actual frequency

**Pros**: Simple, fast  
**Cons**: No word order, equal weights

**Code**: `CountVectorizer()`

---

### TF-IDF

**Formula**: TF × IDF

```
TF = Word count in doc / Total words in doc
IDF = log(Total docs / Docs containing word)
```

**Key Insight**: Common words → low weight, Rare words → high weight

**Pros**: Better than BoW, weights important words  
**Cons**: Still sparse

**Code**: `TfidfVectorizer()`

---

### N-Grams

**Purpose**: Capture word sequences (context)

**Types**:

- Unigram (1,1): Single words → `good`
- Bigram (2,2): Word pairs → `not good`
- Trigram (3,3): 3-word sequences → `food not good`
- Mixed (1,2): Unigrams + Bigrams ✅

**Why needed**: "food is good" ≠ "food is not good"

**Code**: `CountVectorizer(ngram_range=(1,2))`

---

### Word2Vec 🌟

**Concept**: Dense vectors that capture semantic meaning

**Magic**: `king - man + woman ≈ queen`

**Types**:

- **CBOW**: Context → Center word (faster)
- **Skip-Gram**: Center word → Context (better accuracy)

**Dimensions**: Usually 300-d vectors

**Similarity**: Cosine similarity (0 = unrelated, 1 = same)

**Pros**:

- Captures meaning ✅
- Dense vectors ✅
- Word relationships ✅

**Tool**: `gensim.downloader.load('word2vec-google-news-300')`

**Average Word2Vec**: Average all word vectors in a sentence to get one sentence vector

---

## 📊 When to Use What?

| Task                | Best Method              | Why                     |
| ------------------- | ------------------------ | ----------------------- |
| Spam Detection      | TF-IDF, BoW              | Simple, effective       |
| Sentiment Analysis  | Word2Vec                 | Understands good vs bad |
| Chatbots            | Lemmatization + Word2Vec | Needs meaning           |
| Search Engine       | Stemming + TF-IDF        | Speed matters           |
| Text Classification | TF-IDF or Word2Vec       | Depends on data size    |
| Document Similarity | TF-IDF or Word2Vec       | Both work well          |

---

## 🎯 Decision Tree

```
Do you need semantic meaning?
│
├─ NO → Use TF-IDF
│   └─ Fast, effective for classification
│
└─ YES → Use Word2Vec
    └─ Best for understanding relationships
```

---

## ⚡ Quick Code Snippets

### Complete Preprocessing

```python
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    # Tokenize
    words = word_tokenize(text.lower())

    # Remove stopwords & lemmatize
    words = [lemmatizer.lemmatize(w, pos='v')
             for w in words
             if w not in stop_words and w.isalpha()]

    return ' '.join(words)
```

### TF-IDF Vectorization

```python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ["text 1", "text 2", "text 3"]
vectorizer = TfidfVectorizer(max_features=100, ngram_range=(1,2))
X = vectorizer.fit_transform(corpus).toarray()
```

### Word2Vec Similarity

```python
import gensim.downloader as api

model = api.load('word2vec-google-news-300')
similarity = model.similarity('king', 'queen')
similar_words = model.most_similar('happy', topn=5)
```

---

## 🧠 Must Remember

1. **Tokenization is the foundation** - Nothing works without it
2. **Lemmatization > Stemming** for accuracy
3. **Always remove stopwords carefully** - Some words matter!
4. **POS tagging improves lemmatization**
5. **Word2Vec captures meaning** - Best for semantic tasks
6. **TF-IDF is faster** - Good for classification
7. **N-grams capture context** - Use (1,2) for best results
8. **Average Word2Vec** - Converts word vectors → sentence vector

---

## 🔗 Library Cheat Sheet

| Library     | Purpose                           |
| ----------- | --------------------------------- |
| **nltk**    | Tokenization, POS, NER, Stopwords |
| **sklearn** | BoW, TF-IDF, ML models            |
| **gensim**  | Word2Vec, embeddings              |
| **spaCy**   | Production NLP (faster than nltk) |

---

## 📝 Common Mistakes to Avoid

❌ Forgetting to lowercase  
❌ Not removing stopwords  
❌ Using stemming when lemmatization is needed  
❌ Not specifying POS tag in lemmatization  
❌ Removing "not" in sentiment analysis  
❌ Using BoW when context matters  
❌ Training Word2Vec on small datasets

---

**🎓 You're now ready for Deep Learning NLP!**

_Next: RNNs, LSTMs, Transformers, BERT, GPT → GenAI_ 🚀
