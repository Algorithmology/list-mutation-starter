# List Mutation

## Table of Contents

<!---toc start-->

* [List Mutation](#list-mutation)
  * [Table of Contents](#table-of-contents)
  * [Gregory M. Kapfhammer](#gregory-m-kapfhammer)
  * [Re-type the sentence "I adhered to the Allegheny College Honor Code while completing this project."](#re-type-the-sentence-i-adhered-to-the-allegheny-college-honor-code-while-completing-this-project)
  * [Program Output](#program-output)
    * [Report at least two examples of program output from when you ran the `systemsense` program](#report-at-least-two-examples-of-program-output-from-when-you-ran-the-systemsense-program)
      * [First output from running the `systemsense` program](#first-output-from-running-the-systemsense-program)
      * [Second output from running the `systemsense` program](#second-output-from-running-the-systemsense-program)
    * [Use two fenced code blocks to provide output from all different runs of `listmutator` for the two data types](#use-two-fenced-code-blocks-to-provide-output-from-all-different-runs-of-listmutator-for-the-two-data-types)
      * [Provide the command the output for the runs of the `listmutator` for the `SLL`](#provide-the-command-the-output-for-the-runs-of-the-listmutator-for-the-sll)
      * [Provide the command output for the runs of the `listmutator` for the `DLL`](#provide-the-command-output-for-the-runs-of-the-listmutator-for-the-dll)
  * [Data Tables](#data-tables)
  * [Performance Analysis](#performance-analysis)
  * [Professional Development](#professional-development)
    * [Overall, what are the trade-offs associated with using a linked list?](#overall-what-are-the-trade-offs-associated-with-using-a-linked-list)
    * [What is challenging about designing an experiment to evaluate the performance of linked lists?](#what-is-challenging-about-designing-an-experiment-to-evaluate-the-performance-of-linked-lists)
    * [Take Home Points](#take-home-points)

<!---toc end-->

## Add Your Name Here

## Re-type the sentence "I adhered to the Allegheny College Honor Code while completing this project."

TODO: You must retype the sentence here in order to digitally sign your pledge.

**IMPORTANT:** If you do not type the required sentence then the course
instructor will not know that you adhered to the Allegheny College Honor Code
while completing the project.

## Program Output

### Report at least two examples of program output from when you ran the `systemsense` program

#### First output from running the `systemsense` program

TODO: Add output from running the specified program

#### Second output from running the `systemsense` program

TODO: Add output from running the specified program

### Use two fenced code blocks to provide output from all different runs of `listmutator` for the two data types

#### Provide the command output for the runs of the `listmutator` for the `SLL`

TODO: Provide the complete command-lines for your uses of the `listmutator` program

TODO: Provide your own example of a command and the output that it produces
TODO: Make sure that each run is for a unique configuration of the tool
TODO: Make sure that each run is only for the use of the tool with the specified data structure

#### Provide the command output for the runs of the `listmutator` for the `DLL`

TODO: Provide the complete command-lines for your uses of the `listmutator` program

TODO: Provide your own example of a command and the output that it produces
TODO: Make sure that each run is for a unique configuration of the tool
TODO: Make sure that each run is only for the use of the tool with the specified data structure

## Data Tables

TODO: You must add instrumentation using tools like `timeit` to ensure that the
`listmutator` calculates and reports the time overhead data that you will need
to complete the entire experiment. Before you conduct your experiments, please
carefully confirm that `listmutator` calculates and reports the time overhead
values in a correct fashion.

TODO: Use Markdown to provide one or more data tables that summarize the results
from running the `listmutator` program in all possible different configurations.

## Performance Analysis

TODO: Use several paragraphs and/or a list to explain each of the unique
configurations for which it is possible to run the `listmutator` program. Please
note that, for this algorithm engineering project, you are required to run the
`listmutator` tool in all possible valid configurations so that you can
carefully study the performance of all the key methods provided by the
`SinglyLinkedList` and `DoublyLinkedList` classes. You need to make sure that
you specific values for `--startsize` and `--runs` that ensure the `listmutator`
will report performance results that help you to accurately characterize the
worst-case time complexity of the following linked-based operations:

- `removefirst` that removes data from the `_head` of a `SLL` or `DLL`
- `removelast` that removes data from the `_tail` of a `SLL` and `DLL`
- `__add__` that performs the concatenation of two `SLL` or `DLL` instances
through the use of the `+` operator
- `__iadd__` that performs the concatenation of two `SLL` or `DLL` instances
through the use of the `+=` operator

Your implementation of the `SinglyLinkedList` and `DoublyLinkedList` classes
must adhere to the specification and design provided on the course web site. In
addition to providing empirical results in this file you must state what you
think is the worst-case time complexity of each of the operations in the above
list. You must also state whether or not your empirical results confirm and/or
contradict these stated worst-case time complexities. Please note that if the
course web site does not provide an implementation of a specific method then you
must create your own implementation that carefully follows the principles to
which the other operations adhere. Finally, while your experiments are only
required to, for instance, study the use of `int` data inside of the `SLL` and
`DLL` instances, you may also consider how different data types may influence
the performance of these four operations.

TODO: Make sure that your responses explain WHY certain configurations are faster!

TODO: It is not sufficient to ONLY explain WHICH configuration is faster!

TODO: It is not sufficient to ONLY discuss the empirical results! You must also
state and explain the worst-case time complexities for each of the stated
methods!

## Professional Development

### Overall, what are the trade-offs associated with using a linked list?

TODO: Provide a one-paragraph response that answers this question in your own words.

### What is challenging about designing an experiment to evaluate the performance of linked lists?

TODO: Provide a one-paragraph response that answers this question in your own words.

### Take Home Points

TODO: Provide a two to three sentence statement about the key takeaways from
conducting this experiment. Please note that the course instructor will display
some student takeaways on the course web site and use them to facilitate
follow-on class discussions.
