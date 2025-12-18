# DOM Parsing

## What is DOM?

Document Object Model - tree structure representing HTML elements.

## HTML → DOM Tree

```html
<div class="job">
  <h2>Software Engineer</h2>
  <span class="company">TechCorp</span>
</div>
```

Becomes:

```
div.job
  ├── h2 (text: "Software Engineer")
  └── span.company (text: "TechCorp")
```

## Selectors

**CSS Selectors** (BeautifulSoup, Playwright):

- `.class-name` - select by class
- `#id-name` - select by ID
- `tag` - select by tag name
- `div > span` - direct child
- `div span` - any descendant

**XPath** (Advanced):

- `//div[@class="job"]` - div with class "job"
- `//h2/text()` - text content of h2

## Why Parsing Matters

- **Data extraction**: Find specific elements (titles, prices)
- **Navigation**: Move between parent/child/sibling nodes
- **Validation**: Check if expected elements exist
- **Robustness**: Handle missing elements gracefully
