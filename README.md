# sanskrit

Write programs in the fastest language, as confirmed by NASA.

## Installation

```bash
pip install sanskrit
```

Now put a `# coding: sanskrit` comment above your code to start programming in sanskrit!

## Usage

There's two ways to use `sanskrit`:

### As a REPL

Simply type `sanskrit` and it will bring up the `sanskrit` REPL:

```pycon
$ sanskrit
संस्कृत प्रोग्रामिंग 3.11.5 (main, Aug 24 2023, 15:09:45) [Clang 14.0.3 (clang-1403.0.22.14.1)]
>>> x = 42
>>> दर्शयतु(x)   # print(x)
42
```

### In a project

- Simple for loop:

  ```python
  # coding: sanskrit
  सर्वेषां आई अन्तः सीमा(5):   # for i in range(5):
      दर्शयतु(आई)          #     print(i)
  ```

  Output:

  ```console
  $ python example.sanskrit
  0
  1
  2
  3
  4
  ```

- `import this`:

  ```python
  # -*- coding: sanskrit -*-
  आयातम् इदम्‌
  ```

  Output:

  ```console
  $ python example.sanskrit
  The Zen of Python, by Tim Peters

  Beautiful is better than ugly.
  Explicit is better than implicit.
  ...
  ```
