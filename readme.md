# README: URL Crawling Methods

## Background
I wrote a simple Python parser to crawl links up to **three levels deep**.  
I tried three methods:

1. **for-for-for** – hardcoded triple loop  
2. **Recursion (DFS)**  
3. **Breadth-First Search (BFS)**  

---

## Comparison

- **for-for-for**  
  Works but fixed at 3 levels, not flexible.  
  Output count: medium.  

- **Recursion (DFS)**  
  Cleaner and supports any depth.  
  Marks URLs early, so some deeper branches are skipped.  
  Output count: smallest.  

- **BFS**  
  Traverses level by level.  
  Marks URLs late, so some are enqueued multiple times.  
  Output count: largest.  

👉 Best improvement: mark URLs as visited **when enqueuing** in BFS.  

---

## Personal Notes
At first, I tried a simple nested loop, but it wasn’t efficient.  
Recursion made the code cleaner and more flexible for different depths.  
Then I implemented BFS, which is more systematic and can be more efficient, though it produced many more results due to delayed pruning.  

The current solution is basic: it just prints results, without logging or domain filtering. Performance could be improved with `requests.Session`, and additional features like error handling and rate limiting could make it more robust.  

This was mainly a practice exercise.  

References:  
- [Extract all the URLs from a webpage using Python](https://www.geeksforgeeks.org/python/extract-all-the-urls-from-the-webpage-using-python/)  
- [Web crawling using BFS at a specified depth](https://www.geeksforgeeks.org/python/web-crawling-using-breadth-first-search-at-a-specified-depth/)  
