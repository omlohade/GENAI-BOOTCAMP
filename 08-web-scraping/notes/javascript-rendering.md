# JavaScript Rendering

## The Problem

Modern websites use JavaScript to load content AFTER page loads.

## Static HTML (requests sees this):

```html
<div id="jobs-container">
  <!-- Empty! -->
</div>
<script src="app.js"></script>
```

## After JS Execution (browser sees this):

```html
<div id="jobs-container">
  <div class="job">Software Engineer</div>
  <div class="job">Data Scientist</div>
</div>
```

## Why requests Fails

1. Sends HTTP request
2. Gets HTML response
3. Doesn't execute JavaScript
4. Sees empty container

## Solution: Browser Automation

**Playwright/Selenium**:

1. Launch real browser (Chromium, Firefox)
2. Load page fully
3. Execute JavaScript
4. Wait for elements to appear
5. Extract rendered content

## When to Use Each

- **requests**: Faster, lighter (if data is in HTML source)
- **Playwright**: Slower, heavier (if data loaded by JS)

**Test**: View Page Source (Ctrl+U). If you see data → use requests. If empty → use Playwright.
