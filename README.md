# Student Grade and GPA Calculator

A Python script to calculate grades and GPA based on course scores.

## Features
- *Grade Calculation*: Converts scores into letter grades (A, B, C, D, E, F).
- *GPA Calculation*: Computes GPA using numeric equivalents of letter grades.
- *Error Handling*: Ensures input scores are numeric and between 0–100.

## Grading Scale
| Score Range | Letter Grade |
|-------------|--------------|
| 0–29        | F            |
| 30–40       | E            |
| 41–50       | D            |
| 51–65       | C            |
| 66–75       | B            |
| 76–100      | A            |

## How to Run
1. Open the terminal.
2. Run the script using Python:
   ```bash
   python grade_gpa_calculator.py

	3.	Enter your name and scores for each course.

Example Output

Enter your name: John Doe
Enter your biology course score: 85
Enter your chemistry course score: 74
Enter your physics course score: 61
Enter your english course score: 90

 Biology: A
 Chemistry: B
 Physics: C
 English: A

GPA: 4.25

Requirements
	•	Python 3.x

Notes
	•	Customize the grading scale by editing the determine_grade_level function.
	•	Add more courses by updating the input prompts and GPA calculation logic.

License

MIT License

Copyright (c) 2024 [Victor Mbah ]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
