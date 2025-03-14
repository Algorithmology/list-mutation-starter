# :microscope: List Mutation

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## :joy: Table of Contents

<!---toc start-->

* [:microscope: List Mutation](#microscope-list-mutation)
  * [:joy: Table of Contents](#joy-table-of-contents)
  * [:sparkles: Introduction](#sparkles-introduction)
  * [:thumbsup: Seeking Assistance](#thumbsup-seeking-assistance)
  * [:airplane: Project Overview](#airplane-project-overview)
  * [:tada: Program Specification](#tada-program-specification)

<!---toc end-->

## :sparkles: Introduction

If you are a student completing this project as part of a class at Allegheny
College, you can check the schedule on the course website for the due date or
ask the course instructor for more information about the due date or check the
due date by clicking the appropriate box inside of this file. Please note that
the content provided in the `README.md` file for this GitHub repository is an
overview of the project and thus may not include the details for every step
needed to successfully complete every project deliverable. This means that you
may need to schedule a meeting during the course instructor's office hours to
discuss aspects of this project.

## :thumbsup: Seeking Assistance

Even though the course instructor will have covered all the concepts central to
this project before you start to work on it, please note that not every detail
needed to successfully complete the assignment will have been covered during
prior classroom sessions. This is by design as an important skill that you must
practice as an algorithm engineer is to search for and then understand and
ultimately apply the technical content found in additional resources.

## :airplane: Project Overview

This project invites you to implement and use a program called `listmutator`
that conducts an experiment to evaluate the performance of the main operations
provided by the `SinglyLinkedList` (`SLL`) and `DoublyLinkedList` (`DLL`)
classes. The specific operations that your `listmutator` program should evaluate
include these ones:

- `removefirst` that removes data from the `_head` of a `SLL` or `DLL`
- `removelast` that removes data from the `_tail` of a `SLL` or `DLL`
- `__add__` that performs the concatenation of two `SLL` or `DLL` instances
through the use of the `+` operator
- `__iadd__` that performs the concatenation of two `SLL` or `DLL` instances
through the use of the `+=` operator

Both the `SinglyLinkedList` and the `DoublyLinkedList` must be implemented in
an object-oriented fashion as outlined on the course website. The `listmutator`
program should offer functions that support the automated generation of either
`SinglyLinkedList` and `DoublyLinkedList` instances that have random integer
values while also ensuring that the size of the instances increases in a
predictable manner as would occur when performed through a doubling experiment
or a factor-of-ten experiment. The `listmutator` program should also produce
formatted and justified output that makes it easy for an algorithm engineer to
see how, for a specified operation, the execution time increases as the size of
the `SLL` or `DLL` instances increases. Ultimately, the `listmutator` program
should produce a report that contains empirical results that would make it
possible for an algorithm engineer to confirm the worst-case time complexities
for all basic operations in both the `SLL` and the `DLL`.

The `listmutator` program should also included "timing instrumentation" that
records the cost associated with the aforementioned operations provided by
either a `SLL` or a `DLL`. For instance, the `listmutator` could use the
[timeit](https://docs.python.org/3/library/timeit.html) package to measure the
performance of different `SinglyLinkedList` and `DoublyLinkedList` operations,
following the pattern in the article [measure execution time with timeit in
Python](https://note.nkmk.me/en/python-timeit-measure/). After cloning this
repository to your computer, please take the following steps to get started on
the project:

- To install the necessary software for running the `listmutator` program
that you will create as a part of this project, you may consider installing and
using the [`devenv`](https://devenv.sh/getting-started/) tool, bearing in mind
that it is not necessary for you to install the `cachix` program that may be
referenced by these installation instructions. Please note that students who
are using Windows 11 should first install Windows subsystem for Linux (`wsl2`)
before attempting to install `devenv`. Once you have installed `devenv` and
cloned this repository to your computer, you can `cd` into the directory that
contains the `pyproject.toml` file and then type `devenv shell`. It is
important to note that the first time you run this command it may complete
numerous steps and take a considerable amount of time.
- Once this command completes correctly, you will have a Python development
environment that contains a recent version of Python and Poetry! You can verify
that you have the correct version of these two programs by typing:
  - `python --version`
  - `poetry --version`
- If you do not see a recent version of Python after typing the two
aforementioned commands, then it is possible that some part of the installation
process did not work correctly. If that occurs, then please read the following
suggestions and talk with the course instructor and a student technical leader
about what to do next.
- If some aspect of the installation with `devenv` did not work correctly, then
please resolve what is wrong before proceeding further! Alternatively, you may
install the aforementioned versions of Python and Poetry on your laptop using a
tool like [`mise`](https://mise.jdx.dev/). With that said, please make sure
that you use the most recent version of Python and Poetry to complete this
project and, whenever possible, those versions match the ones chosen in GitHub
Actions. This means that, to ensure that the results from running the
experiments are consistent and, as best as is possible, comparable to the
results from other computers, you should use exactly the same version of Python
and Poetry on your laptop and in GitHub Actions. For instance, when you run
`listmutator` in GitHub Actions, you should normally see that it is using
at least Poetry version `2.0.0` and Python version `3.12.8`.
- Before moving to the next step, you may need to again type `poetry install`
in order to avoid the appearance of warnings when you next run the
`listmutator` program. Now you can type the command `poetry run
listmutator --help` and explore how to use the program.

## :tada: Program Specification

Before implementing the program so that it adheres to the following
requirements and produces the expected output, please note that the program
will not work unless you add the required source code at the designated `TODO`
markers. With that said, after you complete a correct implementation of all the
`listmutator`'s features you can run it with the command `poetry run
listmutator --operation add --startsize 10000 --runs 10 --listtype
singlylinked` and see that it produces output like the following. Please note
that while the following example illustrates the type of output that the
`listmutator` might produce it (a) may offer empirical results that are
different than those that you see on your own laptop and (b) is only for a
single example configuration for how you can run the `listmutator` program.

```text
Benchmarking Tool for List Operations

Type of list: singlylinked
Data stored in list: ints
Benchmarking strategy: double
Benchmarking operation: add
Number of runs: 10

Run  1 of 10 for add operation with singlylinked list using size    10000 took 0.0001431500 seconds
Run  2 of 10 for add operation with singlylinked list using size    20000 took 0.0002478680 seconds
Run  3 of 10 for add operation with singlylinked list using size    40000 took 0.0004875230 seconds
Run  4 of 10 for add operation with singlylinked list using size    80000 took 0.0009800040 seconds
Run  5 of 10 for add operation with singlylinked list using size   160000 took 0.0022860720 seconds
Run  6 of 10 for add operation with singlylinked list using size   320000 took 0.0043044530 seconds
Run  7 of 10 for add operation with singlylinked list using size   640000 took 0.0085097760 seconds
Run  8 of 10 for add operation with singlylinked list using size  1280000 took 0.0168375090 seconds
Run  9 of 10 for add operation with singlylinked list using size  2560000 took 0.0339418860 seconds
Run 10 of 10 for add operation with singlylinked list using size  5120000 took 0.0673185660 seconds

Minimum execution time: 0.0001431500 seconds for run 1 with size 10000
Maximum execution time: 0.0673185660 seconds for run 10 with size 5120000
Average execution time: 0.0135056807 seconds across runs 1 through 10
```

Some key aspects of the output that your implementation of the `listmutator`
should preserve are as follows:

- The output should include diagnostic information that explains the type of
list and all the other command-line arguments that the user specified.
- The output should have labels for each specific run that also shows the total
number of runs requested by the user.
- Each line that shows a performance result should include the size of the list
and then the amount of time in seconds that it took to perform the operation.
- The output should be formatted and justified so that it is easy to read, with
numbers aligned to the right and with a consistent number of decimal places.
- After the display of the execution times that arise from each run of the
benchmark, the output should show the minimum, maximum, and average execution
time values across the runs of the benchmark.

Please note that your implementation of the `listmutator` program should work for
all the specified experimental configurations in the introduction to the
project and in the `writing/reflection.md` file. If you study the files in the
`listmutator/` directory you will see that they have many `TODO` markers that
designate the functions you must implement so as to ensure that `listmutator`
runs the desired experiment and produces the correct output. Once you complete a
task associated with a `TODO` marker, make sure that you delete it and revise
the prompt associated with the marker into a meaningful comment.

It is important to note that your experimentation with the `listmutator` must
always operate according to the principles of a doubling experiment. This means
that the `listmutator` must systematically increase the size of the instance of
a `SLL` or a `DLL` by doubling the number of values contained inside of the
linked-based list. The creation of the `listmutator` requires you to add your
own implementation of the `SinglyLinkedList` and `DoublyLinkedList`. As you
create and document these data structures, please make sure that you add type
annotations to all the methods and confirm that they do not have, for instance,
unreachable code paths or undocumented implicit assumptions about the data
types. After creating these data structures and confirming that they work
correctly, you should design your own experiment and state and run experiments
to answer your own research questions, focusing on these key issues:

- If you have already installed the
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs the
automated grading checks provided by
[GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
repository's base directory, run the automated grading checks by typing
`gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all the required responses to the technical writing
prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
labels from all the provided source code. This means that instead of only
deleting the `TODO` marker from the code you should delete the `TODO` marker and
the entire prompt and then add your own comments to demonstrate that you
understand all the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
labels from every line of the `writing/reflection.md` file. This means that you
should not simply delete the `TODO` marker but instead delete the entire prompt
so that your reflection is a document that contains polished technical writing
that is suitable for publication on your professional website.
