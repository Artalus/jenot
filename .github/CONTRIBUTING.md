## Generic commit message conventions

* Use the imperative, present tense: "change", not "changed" nor "changes".
* do not apitalize the first letter.
* No dot (`.`) at the end
* Try to explain "why it changed" rather than "what changed", unless it is a part of a bigger change

## PR conventions
* Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) to name PRs.
The title should provide concise info about the change as whole:
```
    <type>: <description>
```
* If the PR does more than one thing - use Conventional Commits formatting not only for its title, but also for commits inside.
* Make commits atomic and concise; collapse "extras" into the "main" commit.

Summary of types:

| Type         | Explanation |
| ------------ | ----------- |
| **`build`**    | A change of the build system or build configuration. |
| **`bump`**     | An increase of the version of an external dependency or an update of a bundled third party package. |
| **`chore`**    | A change that doesn't match any other type. |
| **`ci`**       | A change of CI scripts or configuration. |
| **`docs`**     | A change of documentation only. |
| **`enhance`**  | An enhancement of the code without adding a user-visible feature, for example adding a new utility class to be used by a future feature or refactoring. |
| **`feat`**     | An addition or improvement of a user-visible feature. |
| **`fix`**      | A bug fix (not necessarily user-visible). |
| **`perf`**     | A performance improvement. |
| **`refactor`** | A restructuring of the existing code without changing its external behavior. |
| **`style`**    | A change of code style. |
| **`test`**     | An addition or modification of tests or test framework. |
| **`ux`**       | A change in GUI, CLI, or workflow, visible to user. |



## Example
Merge PRs as:
```
(#123) title
Description
```

### BAD commit tree:
```
* fixes for watchlist
|\
| o fix indentation
| o typo
| o add removing
|/
```
### BETTER commit tree:
```
* feat: allow removing entries from watchlist
|\
| o ux: add "remove" button to watchlist window
| o refactor: use new methods instead of initializing in constructor
| o enhance: add methods edit already created watchlist
|/
```
