===== Project Overview =====
This notebook investigates the real-world performance of two data structures, HashSet and Trie, in the context of a sentiment analysis task using airline reviews.

Through three structured experiments, we compare theoretical and practical runtime behavior under varying workloads, data characteristics, and access patterns.

===== Repository Structure =====
--------------------------------------------------------------------------------------
1. src/
- Contains all source code modules that implement the project’s core logic and data structures.
| File                  | Description                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `trie.py`             | Implementation of the Trie data structure used for lexicon lookup.                                                       |
| `utils.py`            | Helper functions for tokenization, timing, and preprocessing.                                                            |
| `sentiment_scorer.py` | Defines `HashSetSentimentScorer` and `TrieSentimentScorer` classes that handle review scoring using each data structure. |
*These files are required to run the notebook successfully

--------------------------------------------------------------------------------------
2. Experiment Results/
- Contains screenshots of all generated graphs and output tables from each experiment.

These are provided as a fallback in case the Jupyter Notebook cannot be executed on the marker’s system.

Each Experiment (1, 2, 3) includes:
1. Results Table
2. Graphs

--------------------------------------------------------------------------------------
3. data/
- Stores all datasets and lexicons used in the experiments.
| File                 | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| `airline.csv`        | The main dataset containing airline review text used for sentiment scoring. |
| `positive-words.txt` | Positive sentiment lexicon used by both data structures.                    |
| `negative-words.txt` | Negative sentiment lexicon used by both data structures.                    |

*These files are required to run the notebook successfully

--------------------------------------------------------------------------------------
4. Presentation/
Contains the PowerPoint presentation slides used for the in-class presentation of this assignment.
Slides summarize:
1) Experiment design
2) Key findings from each experiment
3) Learning points and real-world implications

--------------------------------------------------------------------------------------
5. Sentiment Analysis - G3T6.ipynb
The main Jupyter Notebook containing all experiments, analysis, and conclusions:
Experiment 1: Lookup Runtime vs Number of Reviews (N)
Experiment 2: Lookup Runtime vs Lookup Runtime vs Prefix Overlap
Experiment 3: Lookup Runtime vs Workload Characteristics (Hit/Miss Ratio & Access Order)

Each includes inline results, graphs, and full discussion of findings.

===== Notes For Markers =====
1. Hardware Dependency
- Runtime results are hardware-dependent
- Differences in CPU architecture, cache size, and memory speed may slightly alter absolute timings, but relative trends and conclusions remain consistent

2. Long Runtime
- The full notebook may take several minutes to execute (depending on system specifications)
- Some experiments perform repeated runs to obtain median runtimes for accuracy
- If time-constrained, you may view the pre-generated results in the Experiment Results/ folder

3. AI Assistance Disclaimer
AI (specifically ChatGPT) was used for the following purposes (in varying degrees) in our assignment:
1) Idea Generation
3) Code Generation
3) Debugging


===== Testing Environment =====
This is the computer environment that ran the current sample output on the submitted jupyter notebook file

=== Environment Information ===
Python version   : 3.12.7
Platform          : Windows 11 (10.0.22631)
Processor         : Intel64 Family 6 Model 183 Stepping 1, GenuineIntel
Machine           : AMD64
Architecture      : 64bit

=== Library Versions ===
pandas            : 2.2.2
numpy             : 1.26.4
matplotlib        : 3.9.2
os, re, math, csv, pickle, random, platform, statistics, time, sys : built-in

=== Path Info ===
Working Directory : C:\Users\marcl\DSA Assignment - Sentiment Analysis
Project Root      : C:\Users\marcl
Python Path[0]    : ..
===============================