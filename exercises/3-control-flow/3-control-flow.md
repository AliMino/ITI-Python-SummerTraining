# Exercises - Control Flow

- [Exercises - Control Flow](#exercises---control-flow)
  - [Constructing The Data Dictionary](#constructing-the-data-dictionary)
    - [The Course](#the-course)
    - [The Enrollments](#the-enrollments)
    - [The Trainee](#the-trainee)
    - [The Courses' Points](#the-courses-points)
  - [Operating On The Data Dictionary](#operating-on-the-data-dictionary)

## Constructing The Data Dictionary

Use the attached files[^courses] [^trainees] [^enrollments] [^points] to build the courses dictionary, where all keys are strings representing the names of the courses, and the values are [course dictionaries](#the-course).

```python

courses = {
    "COURSE_NAME": {
        # Course details...
    }
}
```

### The Course

Each course is a dictionary with the following keys: `id` (integer), `code` (string), `total_points` (float), [`enrollments`](#the-enrollments) (list) and [`points`](#the-courses-points) (dictionary), as following...

```python
courses = {
    "COURSE_NAME": {
        "id": int,
        "code": str,
        "total_points" int,
        "enrollments": [
            # Trainess enrollment details...
        ],
        "points": {
            # Trainees points...
        }
    }
}
```

### The Enrollments

Each item in the enrollments list is an enrollment dictionary with the following keys: [`trainee`](#the-trainee) (dictionary) and `enrollment_date` (string), as following...

```python
    {
        "enrollments": [
            { "trainee": {}, "enrollment_date": str }
        ]
    }
```

### The Trainee

Each trainee is a dictionary with the following keys: `id` (int) and `name` (str), as following...

```python
    {
        "trainee": { "id": int, "name": str }
    }
```

### The Courses' Points

The `point` dictionary maps the name of a trainee to his/her score at this particular course, as following...


```python
    {
        "points": { "TRAINEE_NAME": float }
    }
```

---

---

## Operating On The Data Dictionary

After constructing the [`courses` dictionary](#constructing-the-data-dictionary), write Python snippets to carry out the following operations:

1. Add a new course to the courses dictionary.
1. Enrol a trainee in a course.
1. Record a trainee's points on a course.
1. Retrieve the total number of courses.
1. Retrieve the names of all available courses.
1. For each course retrieve the following details:
   1. The number of trainees enrolled on this course.
   1. The names of all trainees enrolled on this course.
   1. The minimum and the maximum points obtained in this course, by who?
   1. The average points obtained in this course.
1. Check if a trainee is enrolled on a course.
1. For each trainee retrieve the following details:
   1. The number of courses did this trainee enroll in.
   1. The name of the course at which this trainee has obtained his maximum and minimum score percentage.
   1. The average score percentage obtained by this trainee in all courses.
   1. The rank of this trainee; the rank is either
      - Poor: If the trainee had obtained 50% average score percentage or less, or less than 60% in 3 courses or less.
      - Able: If the trainee is enrolled on 3 courses or less, and had obtained at least 60% average score percentage.
      - Good: If the trainee is enrolled on 3 courses or more all the way up to 5 courses, and had obtained average score percentage between 60%, exclusive and 70%, inclusive.
      - Proper: If the trainee is enrolled on 3 courses or more all the way up to 5 courses, and had obtained average score percentage between 70% and 80%, exclusive.
      - Nice: If the trainee is enrolled on 3 courses or more all the way up to 5 courses, and had obtained at least 80% average score percentage.
      - Great: If the trainee is enrolled on more than 5 courses, and had obtained at least 70% average score percentage.

[^courses]: [course.csv](courses.csv)

[^trainees]: [trainees.csv](trainees.csv)

[^enrollments]: [enrollments.csv](enrollments.csv)

[^points]: [Python](points/py36.csv) &emsp; [PHP](points/php81.csv) &emsp; [SQL](points/sql.csv) &emsp; [Docker](points/do.csv) &emsp; [TypeScript](points/ts.csv) &emsp; [Angular](points/ng.csv) &emsp; [C++](points/cpp.csv)
