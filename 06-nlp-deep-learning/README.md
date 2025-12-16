# 06 - NLP in Deep Learning

## 📚 Chapter Overview

This chapter introduces deep learning approaches for Natural Language Processing (NLP), explaining why sequential models are necessary and how they differ from traditional ML-based NLP techniques.

## 📋 Table of Contents

1. [What We Learned Till Now](#1-what-we-learned-till-now)
2. [Why Move to Deep Learning for NLP](#2-why-move-to-deep-learning-for-nlp)
3. [Types of Data & Neural Networks](#3-types-of-data--neural-networks)
4. [Sequential Data Explained](#4-sequential-data-explained)
5. [NLP Deep Learning Use Cases](#5-nlp-deep-learning-use-cases)
6. [Why ANN Fails for NLP](#6-why-ann-fails-for-nlp)
7. [Introduction to RNN](#7-introduction-to-rnn)
8. [RNN Backpropagation Through Time](#8-rnn-backpropagation-through-time)
9. [RNN Problems](#9-rnn-problems)
10. [Understanding Gradients](#10-understanding-gradients)

---

## 1. What We Learned Till Now

### ML-Based NLP Recap

Earlier NLP techniques focused on converting **text → vectors**:

- **One-Hot Encoding**
- **Bag of Words (BoW)**
- **TF-IDF**
- **Word2Vec**
- **Average Word2Vec**

👉 These methods were mainly used with **Machine Learning models** for:

- Sentiment Analysis
- Text Classification

---

## 2. Why Move to Deep Learning for NLP?

### Because text is SEQUENTIAL data

👉 **Meaning of a sentence depends on word order**

**Example:**

- ✅ "The food is good"
- ❌ "Good the food is"

➡️ **Order matters** → ML models struggle here.

---

## 3. Types of Data & Neural Networks

### 🔹 Tabular Data → ANN

**Examples:**

- House price prediction
- Salary prediction

**Key points:**

- Order of features does NOT matter
- ANN works well
- Input = fixed features (F1, F2, …)

### 🔹 Image / Video Data → CNN

**Examples:**

- Image classification
- Object detection (YOLO, etc.)

**Key points:**

- Spatial structure matters
- CNN extracts visual patterns

### 🔹 Sequential Data → NLP / Time Series

**Examples:**

- Text
- Chat conversations
- Language translation
- Email auto-suggestions
- Sales forecasting (time-based)

**Key point:**

- Sequence & context matter
- ANN & CNN are NOT sufficient

---

## 4. Sequential Data Explained

### What is Sequential Data?

**Sequential data = order-dependent data**

**Examples:**

- Sentences
- Chat history
- Time-series sales data

👉 **Changing order changes meaning.**

---

## 5. NLP Deep Learning Use Cases

- Text Generation
- Chatbots
- Language Translation
- Auto-suggestions (Gmail, LinkedIn)
- Time-series forecasting

---

## 6. Why ANN Fails for NLP

### Problem Being Solved

**Task:** Sentiment Analysis

**Example dataset:**

| Sentence             | Output |
| -------------------- | ------ |
| The food is good     | 1      |
| The food is bad      | 0      |
| The food is not good | 0      |

### Text → Vectors (Recap)

To train ML/DL models, text must be converted into vectors.

**Example (Bag of Words):**

**Vocabulary:** `[food, good, bad, not]`

| Sentence      | Vector |
| ------------- | ------ |
| food good     | 1100   |
| food bad      | 1010   |
| food not good | 1101   |

✔ Fixed vector size  
❌ Sequence/order is lost

### ❌ Problem 1: Sequence Information is Lost

ANN treats inputs as independent features, not ordered data.

- "food not good"
- "good food not"

Both may produce same vector, but meanings are different.

➡️ **Context is lost**

### ❌ Problem 2: All Words Passed at Once

In ANN:

- Entire sentence vector is fed in one shot
- No concept of time steps

But language is sequential:

- t1 → "The"
- t2 → "food"
- t3 → "is"
- t4 → "good"

ANN cannot handle:

- Word-by-word processing
- Language translation
- Text generation
- Speech recognition

### Why Sequential Processing is Needed

For NLP tasks:

- Each word depends on previous words
- Context builds over time

**Example:**
"The food is **not** good"

The word "not" changes the entire meaning.

➡️ **Model must remember previous words**

### ANN vs RNN Comparison

| Feature          | ANN             | RNN         |
| ---------------- | --------------- | ----------- |
| Handles sequence | ❌ No           | ✅ Yes      |
| Memory of past   | ❌ No           | ✅ Yes      |
| NLP suitability  | ❌ Poor         | ✅ Good     |
| Time-step input  | ❌ No           | ✅ Yes      |
| Language tasks   | ❌ Not suitable | ✅ Suitable |

---

## 7. Introduction to RNN

### 🔁 What is RNN?

**RNN** (Recurrent Neural Network) is a neural network with a **feedback loop**.

**Key idea:**

- Hidden state at time `t` depends on:
  - Input at time `t`
  - Previous hidden state

### RNN Architecture Concept

At each time step:

```
Input (Xt) → Hidden State (Ht) → Output (Yt)
               ↑
          Previous H(t-1)
```

- Same hidden layer reused at every time step
- Remembers past information (context)

### How RNN Processes a Sentence

**Sentence:** "The food is good"

| Time Step | Input |
| --------- | ----- |
| t1        | The   |
| t2        | food  |
| t3        | is    |
| t4        | good  |

At:

- **t2** → model knows "The"
- **t3** → model knows "The food"
- **t4** → model knows "The food is"

➡️ **Context preserved** ✔

### RNN Recap

- RNN processes sequence data word-by-word (time step by time step)
- Same weights are reused across time
- Output at time `t` depends on:
  - Current input `xₜ`
  - Previous hidden state `oₜ₋₁`

---

## 8. RNN Backpropagation Through Time

### 🔁 What is BPTT?

**BPTT** = Backpropagation in RNN across time steps

➡️ RNN processes data step by step (time-wise)  
➡️ During training, error is sent back from last step to first step

### Why "Through Time"?

Because:

- Same RNN repeats at every time step
- Same weights are used again and again
- So error must flow back through all time steps

### RNN Has 3 Weights

| Weight | Purpose                  |
| ------ | ------------------------ |
| Wᵢ     | Input → Hidden           |
| Wₕ     | Hidden → Hidden (memory) |
| Wₒ     | Hidden → Output          |

### Forward Propagation

For time step `t`:

**Hidden state:**

```
oₜ = tanh(xₜ · Wᵢ + oₜ₋₁ · Wₕ + b)
```

**Final output:**

```
ŷ = sigmoid(o_T · Wₒ)   # binary
ŷ = softmax(o_T · Wₒ)   # multiclass
```

Where:

- `Wᵢ` → input weights
- `Wₕ` → hidden (recurrent) weights
- `Wₒ` → output weights
- `b` → bias

### Training Flow

**Step 1: Forward Pass**

- Input words go one by one
- Hidden state updates each time
- Final output is produced

**Step 2: Loss Calculation**

- Compare predicted output with actual output
- Find error (loss)

**Step 3: Backward Pass (BPTT)**

- Error goes backwards
- Starts from last time step
- Updates all 3 weights

### Weight Update Rule

General formula:

```
W_new = W_old − η · (∂Loss / ∂W_old)
```

Where: `η` = learning rate

### How Weights Are Updated

**Output weight (Wₒ):**

- Updated using final output error

**Hidden weight (Wₕ):**

- Updated using errors from all time steps
- Same weight updated many times

**Input weight (Wᵢ):**

- Updated using error flowing back to inputs

### Updating Hidden Weights (Wₕ)

`Wₕ` affects ALL time steps, so gradients are summed across time.

For T=3 example:

```
∂L/∂Wₕ =
  (∂L/∂ŷ · ∂ŷ/∂o₃ · ∂o₃/∂Wₕ)
+ (∂L/∂ŷ · ∂ŷ/∂o₃ · ∂o₃/∂o₂ · ∂o₂/∂Wₕ)
+ (∂L/∂ŷ · ∂ŷ/∂o₃ · ∂o₃/∂o₂ · ∂o₂/∂o₁ · ∂o₁/∂Wₕ)
```

👉 Same weight updated using multiple time dependencies

### Key Point to Remember ⭐

**One error** → travels through all time steps → updates same weights repeatedly

---

## 9. RNN Problems

### ❌ Main Problem: Vanishing Gradient

**What is Vanishing Gradient?**

- During backpropagation, gradients become very small
- Earlier time-step words stop influencing learning
- **Result:** RNN forgets old information

### 🧠 Short-Term vs Long-Term Dependency

#### ✅ Short-term dependency (RNN works fine)

**Example:**

```
"I like to play ___"
```

- Next word depends on recent words
- RNN can handle this

#### ❌ Long-term dependency (RNN fails)

**Example:**

```
"My name is Krish ... I like to make ___"
```

- Prediction depends on words far in the past
- RNN cannot remember early words

### 🔬 Why Vanishing Gradient Happens

RNN uses sigmoid / tanh:

- Their derivatives are < 1
- During backpropagation:
  - Gradients are multiplied many times
  - Values → almost zero
  - Earlier words contribute almost nothing

👉 **Older time steps ≈ forgotten**

### 📉 Effect on Learning

- Words near last timestamp matter most
- Words at start of sentence have zero impact
- Model becomes biased toward recent words

### ❗ Key Issues in Simple RNN

- ❌ Cannot capture long-term dependencies
- ❌ Suffers from vanishing gradient
- ❌ Poor accuracy for long sentences
- ❌ Earlier context is ignored

### 🛠️ Partial Fixes (Not Enough)

- Using tanh instead of sigmoid
- Using ReLU / Leaky ReLU

⚠️ Still not a complete solution

### ✅ Proper Solutions

#### 🔹 LSTM (Long Short-Term Memory)

Special gates:

- Forget gate
- Input gate
- Output gate

Benefits:

- Maintains long-term memory
- Solves vanishing gradient

#### 🔹 GRU (Gated Recurrent Unit)

- Simpler than LSTM
- Faster training
- Also handles long-term dependency

---

## 10. Understanding Gradients

### 🌱 What is a Gradient?

👉 **Gradient = direction + amount of change**

In machine learning, a gradient tells the model:

> "In which direction should I change my weights to reduce the error, and how much?"

### 🧠 Real-Life Example

#### 🏔️ Walking down a hill

- You are standing on a hill
- Your goal = reach the lowest point (minimum error)
- The slope of the hill tells you:
  - Which direction is down
  - How steep it is

👉 **That slope = gradient**

### 🤖 Gradient in Machine Learning

**ML goal:** Reduce loss (error)

**How?** Adjust weights

**Gradient tells:**

- ❓ Should weight increase or decrease
- ❓ By how much

### 🧮 Simple Definition

**Gradient is the rate of change of loss with respect to weights.**

OR even simpler:

**Gradient = how much error changes when weight changes**

### 🔁 Why Gradients are Needed

**Without gradients:**

- Model doesn't know how to improve
- Training is blind guessing

**With gradients:**

- Model learns step by step
- Error keeps reducing

### 🔄 Gradient Descent

1. Model predicts output
2. Calculate error (loss)
3. Calculate gradient
4. Update weights: Move opposite to gradient
5. Repeat until error is small

### ⚠️ Vanishing Gradient

- Gradient becomes very small
- Weight updates become almost zero
- Model stops learning

👉 **This is why RNN fails for long sequences**

### 🧠 One-Line Exam Answer

> Gradient is the rate at which the loss changes with respect to model parameters and is used to update weights during training.

---

## 🎯 Roadmap: What Comes Next

You will learn in this order:

1. ✅ **Simple RNN** (Covered in this chapter)
2. **LSTM** (Next)
3. **GRU**
4. **Bidirectional RNN**
5. **Encoder–Decoder Architecture**
6. **Self-Attention**
7. **Transformers**
8. **LLMs & Generative AI**

👉 All modern LLMs (ChatGPT, Gemini, Claude) are based on **Transformers**

---

## 🔥 Why This is IMPORTANT

### For Interviews

- Core foundation for Generative AI
- Asked heavily in ML / AI interviews

### For GenAI

- Required to understand LLMs
- Foundation for modern AI systems

---

## 📝 Key Takeaways

1. **NLP data is sequential**
2. **ANN cannot preserve order**
3. **ANN processes all inputs at once**
4. **RNN processes one word per time step**
5. **RNN maintains context via hidden state**
6. **RNN is the foundation of NLP deep learning**
7. **RNN suffers from vanishing gradient problem**
8. **LSTM and GRU solve the vanishing gradient issue**

---

## 🔗 Next Steps

- Practice implementing Simple RNN
- Understand LSTM architecture
- Learn GRU
- Move to Transformer-based models

---

## 📚 Additional Resources

- [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [Sequence Models Course - deeplearning.ai](https://www.coursera.org/learn/nlp-sequence-models)

---

**Previous Chapter:** [05 - ML for NLP](../05-ML-for-NLP/README.md)  
**Next Chapter:** 07 - ANN Project Implementation (Coming Soon)

---

_Happy Learning! 🚀_
