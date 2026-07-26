# Complete Study Guide: Regular Expressions (Regex) and Advanced Regular Expressions

## Introduction

A **Regular Expression (Regex)** is a sequence of characters that defines a search pattern. Regex is commonly used to:

- Search text
- Extract information from strings
- Validate user input
- Replace text patterns
- Process files and logs

Regex is supported by many programming languages, text editors, and Integrated Development Environments (IDEs).

As your regex skills improve, you can create increasingly sophisticated text-processing solutions.

---

# Part 1: Basic Regular Expressions

## Example 1: U.S. Phone Numbers

### Regex

```python
r"\d{3}-\d{3}-\d{4}"
```

### Matches

```text
111-222-3333
888-123-7612
555-987-4567
```

### Explanation

```regex
\d{3}
```

Matches exactly 3 digits.

```regex
-
```

Matches a hyphen.

Overall format:

```text
XXX-XXX-XXXX
```

---

## Example 2: Positive and Negative Numbers

### Regex

```python
r"^-?\d*(\.\d+)?$"
```

### Matches

```te*t
10
-10
25.75
-3.14
0.99
```

###*Explanation

#### `^`

Beginning o* string.

#### `-?`

Optional nega*ive sign.

#### `\d*`

Zero or mor* digits.

#### `(\.\d+)?`

Optiona* decimal portion.

#### `$`

End o* string.

This regex validates num*ers with or without decimal places*

---

## Example 3: Extracting Pa*ts of URLs or File Paths

### Rege*

