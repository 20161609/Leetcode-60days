# Notes

## Link
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

## Approach
1. Always binary-search on the **shorter** array (`nums1`). If not, swap the arrays.
2. Let `i` be the cut in `nums1` and `j = (n1 + n2 + 1)//2 - i` be the cut in `nums2` so that  
   the **left half has exactly** `(n1+n2+1)//2` elements.
3. Define boundary values to avoid out-of-range:
   - `maxLeft1 = -inf` if `i == 0` else `nums1[i-1]`
   - `minRight1 = +inf` if `i == n1` else `nums1[i]`
   - `maxLeft2 = -inf` if `j == 0` else `nums2[j-1]`
   - `minRight2 = +inf` if `j == n2` else `nums2[j]`
4. Check the **partition condition**:
   - If `maxLeft1 <= minRight2` **and** `maxLeft2 <= minRight1`, the partition is valid.  
     - If total length is even → median is  
       `(max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2`.
     - If odd → median is `max(maxLeft1, maxLeft2)`.
   - If `maxLeft1 > minRight2`, move `i` left (`right = i - 1`).
   - Else move `i` right (`left = i + 1`).
5. This finds the unique cut where **all left elements ≤ all right elements**, so the median lies between the two border values.

## Code
Final implementation is in `solution.py`.

## Complexity Analysis
- **Time:** O(log min(n1, n2)) — Binary search only on the shorter array.
- **Space:** O(1) — Constant extra variables.

## Review
- I didn’t solve it alone; I asked ChatGPT for the partition idea.  
- **What I was missing**
  - A clear **invariant**: “left half size fixed” and “all left ≤ all right.”  
    My attempt tried to compare mids of both arrays and shift ranges, but it **did not enforce** this global condition.
  - Proper **edge handling** at the boundaries (empty side → ±∞ sentinels).  
    Without that, off-by-one and out-of-range cases appear.
  - The key insight that the problem is **not** about merging or two pointers across arrays, but about **finding a cut** via binary search on indices.
- **Why my old approach fails (brief)**
  - It adjusted `l1/r1` and `l2/r2` by comparing `nums1[mid1]` vs `nums2[mid2]`, which can break when arrays are interleaved unevenly.  
    Example: `nums1=[1,4]`, `nums2=[2,3,5,6]`. Comparing mids doesn’t guarantee the left half has the correct size nor that left ≤ right globally.
  - Special cases (one array empty, non-overlapping arrays) were handled ad-hoc, but the general interleaving case still breaks and led to incomplete logic (`# FILL OUT`).

**Takeaway:** Think in terms of a **valid partition** (sizes + order). Binary search on the cut index `i` with sentinels makes the proof and implementation clean.
