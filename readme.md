# README: Comparison of Three URL Crawling Methods

## Background
I implemented a simple Python web parser to crawl all links (`<a href>`) from a website up to **three levels deep (max_depth=3)**.  
To explore different traversal strategies, I built three versions:

1. **for-for-for** (hardcoded triple loop)  
2. **Recursion (DFS)**  
3. **Breadth-First Search (BFS)**  

---

## Differences Between the Methods

### 1. for-for-for
- **Approach**: Manually writing three nested `for` loops.  
- **Characteristics**:  
  - Works only for exactly three levels (not extendable).  
  - Marks `visited` at each level, so some branches get cut off early.  
  - Redundant code, not scalable.  
- **Result**: Medium-sized output (177 URLs) — more than recursion, fewer than BFS.  

---

### 2. Recursion (DFS)
- **Approach**: Depth-First Search with recursion.  
- **Characteristics**:  
  - Adds each URL to `visited` immediately when entering.  
  - If a URL was seen at a shallower depth, the entire deeper subtree from that URL is skipped.  
  - This leads to missing many level-3 URLs.  
- **Result**: Smallest output (88 URLs), because many branches were pruned too early.  

---

### 3. Breadth-First Search (BFS)
- **Approach**: Queue-based traversal, level by level.  
- **Characteristics**:  
  - Only adds a URL to `visited` when dequeuing.  
  - If a URL is linked from multiple parents, it may be enqueued multiple times.  
  - This allows exploring more branches, but also inflates the count.  
- **Result**: Largest output (732 URLs).  

---

## Why the Results Differ

1. **DFS prunes too early**  
   - In recursion, `visited.add(url)` happens immediately on entry.  
   - Once a URL is marked, any deeper occurrences of it are skipped, even if they could lead to new children.  
   - Result: fewer URLs.

2. **BFS prunes too late**  
   - In BFS, `visited` is updated when a URL is dequeued.  
   - This means the same URL can be enqueued multiple times from different parents.  
   - Result: more URLs.

3. **for-for-for is limited**  
   - Works only for exactly three levels.  
   - Covers fewer paths than BFS, but doesn’t prune as aggressively as DFS.  
   - Result: middle ground.  

---

## Conclusion
- **DFS (recursion)** → Fewest results, due to early pruning.  
- **BFS** → Most results, due to late pruning.  
- **for-for-for** → Middle results, but not extensible.  

👉 For collecting **unique level-3 URLs**, the best practice is to improve BFS by marking URLs as visited **when enqueuing**, not when dequeuing.  
This avoids both early pruning and duplicate exploration.  
