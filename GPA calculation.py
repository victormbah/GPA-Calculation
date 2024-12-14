try:
  username = input("Enter your name: ")  # Prompt for username

  biology_score = float(input("Enter your biology course score: "))  # Get Biology score
  chemistry_score = float(input("Enter your chemistry course score: "))  # Get Chemistry score
  physics_score = float(input("Enter your physics course score: "))  # Get Physics score
  english_score = float(input("Enter your english course score: "))  # Get English score

  def determine_grade_level(course_score):
    # Determine the grade level based on the course score
    if 0 <= course_score <= 29:
        return "F"  # Failing grade
    elif 30 <= course_score <= 40:
        return "E"  # Barely passing grade
    elif 41 <= course_score <= 50:
        return "D"  # Below average grade
    elif 51 <= course_score <= 65:
        return "C"  # Average grade
    elif 66 <= course_score <= 75:
        return "B"  # Above average grade
    elif 76 <= course_score <= 100:
        return "A"  # Excellent grade
    else:
        return None  # Invalid score outside range

  def score_grade(score_range):
    # Map grade level to a numeric score
    grade_to_score = {
        "F": 0,
        "E": 1,
        "D": 2,
        "C": 3,
        "B": 4,
        "A": 5
    }
    return grade_to_score.get(score_range, None)  # Return None for invalid grades

  # Determine grade levels for each subject
  biology_grade_level = determine_grade_level(biology_score)
  chemistry_grade_level = determine_grade_level(chemistry_score)
  physics_grade_level = determine_grade_level(physics_score)
  english_grade_level = determine_grade_level(english_score)

  # Check for any invalid grades
  if None in [biology_grade_level, chemistry_grade_level, physics_grade_level, english_grade_level]:
    print("Please enter valid scores between 0 and 100.")
  else:
    biology_score_grade = score_grade(biology_grade_level)  # Convert Biology grade level to numeric
    chemistry_score_grade = score_grade(chemistry_grade_level)  # Convert Chemistry grade level to numeric
    physics_score_grade = score_grade(physics_grade_level)  # Convert Physics grade level to numeric
    english_score_grade = score_grade(english_grade_level)  # Convert English grade level to numeric

    # Display grade levels for all subjects
    print(" Biology: " + biology_grade_level)
    print(" Chemistry: " + chemistry_grade_level)
    print(" Physics: " + physics_grade_level)
    print(" English: " + english_grade_level)

    # Display numeric scores for all subjects
    print(" Biology: " + str(biology_score_grade))
    print(" Chemistry: " + str(chemistry_score_grade))
    print(" Physics: " + str(physics_score_grade))
    print(" English: " + str(english_score_grade))

    # Calculate and display GPA
    gpa = (biology_score_grade + chemistry_score_grade + physics_score_grade + english_score_grade) / 4
    print(gpa)

  # Display grade levels and scores
    print(f"\n =========== \n GRADE LEVEL \n ===========")
    print(f" Biology: {biology_grade_level}\n Chemistry: {chemistry_grade_level}\n Physics: {physics_grade_level}\n English: {english_grade_level}\n")

    print(f" =========== \n GRADE SCORE \n ===========")
    print(f" Biology: {biology_score_grade}\n Chemistry: {chemistry_score_grade}\n Physics: {physics_score_grade}\n English: {english_score_grade}\n")

    # Calculate GPA
    gpa = (biology_score_grade + chemistry_score_grade + physics_score_grade + english_score_grade) / 4
    print(f"GPA: {gpa:.2f}")
    
except ValueError:
 print("Invalid input. Please enter numeric values for scores.")