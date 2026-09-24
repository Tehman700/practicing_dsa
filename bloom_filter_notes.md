# Bloom Filter — How It Works

## 1. The problem it solves

You want to answer: **"Have I seen this item before?"**

A `set` answers this perfectly, but it stores every item. 100 million emails
in a Python set = several GB of RAM.

A Bloom filter answers the same question using **~10 bits per item**, no matter
how long the items are. 100 million items ≈ 120 MB.

The catch: it's allowed to lie in one direction.

| Filter says | Truth |
|---|---|
| "No" | **Definitely not there.** Never wrong. |
| "Yes" | **Probably there.** Might be wrong (false positive). |

No false negatives, some false positives. That trade is the whole idea.

---

## 2. The data structure

Just **an array of bits**, all starting at 0.

```
index: 0  1  2  3  4  5  6  7  8  9 ...
bits:  0  0  0  0  0  0  0  0  0  0
```

Two numbers define it:
- `m` = how many bits in the array
- `k` = how many hash functions you use

---

## 3. Adding an item

1. Run the item through `k` different hash functions.
2. Each hash gives you a number → take it `mod m` to get a bit index.
3. Set all `k` of those bits to 1.

Adding `"Alice"` with `k = 3`:

```
hash1("Alice") % 10 = 2
hash2("Alice") % 10 = 5
hash3("Alice") % 10 = 9

index: 0  1  2  3  4  5  6  7  8  9
bits:  0  0  1  0  0  1  0  0  0  1
             ^        ^           ^
```

Then adding `"Bob"`:

```
hash1("Bob") % 10 = 1
hash2("Bob") % 10 = 5      <-- already 1, that's fine, leave it
hash3("Bob") % 10 = 7

index: 0  1  2  3  4  5  6  7  8  9
bits:  0  1  1  0  0  1  0  1  0  1
```

**Bits are never turned back off.** That's why you can't delete from a
Bloom filter.

---

## 4. Checking an item

Hash it the same way, look at those `k` bits.

- **Any bit is 0** → the item was never added. Return `False`. This is certain,
  because adding it would have set that bit.
- **All bits are 1** → return `True`. Probably there... but maybe those bits
  were set by *other* items.

Check `"Alice"` → bits 2, 5, 9 → all 1 → `True` ✓ (correct)

Check `"Carol"`, where hashes give 1, 5, 7:
```
index: 0  1  2  3  4  5  6  7  8  9
bits:  0  1  1  0  0  1  0  1  0  1
          ^        ^     ^
```
All three are 1 → returns `True`, but Carol was never added.
**That's a false positive** — bit 1 and 7 came from Bob, bit 5 from either.

---

## 5. Why `k` hashes and not 1?

- **k = 1**: one bit per item. The array fills up fast and everything collides.
- **k too large**: each item sets many bits, the array saturates, and soon
  *every* lookup returns "all ones" = always true. Useless.

There's a sweet spot in the middle.

---

## 6. The two formulas

Given `n` items you plan to store and `p`, the false-positive rate you'll accept:

```
m = -(n * ln(p)) / (ln 2)^2        <- number of bits
k = (m / n) * ln 2                 <- number of hash functions (round it)
```

Worked example, `n = 1,000,000`, `p = 0.01` (1%):

```
m = -(1e6 * ln 0.01) / (0.693)^2 = 9,585,059 bits ≈ 1.14 MiB
k = (9585059 / 1e6) * 0.693 ≈ 6.6 → 7 hashes
```

**The key insight:** `m / n` = 9.58 bits per item. Plug in `n = 1e9` and you
still get 9.58 bits per item. **Bits-per-item depends only on `p`, never on
`n`.** That's why Bloom filters scale.

Rough table for 1% FPR:

| items | memory |
|---|---|
| 1 thousand | 1.2 KB |
| 1 million | 1.14 MiB |
| 1 billion | 1.11 GiB |

Want 0.1% instead of 1%? That costs ~14.4 bits/item. Each extra 10× accuracy
costs about 4.8 more bits per item — cheap.

---

## 7. Getting `k` hash functions (the practical bit)

You don't need `k` separate hash algorithms. Standard trick
(**Kirsch–Mitzenmacher**): take one hash, split it into two halves `h1` and `h2`,
then generate as many as you want:

```
index_i = (h1 + i * h2) % m      for i = 0, 1, 2, ..., k-1
```

In Python: `hashlib.blake2b(item.encode(), digest_size=16).digest()` gives you
16 bytes. First 8 bytes → `h1`, last 8 bytes → `h2`
(via `int.from_bytes(...)`). One hash call instead of `k`.

Tip: force `h2` to be odd (`h2 |= 1`). An even stride can walk a short cycle
through the array and revisit the same indices.

---

## 8. Storing bits in Python

A `bytearray` is the natural fit — 8 bits per byte, no dependencies.

For bit at position `i`:

```
byte position  = i // 8      (or i >> 3)
bit within it  = i % 8       (or i & 7)

set:    bits[i >> 3] |=  (1 << (i & 7))
test:   bits[i >> 3] >>  (i & 7) & 1
```

`bytearray(m // 8)` allocates and zeroes it in one go.

---

## 9. What to build

```
class BloomFilter:
    __init__(self, capacity, error_rate=0.01)
        compute m and k from the formulas
        allocate the bytearray
        keep a count of insertions

    _indices(self, item)        -> yields k bit positions
    add(self, item)             -> set those bits
    __contains__(self, item)    -> all those bits set?
```

`__contains__` is the dunder that makes `if x in filter:` work.

---

## 10. How to test it

The satisfying part — check the math holds:

1. Build a filter with `capacity = 100_000`, `error_rate = 0.01`.
2. Add 100,000 strings (`"item0"` … `"item99999"`).
3. Check all 100,000 are found → must be **100%**. Any miss = bug in your code.
4. Check 100,000 strings you *never* added (`"nope0"` … `"nope99999"`).
5. Count how many wrongly say `True`. Divide by 100,000.

You should land near 1%. If you get ~0% you over-sized `m`; if you get 30%+,
`k` or the index math is wrong.

Then try `error_rate = 0.001` and confirm the measured rate drops to ~0.1%.
Watching the prediction match reality is the moment it clicks.

---

## 11. Gotchas

- **No deletion.** Clearing bits would break other items sharing them.
  (A *Counting* Bloom filter uses counters instead of bits to allow it.)
- **Overfilling.** Past `capacity`, the FPR climbs fast. It doesn't error —
  it just quietly gets worse.
- **Don't use Python's `hash()`.** It's randomly salted per process, so your
  filter gives different answers on every run.
- **Test with items you truly never added.** If your "absent" set overlaps the
  "present" set, your measured FPR is meaningless.

---

## 12. Where they're actually used

- Browsers checking a URL against a malicious-sites list before a network call
- Databases (Cassandra, HBase) skipping disk reads for keys that aren't there
- CDNs deciding whether to cache on first request or second
- Spell checkers, in the old days

The pattern is always the same: **a cheap "definitely no" that lets you skip
an expensive lookup.**
