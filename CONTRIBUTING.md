# Contributions

Thanks for your interest in helping improve Taipy! Contributions are welcome, and they are greatly appreciated!
Every little help and credit will always be given.

There are multiple ways to contribute to Taipy, code, but also reporting bugs, creating feature requests, helping
other users in our forums, Stack Overflow, etc.

Several channels are open to communicate with the Taipy R&D team:

- The [taipy.io forum](https://www.taipy.io/community/) for open discussion with the Taipy team.
- [GitHub issues](https://github.com/Avaiga/taipy/issues) on the Taipy repository to suggest improvements, new features, or to report a bug.
- [GitHub discussions](https://github.com/Avaiga/taipy/discussions) on the Taipy repository for discussing technical topics related to the implementation of Taipy.
- [StackOverflow](https://stackoverflow.com/questions/tagged/taipy) for precise questions related to the usage of Taipy.
- [Discord](https://discord.com/invite/SJyz2VJGxV) for a more direct communication with the Taipy team.

Before contributing to Taipy, please read our [Code of conduct](https://docs.taipy.io/en/latest/contributing/code_of_conduct/)


## Never contributed to an open source project before ?

Have a look at this [GitHub documentation](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

## Bugs report

Reporting bugs is through [GitHub issues](https://github.com/Avaiga/taipy/issues).

Please report relevant information and preferably code that exhibits the problem. We provide templates to help you
present the issue in a comprehensive way.

The Taipy team will analyze and try to reproduce the bug to provide feedback. If confirmed, we will add a priority
to the issue and add it in our backlog. Feel free to propose a pull request to fix it.

## Issue reporting, feedback, proposal, design or any other comment

Any feedback or proposal is greatly appreciated! Do not hesitate to create an issue with the appropriate template on
[GitHub](https://github.com/Avaiga/taipy/issues).

The Taipy team will analyze your issue and return to you as soon as possible.

## Improve Documentation

Do not hesitate to create an issue or pull request directly on the
[taipy-doc repository](https://github.com/Avaiga/taipy-doc).

## Implement Features

The Taipy team manages its backlog in private. Each issue that is or is going to be engaged by the
Taipy team is attached to the "🔒 Staff only" label or has already assigned to a Taipy team member.
Please, do not work on it, the Taipy team is on it.

All other issues are sorted by labels and are available for a contribution. If you are new to the
project, you can start with the "good first issue" or "🆘 Help wanted" label. You can also start with
issue with higher priority like "Critical" or "High". The higher the priority, the more value it
will bring to Taipy.

If you want to work on an issue, please add a comment and wait to be assigned to the issue to inform
the community that you are working on it.

### Contribution workflow

1. Make your [own fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) of the repository
   target by the issue. Clone it on our local machine, then go inside the directory.

2. We are working with [Pipenv](https://github.com/pypa/pipenv) for our virtualenv.
   Create a local env and install development package by running `$ pipenv install --dev`, then run tests with
   `$ pipenv run pytest` to verify your setup.

3. For convention help, we provide a [pre-commit](https://pre-commit.com/hooks.html) file.
   This tool will run before each commit and will automatically reformat code or raise warnings and errors based on the
   code format or Python typing.
   You can install and setup it up by doing:
   ```bash
   $ pipenv install pre-commit
   $ pipenv run python -m pre-commit install
   ```

4. Make the changes.<br/>
   You may want to also add your GitHub login as a new line of the `contributors.txt` file located at the root
   of this repository. We are using it to list our contributors in the Taipy documentation
   (see the "Contributing > Contributors" section) and thank them.

5. Create a [pull request from your fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork).<br/>
   Keep your pull request as __draft__ until your work is finished.
   Do not hesitate to add a comment for help or questions.
   Before you submit a pull request for review from your forked repo, check that it meets these guidelines:
     - The code and the branch name follow the [Taipy coding style](#coding-style-and-best-practices).
     - Include tests.
     - Code is [rebase](http://stackoverflow.com/a/7244456/1110993).
     - License is present.
     - pre-commit works - without mypy error.
     - Taipy tests are passing.

6. The Taipy team will have a look at your Pull Request and will give feedback. If every requirement is valid, your
   work will be added in the next release, congratulation!

## Coding style and best practices

### Python

Taipy's repositories follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) and
[PEP 484](https://www.python.org/dev/peps/pep-0484/) coding convention.

## TypeScript

Taipy's repositories use the [ESLint](https://eslint.org/) and
[TypeScript ESLint](https://github.com/typescript-eslint/typescript-eslint) plugin to ensure a common set of rules.

### Git branches

All new development happens in the `develop` branch. All pull requests should target that branch.
We are following a strict branch naming convention based on the pattern: `<type>/#<issueId>[IssueSummary]`.

Where:

- `<type>` would be one of:
    - feature: new feature implementation, or improvement of a feature.
    - bug: bug fix.
    - review: change provoked by review comment not immediately taken care of.
    - refactor: refactor of a piece of code.
    - doc: doc changes (complement or typo fixes…).
    - build: in relation with the build process.
- `<issueId>` is the processed issue identifier. The advantage of explicitly indicating the issue number is that in
  GitHub, a pull request page shows a direct link to the issue description.
- `[IssueSummary]` is a short summary of the issue topic, not including spaces, using Camel case or lower-case,
  dash-separated words. This summary, with its dash (‘-’) symbol prefix, is optional.

## Important Notes

- If your PR is not created or there is no other activity within 14 days of being assigned to the issue, a warning message will appear on the issue, and the issue will be marked as "🥶Waiting for contributor".
- If your issue is marked as "🥶Waiting for contributor", you will be unassigned after 14 days of inactivity.
- Similarly, if there is no activity within 14 days of your PR, the PR will be marked as "🥶Waiting for contributor".
- If your PR is marked as "🥶Waiting for contributor", it will be closed after 14 days of inactivity.

We do this in order to keep our backlog moving quickly. Please don't take it personally if your issue or PR gets closed
because of this 14-day inactivity time limit. You can always reopen the issue or PR if you're still interested in working
on it.


## Dependency management

Taipy comes with multiple optional packages. You can find the list directly in the product or Taipy's packages.
The back-end Pipfile does not install by default optional packages due to `pyodbc` requiring a driver's manual
installation. This is not the behavior for the front-end that installs all optional packages through its Pipfile.

If you are a contributor on Taipy, be careful with dependencies, do not forget to install or uninstall depending on
your issue.

If you need to add to Taipy a new dependency, do not forget to add it in the `Pipfile` and the `setup.py`.
Keep in mind that dependency is a vector of attack. The Taipy team limits the usage of external dependencies at the
minimum.

## Contributing to taipy-doc Gallery

Here is a small section if you specifically want to contribute to the
[Gallery](docs/gallery/index.md) section. Follow these steps to add your
demo to the documentation.

### Steps:

#### 1. Create a Folder

Create a folder to organize your application description. Use a clear and concise name
for the folder that represents the content. For example:

```
docs/gallery/{category}/your_folder/
```

Category is the category of the article (finance, decision_support, llm,
visualization or other).

#### 2. Add Content

Place your images and Markdown files in the created folder. Name the
Markdown file "*index.md*".

#### 3. Add Metadata to the content

The header contains the following information:
- title: The title of the item
- category: The category of the item (fundamentals, visuals, scenario_management,
integration or large data)
- type: The type of the item (code, video or article)
- data-keywords: A comma separated list of keywords
- short-description: A short description of the item
- img: The path to the image associated with the item

This header will be used to display the article in the correct pages.

**Example:**

```
---
title: Realtime Pollution Dashboard
category: visualization
data-keywords: dashboad
short-description: Streams real-time pollution data from sensors and shows air quality on a map.
img: pollution_sensors/images/pollution_dashboard.png
---

A use-case of measuring air quality with sensors around a factory to showcase the ability of Taipy
to dashboard streaming data.

[Try it live](https://realtime-pollution.taipy.cloud/){: .tp-btn target='blank' }
[Get it on GitHub](https://github.com/Avaiga/demo-realtime-pollution){: .tp-btn .tp-btn--accent target='blank' }

# Understanding the Application

Rest of the description of your application
```

Note that every application have a short description at the beginning and
two buttons:

- one to see the deployed application and test it,
- one to the GitHub repository.

You shall then describe your application in more details.

#### 4. Update mkdocs.yml_template

Add the new Markdown file to the "mkdocs.yml_template" file in the appropriate section.

```
"Title of the Application": gallery/{category}/your_folder/index.md
```

#### Checklist:

- Ensure no spaces in filenames.
- Check for unrecognized characters. Building the documentation will help you know
if any are present.
- Break lines in the Markdown file before 100 characters.
- Use relative links to taipy doc (.md). To express
`https://docs.taipy.io/en/latest/manuals/studio/config/` in a tip article, write
`../../../manuals/studio/config/index.md`.
- Follow conventions for styling code, variables, etc.
- Check the level of titles in the Markdown file.
- Build the doc and test the page. See [INSTALLATION.md](INSTALLATION.md)


## Contributing to taipy-doc Tutorials

Here is a small section if you specifically want to contribute to the
[Tutorials](docs/tutorials/index.md) section. Follow these steps to add your
article to the documentation.

### Steps:

#### 1. Create a Folder

Create a folder to organize your tutorial. Use a clear and concise name for the
folder that represents the content. For example:

```
docs/tutorials/{category}/your_folder/
```

Category is the category of the article (fundamentals, visuals, scenario
management, integration or large data).

#### 2. Add Content

Place your images and Markdown files in the created folder. Name the
Markdown file "*index.md*".

#### 3. Add Metadata to the content

The header contains the following information:
- title: The title of the item
- category: The category of the item (fundamentals, visuals, scenario_management,
integration or large data)
- data-keywords: A comma separated list of keywords
- short-description: A short description of the item
- img: The path to the image associated with the item

This header will be used to display the article in the correct pages.

**Example:**

```
---
title: Scenarios
category: scenario_management
data-keywords: scenario cycle configuration datanode dag
short-description: A Taipy scenario models an instance of your end-user business problem to solve on data and parameter sets.
img: 1_scenarios/images/scenario.png
---

And here is the content of my article...
```

#### 4. Update mkdocs.yml_template

Add the new Markdown file to the "mkdocs.yml_template" file in the appropriate section.

```
"Title of the Article": tutorials/{category}/your_folder/index.md
```

#### Checklist:

- Ensure no spaces in filenames.
- Check for unrecognized characters. Building the documentation will help you know
if any are present.
- Break lines in the Markdown file before 100 characters.
- Use relative links to taipy doc (.md). To express
`https://docs.taipy.io/en/latest/manuals/studio/config/` in a tip article, write
`../../../manuals/studio/config/index.md`.
- Follow conventions for styling code, variables, etc.
- Check the level of titles in the Markdown file.
- Build the doc and test the page. See [INSTALLATION.md](INSTALLATION.md)
