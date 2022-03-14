<h2><a href="https://leetcode.com/problems/valid-parentheses/">20. Valid Parentheses</a></h2><h3>Easy</h3><hr><i>Tags:</i></br>
<b>string | stack</b>
</br></br>
<i>Companies:</i></br>
<b>airbnb | amazon | bloomberg | facebook | google | microsoft | twitter | zenefits</b><hr>
<div><p>Given a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
</ol>

<p> </p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "()[]{}"
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "(]"
<strong>Output:</strong> false
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= s.length <= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>'()[]{}'</code>.</li>
</ul>
</div>

---

## Explanation:

```
First We will take an empty stack.
If '(' or '{' or '[' is encountered, then we will push that into the stack.
If ')' is encountered and last appended element in p is '(', then I will pop the last appended '('
Suppose, Stack = [ '[', '{', '(' ] and I got ')', then [ '[', '{', '(', ')' ]. The last 2 element will cancel out because of valid parenthases
In the same way,
If '}' is encountered and last appended element in p is '{', then I will pop the last appended '{'
If ']' is encountered and last appended element in p is '[', then I will pop the last appended '['.

In other condition we will return False
Because, Suppose Stack = [ '[', '{', '(' ] and we got '}'.Now, Stack = [ '[', '{', '(', '}']. So, this is invalid.

At the end there is no element in the stack, then that is a valid staring. So, return True
Else, Return False
```

## Solutions:

### Approach #1:

```py
class Solution:
    def isValid(self, s: str) -> bool:

        ParMap = {'}': '{', ']': '[', ')':'('}

        stack = []

        for p in s:
            if p in '([{':
                stack.append(p)
            else:
                if stack and ParMap[p] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
```

### Approach #2:

```py
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for k in s:
            if k == "(" or k == "[" or k == "{":
                stack.append(k)
            elif stack:
                last_elem = stack.pop()
                if k == ")" and last_elem == "(":
                    continue
                elif k == "]" and last_elem == "[":
                    continue
                elif k == "}" and last_elem == "{":
                    continue
                else:
                    return False
            else:
                return False

        return True if not stack else False
```

### Approach #3:

```py

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack: return False
                if stack:
                    p = stack.pop()
                    a = (p == '(' and char == ')')
                    b = (p == '[' and char == ']')
                    c = (p == '{' and char == '}')
                    if not a and not b and not c:
                        return False

        return not stack
```

### Approach #4:

```py
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 != 0:
            return False

        Dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        dictKeys = Dict.keys()

        for i in s:
            if i in dictKeys:
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i != Dict[a]:
                    return False

        return stack == []
```

### Approach #5:

```py
class Solution:
    def isValid(self, s: str) -> bool:
        dic, stack = {')': '(', ']': '[', '}': '{'}, []
        for i in s:
            if stack and dic.get(i) == stack[-1]:
				stack.pop()
            else:
				if i in dic:
					return False
				stack.append(i)
        return not stack
```

### Approach #6:

```py
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif stack and stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack and stack[-1] == '{' and i == '}':
                stack.pop()
            elif stack and stack[-1] == '[' and i == ']':
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False

```

### Approach #7:

```py
def isValid(self, s: str) -> bool:
	while "()" in s or "[]" in s or "{}" in s:
		s = s.replace("()", "")
		s = s.replace("[]", "")
		s = s.replace("{}", "")
	return s == ""
```

### Approach #8:

```py
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                curBracket = stack.pop()
                if curBracket == "(":
                    if bracket != ")":
                        return False
                if curBracket == "{":
                    if bracket != "}":
                        return False
                if curBracket == "[":
                    if bracket != "]":
                        return False
        if stack:
            return False
        else:
            return True
```