```python
r"^/(.+)/([^/]+)/$"
``*

### Example Match

```text
/proj*cts/python/
```

### Captured Grou*s

| Group | Value |
|---------|--*------|
| Group 1 | projects |
| G*oup 2 | python |

### Explanation
*#### `^/`

Must begin with a slash*

#### `(.+)`

Captures directory *ames.

#### `([^/]+)`

Captures te*t that isn't a slash.

#### `/$`

*ust end with a slash.

This patter* is commonly used when processing:*
- URLs
- Directory structures
- F*le paths

---

# Helpful Learning *ool

Regex can quickly become diff*cult to read and understand.

A po*ular website for learning and debu*ging regex is:

https://regex101.c*m/

This tool:

- Explains regex p*tterns step by step
- Tests matche* in real time
- Shows captured gro*ps
- Helps debug expressions

---
*# Part 2: Advanced Regular Express*ons

Advanced regex techniques provide more control over pattern matching and text manipulation.

---

# 1. Alternation

## Definition

Alternation allows matching one option from several possibilities using the pipe symbol (`|`).

### Syntax

```regex
(option1|option2|option3)
```

### Example

```python
r"location.*(London|Berlin|Madrid)"
```

### Matches

```text
location is London
location is Berlin
location is Madrid
```

### Explanation

- `location` → literal text
- `.*` → any character(s)
- `(London|Berlin|Madrid)` → one of three possible city names

---

# 2. Matching Only at the Beginning or End

Regex anchors help ensure patterns appear at specific positions.

---

## Beginning of String (`^`)

### Example

```python
r"^My name is (\w+)"
```

### Matches

```text
My name is Asha
```

### Does Not Match

```text
Hello. My name is Asha
```

### Explanation

The `^` anchor requires the match to start at the beginning of the string.

---

## End of String (`$`)

### Example

```python
r"\w+$"
```

### Matches

```text
world
```

in

```text
Hello world
```

### Explanation

The `$` anchor requires the match to occur at the end of the string.

---

# 3. Character Ranges

## Definition

Character ranges match a single character chosen from a set.

---

## Uppercase Letters

### Regex

```python
r"[A-Z]"
```

### Matches

```text
A
B
Z
```

### Explanation

Any uppercase letter from A to Z.

---

## Digits and Symbols

### Regex

```python
r"[0-9$-,.]"
```

### Matches

```text
0
5
9
$
-
,
.
```

### Explanation

The character class accepts:

- Digits 0-9
- Dollar sign ($)
- Hyphen (-)
- Comma (,)
- Period (.)

---

# 4. Character Ranges with Quantifiers

## U.S. Phone Number Example

### Regex

```python
r"([0-9]{3}-[0-9]{3}-[0-9]{4})"
```

### Matches

```text
888-123-7612
555-333-9876
```

### Explanation

```regex
[0-9]{3}
```

Three digits.

```regex
-
```

Hyphen.

```regex
[0-9]{4}
```

Four digits.

Pattern format:

```text
XXX-XXX-XXXX
```

---

# 5. Capture Groups

## Definition

Parentheses create groups that save matched text.

### Example

```python
r"(\w+)@(\w+\.\w+)"
```

### Input

```text
user@example.com
```

### Groups

| Group | Captured Text |
|---------|---------|
| 1 | user |
| 2 | example.com |

Capture groups become particularly useful with substitutions and backreferences.

---

# 6. Backreferences

## Definition

Backreferences reuse previously captured groups.

Used frequently with:

```python
re.sub()
```

---

## Example

```python
re.sub(
    r"([A-Z])\.\s+(\w+)",
    r"Ms. \2",
    "A. Weber and B. Bellmas have joined the team."
)
```

### Output

```text
Ms. Weber and Ms. Bellmas have joined the team.
```

### Explanation

Regex:

```regex
([A-Z])\.\s+(\w+)
```

Matches:

```text
A. Weber
B. Bellmas
```

Captured groups:

| Group | Content |
|---------|---------|
| \1 | Initial |
| \2 | Last name |

Replacement:

```python
r"Ms. \2"
```

Result:

```text
A. Weber → Ms. Weber
B. Bellmas → Ms. Bellmas
```

---

# 7. Lookahead

## Definition

Lookahead checks if a pattern is followed by another pattern without including that pattern in the final match.

### Syntax

```regex
pattern(?=another_pattern)
```

---

## Example

### Regex

```python
r"(Test\d)-(?=Passed)"
```

### Text

```text
Test1-Passed, Test2-Passed, Test3-Failed,
Test4-Passed, Test5-Failed
```

### Matches

```text
Test1
Test2
Test4
```

### Explanation

```regex
Test\d
```

Matches:

```text
Test1
Test2
Test3
Test4
Test5
```

But:

```regex
(?=Passed)
```

Requires "Passed" immediately after the hyphen.

Therefore:

```text
Test1-Passed ✅
Test2-Passed ✅
Test3-Failed ❌
Test4-Passed ✅
Test5-Failed ❌
```

Only:

```text
Test1
Test2
Test4
```

are returned.

---

# Regex Cheat Sheet

## Character Classes

```regex
\d     Digit
\w     Word character
\s     Whitespace
[A-Z]  Uppercase letter
[a-z]  Lowercase letter
[0-9]  Digit range
```

---

## Quantifiers

```regex
*      Zero or more
+      One or more
?      Zero or one
{3}    Exactly three
{2,5}  Between 2 and 5
```

---

## Anchors

```regex
^      Start of string
$      End of string
```

---

## Grouping

```regex
(...)      Capture group
(?:...)    Non-capturing group
```

---

## Alternation

```regex
cat|dog|bird
```

Match either:

```text
cat
dog
bird
```

---

## Lookahead

```regex
X(?=Y)
```

Match X only if followed by Y.

---

## Backreferences

```regex
\1
\2
\3
```

Reuse captured groups.

---

# Common Uses of Regex

Regex is frequently used for:

### Data Validation

```text
Phone numbers
Emails
Passwords
Dates
Postal codes
```

### Data Extraction

```text
URLs
Usernames
Filenames
Log data
```

### Search and Replace

```text
Cleaning data
Formatting text
Renaming patterns
```

### Text Processing

```text
Web scraping
File parsing
Natural language processing
```

---

# Key Takeaways

✅ Regex is a powerful language for pattern matching.

✅ Basic regex supports searching, extraction, and validation.

✅ Anchors (`^`, `$`) control match position.

✅ Character classes (`[A-Z]`, `[0-9]`, `\d`, `\w`) define allowed characters.

✅ Quantifiers (`*`, `+`, `?`, `{n}`) control rep*tition.

✅ Alternation (`|`) lets *ou choose between multiple pattern*.

✅ Capture groups store matched *alues.

✅ Backreferences reuse cap*ured values.

✅ Lookaheads apply c*nditions without consuming characters.

✅ Regular expressions are widely used in software development, automation, and data processing.

---

# Useful Resources

### Regex Debugger

https://regex101.com/

### Regex Practice

https://regexcrossword.com/

### Python Regex Documentation

https://docs.python.org/3/howto/regex.html

https://docs.python.org/3/library/re.html

### Greedy vs Non-Greedy Matching

https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy