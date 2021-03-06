# ViewTree Search CLI

ViewTree Search CLI is a command-line interface which allows a user to load ViewTree JSON scripts from files or from URLs and then perform selector searches on it.

**_What is a ViewTree?_**
A ViewTree is a hierarchical JSON with attributes which describe a view.

**_What are Selectors?_**
Selectors allow a user to identify portions of the ViewTree which are of interest by key attribute values.
The ViewTree Search CLI searches a ViewTree JSON using selectors as input from the user.

Selectors handled now include:
* Simple selectors
  * Only one of:
    * a view class name (no prefixes)
    * or a CSS class name (prefixed with a '.')
    * or a view identifier (prefixed with a '#')
* Compound selectors
  * Two or more simple selectors 
  * **Note:** _due to not having a prefix, only one view class name can be included in a Compound Selector_
  
# Key Assumptions made when completing the work

* Python's native recursion with no modification to the 1000 recursion depth limit is adequate to handle inputs.  This assumption prevents a more complicated architecture in which a recursion stack is maintained rather than using straightforward recursion.  It also prevents overriding Python's default 1000 recursion depth limit.
* A compound selector will match portions of the ViewTree simultaneously matched by all selectors in the compound selector with no regard to distance between selectors and with no implied combinators other than that all selectors must be engaged at the same time.
* A compound selector match will not short-circuit further descendent searches for other compound selector matches deeper in the ViewTree.  
* Output of the lowest-most class in the ViewTree JSON which satisfies the selector match (like a CSS match) is satisfactory.
* I know there are great, almost-standard Python libraries out there which could have made my work cleaner and easier (ahem, pytest, requests, even parameterized).  Had I searched PyPi, I might have found specific modules which could have made this work simpler.  *My assumption was that for this effort I'd use only standard library modules.*
* I assumed JSON viewtree values will not contain spaces for the keys used in selectors. This seems to make sense because of the tie to actual naming conventions in the tools represented and based on combinators.
  
# Up Next
- [ ] Attempt complex selectors/selector chaining

## Getting Started

1. Retrieve files from the Han-Shot-First repo.  
2. Perform the installation steps in the Installing section of this readme.
3. Start the CLI by executing the following command:
```
python viewtree_search_cli_demo_usage.py
```

### Prerequisites

ViewTree Search CLI was developed in Python 3.7.  However, it should be backwards compatible into Python 3.6.  I have not tested it in earlier releases of Python 3. 

### Installing

Download these Python files into a folder which has access to Python 3.6 or higher:

* viewtree_search_cli.py
* viewtree_search_cli_demo_usage.py
* test_viewtree_search.py

Download these test ViewTree JSON files into the same folder:

* the_modal_nodes.json
* mos_eisley.json

These are helpful but not necessary:

* viewtree_search_demo_usage.py

## Example usage

Check out this [example transcript](https://github.com/ErikPohl-Lot49-Projects/Han-Shot-First/blob/master/Example_transcript.md).

## Running the tests

Tests have been batched in one Python module.  To execute it, run this command from the command line in the folder in which the files are installed:
```
python -m unittest -v test_viewtree_search.py
```

## Contributing

For now, I'd be excited to receive pull requests.  I don't have rules for contributing right now.

## Authors

* **Erik Pohl** - *Initial work* - 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to everyone who has motivated me to learn more.

## Standards

Here is a generic list of standards which are applied when preparing a build.

- [x] Apply this checklist to all new projects as step one
- [x] A complete regression test suite in UnitTest (with homegrown parameterized testing)
- [x] Meaningful exceptions and exception-handling coverage.
- [x] Thoughtful, self-documenting, variable, method, and function names.
- [x] Adequate output to permit users to understand the results, assisting in the self-documenting nature of the code.
  - [x] Specifically, would this benefit from comprehensive logging?
  - [x] Would it benefit from a results page with stats to demonstrate accurate and complete results?
  - [x] How do I want to manage output to stdout, stderr, file, etc?
  - [x] How do comments and outputs help and assist one another without being redundant?
- [x] Actual docstring comments at all levels of the code.
- [x] Linting the code for PEP 8 standardization like PEP8 or Applying a PEP formatter to the code like Project Black.
- [x] Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.
- [x] Commit statements which facilitate an understanding of code history.
- [x] Readme.md pages with more interesting usage of markdown which tell a code narrative. 
- [x] For custom classes, create dunders as appropriate
- [x] Make sure to include standard module comment headers
- [x] Make good decisions relating to
  - [x] Exceptions versus return values
  - [x] Using idiomatic Python versus clarity of code
  - [x] Having functions return values -- as a default-- have a good reason not to

# Disclaimers

* Some of this documentation, naming choices, and code involves fun I might have with friends and colleagues, but not include in work intended for a client.  
* Use of a fictional blaster to dispose of bounty hunters claiming a bounty on one's head is neither endorsed nor proscribed herein.

# Trivia

* The title of this repo refers to a controversy introduced in the 1997 Special Edition Star Wars rerelease of Star Wars IV: A New Hope.

In the version of Star Wars IV: A New Hope which I watched with my familly in an Anderson, SC drive-in theater in 1977, Han Solo, when cornered by a bounty hunter in the Mos Eisley cantina, understood his best and only option to avoid an untimely end was to use his blaster to eliminate the threat.  It was self-defense, and would not have ended well had he not shot Greedo.  It showed Han was a street smart anti-hero: and it defined the beginning of Han's arc starkly when juxtaposed against Obi Wan Kenobi and the ways of a Jedi.

![What Would Han Solo Do?](https://github.com/ErikPohl-Lot49-Projects/Han-Shot-First/blob/master/media/What_would_Han_Solo_do__by_mjt423.jpg "What Would Han Solo Do?")

* You will find Garindan in the Mos Eisley test file.  This was another bounty hunter following Han in the Mos Eisley cantina.

* Mos Eisley, the name of one of the test files, is a city on Tatooine which contains a cantina in which some critical exposition (rising action for the English major nerds out there) takes place in Star Wars IV: A New Hope.

* I took the liberty of renaming SystemViewController.json to the_modal_nodes.json.  This is a reference to the band in the cantina scene in Star Wars IV: A New Hope.

![Beep beep beep](https://github.com/ErikPohl-Lot49-Projects/Han-Shot-First/blob/master/media/296937d-emp.jpg "Beep beep beep")






