# Quick Reference - NLP in Deep Learning

## 🎯 One-Liner Definitions

| Term                   | Definition                                                     |
| ---------------------- | -------------------------------------------------------------- |
| **Sequential Data**    | Data where order matters (text, time-series)                   |
| **RNN**                | Neural network with feedback loop for sequential data          |
| **BPTT**               | Backpropagation Through Time - training RNNs across time steps |
| **Vanishing Gradient** | Gradients become too small, stopping learning                  |
| **Gradient**           | Rate of change of loss w.r.t. weights                          |
| **LSTM**               | Long Short-Term Memory - RNN variant with gates                |
| **GRU**                | Gated Recurrent Unit - simpler LSTM alternative                |

---

## 📊 ANN vs RNN

| Feature              | ANN | RNN |
| -------------------- | --- | --- |
| Handles sequence     | ❌  | ✅  |
| Memory               | ❌  | ✅  |
| NLP tasks            | ❌  | ✅  |
| Time-step processing | ❌  | ✅  |

---

## 🔑 Key Formulas

### RNN Forward Pass

```
oₜ = tanh(xₜ · Wᵢ + oₜ₋₁ · Wₕ + b)
```

### Weight Update

```
W_new = W_old − η · (∂Loss / ∂W_old)
```

---

## 🎓 RNN Problems & Solutions

| Problem              | Solution               |
| -------------------- | ---------------------- |
| Vanishing Gradient   | LSTM / GRU             |
| Long-term dependency | LSTM / GRU             |
| Slow training        | GRU (faster than LSTM) |
| Exploding Gradient   | Gradient Clipping      |

---

## 🔄 Learning Roadmap

1. Simple RNN ✅
2. LSTM
3. GRU
4. Bidirectional RNN
5. Encoder-Decoder
6. Attention Mechanism
7. Transformers
8. LLMs

---

## 💡 Interview Quick Points

### Why RNN over ANN for NLP?

- **Order matters in text**
- **ANN loses sequence information**
- **RNN processes word-by-word**
- **RNN has memory (hidden state)**

### Why LSTM over Simple RNN?

- **Solves vanishing gradient**
- **Handles long-term dependencies**
- **Uses gates (forget, input, output)**
- **Better for real-world NLP**

### What is Gradient?

- **Direction to update weights**
- **Rate of change of loss**
- **Used in gradient descent**

---

## 📋 RNN Weights

| Weight | Flow            | Purpose         |
| ------ | --------------- | --------------- |
| Wᵢ     | Input → Hidden  | Process input   |
| Wₕ     | Hidden → Hidden | Memory/Context  |
| Wₒ     | Hidden → Output | Generate output |

---

## ⚡ Quick Revision

**10-Second Summary:**

- Text is sequential → order matters
- ANN can't handle sequences
- RNN processes step-by-step with memory
- RNN has vanishing gradient problem
- LSTM/GRU solve this

**30-Second Summary:**
Traditional NLP used BoW, TF-IDF, Word2Vec with ML models. But text is sequential - order matters. ANN can't handle this because it processes all words at once and has no memory. RNN solves this by processing words step-by-step and maintaining hidden state. However, simple RNN suffers from vanishing gradient, making it forget long-term context. LSTM and GRU solve this using gate mechanisms.

---

## 🎯 Exam-Perfect Answers

### Q: Why can't ANN handle NLP?

**A:** ANN treats inputs as independent features and processes entire input at once, losing sequence information. In NLP, word order and context are crucial. ANN has no memory mechanism to track previous words, making it unsuitable for language tasks.

### Q: What is vanishing gradient?

**A:** Vanishing gradient occurs when gradients become extremely small during backpropagation through many time steps. This causes earlier time steps to contribute almost nothing to learning, making the model unable to capture long-term dependencies.

### Q: How does RNN maintain context?

**A:** RNN maintains context through hidden state that is passed from one time step to the next. At each step, the hidden state combines current input with previous hidden state, creating a memory of past information.

---

## 🔢 Types of Data & Models

| Data Type   | Model    | Examples                               |
| ----------- | -------- | -------------------------------------- |
| Tabular     | ANN      | Price prediction, classification       |
| Image/Video | CNN      | Object detection, image classification |
| Sequential  | RNN/LSTM | NLP, time-series, translation          |

---

## 💻 Use Cases

### RNN Applications

- Text generation
- Machine translation
- Sentiment analysis
- Chatbots
- Speech recognition
- Time-series forecasting
- Auto-suggestions

---

## ⚠️ Common Mistakes to Avoid

1. ❌ Using ANN for sequential data
2. ❌ Ignoring vanishing gradient in simple RNN
3. ❌ Not normalizing gradients (exploding gradient)
4. ❌ Using very deep simple RNN (use LSTM instead)
5. ❌ Forgetting that same weights are reused across time steps

---

## 🎨 Visual Memory Aids

### RNN Flow

```
t1: "The"    → h1 →
t2: "food"   → h2 → (remembers "The")
t3: "is"     → h3 → (remembers "The food")
t4: "good"   → h4 → (remembers "The food is")
```

### BPTT Flow

```
Forward: Input → Hidden → Output
Backward: Loss ← Hidden ← All time steps
```

---

**Remember:** This is just the foundation. Real-world NLP uses Transformers (BERT, GPT), which we'll cover later!
