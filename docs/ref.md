# Reference card
!!! default "Documentation"

    Docs CSC is based on *Material for MkDocs*. Note that not all (by far) features are supported.

    [Reference - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/){ .md-button target=_blank }

!!! info "Source"

    This page is more useful when viewed side-by-side with [the Markdown source at GitHub](https://github.com/CSCfi/csc-user-guide/blob/master/docs/ref.md?plain=1){ target=_blank }.

This page contains some elements that are available in Docs CSC. For example, here we have some
body text [with an external link](https://example.com){ target=_blank }. **Some of it is
boldfaced**, *some italicized*. `Some might be monospaced`. Some acronyms, like HPC, are
defined automatically (see: [Glossary](#glossary)).

> There's even text in a blockquote. The blockquote has some filler text after an empty line. I
like to imagine it's what a typewriter would dream.
>
> Vel suscipit quia voluptates quis. Rerum sequi voluptatem in non ipsam tempora quod natus. Soluta
perferendis illo saepe sint ipsa vitae provident non. Et qui quaerat et rerum libero officia omnis
enim. Laboriosam autem vel vel aut quod.

## Glossary
There is a glossary of HPC-related acronyms that get highlighted automatically. For example: CPU,
GPU, QPU, etc. The acronyms are defined in the markdown file
`csc-overrides/assets/glossaries/hpc.md`. More acronyms/terms can be added there or to another
markdown file, like so:

=== "another_glossary.md"

    ```markdown
    *[GNU]: GNU's not Unix!
    ```

=== "mkdocs.yml"

    ```yaml
    markdown_extensions:
    - ...
    - pymdownx.snippets:
        base_path: csc-overrides/assets/glossaries
        auto_append:
        - hpc.md
        - another_glossary.md
    - ...
    ```

## Headings
The heading for Headings is a heading of a heading level 2. Remember to only use one heading level
1 heading on your page and to keep the heading hierarchy intact. So no skipping levels.

### This is a heading level 3 heading
That one's a level 3. Here is some text under it.

#### Now for a level 4 heading
Some text _four_ it here.

##### Level 5 heading: `now with added monospace`
No text this time.

###### Level 6
More text coming up next in Text.

## Text
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nulla ex, elementum ultrices
tempor quis, commodo sit amet quam. Sed accumsan placerat nunc. Suspendisse elementum augue et est
tempor lacinia. Pellentesque vel ante id nunc luctus euismod id non est. Vivamus porttitor dui et
porta maximus. Sed quis orci finibus, feugiat orci vitae, luctus nisl. Praesent lorem turpis,
tristique id lacus sed, sollicitudin ultricies velit. In maximus ante massa, in ullamcorper eros
IaaS fermentum in. Nulla condimentum urna sit amet leo scelerisque, et iaculis odio iaculis. Donec
quis tortor non metus tincidunt placerat. Curabitur rhoncus libero ut augue scelerisque varius.
Nunc bibendum sit amet nisi in varius. Nullam eu eros elementum, pellentesque nisl non, laoreet
felis. Ut et risus enim. Proin tempor tellus eu commodo blandit. Interdum et malesuada fames ac
ante ipsum primis in faucibus.

Nam erat dui, ullamcorper sit amet erat nec, interdum posuere diam. Nam aliquet gravida hendrerit.
Sed erat justo, feugiat sollicitudin scelerisque id, luctus sit amet velit. Sed suscipit at nisi eu
ornare. Nam in mauris ex. In ut sagittis nibh, eleifend pharetra tortor PaaS. Integer sapien
tortor, ullamcorper ac diam ut, vehicula mattis augue. Pellentesque a enim eget est ornare
ullamcorper vitae nec mi. Quisque quis congue augue, eu aliquam tortor. In risus lectus, pharetra
eu fermentum non, gravida volutpat magna. Morbi in congue erat.

Donec a est quis nulla scelerisque cursus ut vitae ligula. In risus felis, finibus et tortor eu,
volutpat efficitur turpis. Praesent vitae vulputate dolor, at posuere urna. Aenean ullamcorper orci
sit amet purus tincidunt, id vehicula lectus aliquet. Ut auctor dapibus magna at hendrerit. Nam
lobortis convallis lacus blandit tempus. Proin et ex ut dolor vehicula suscipit a vitae nisi. Nam
feugiat accumsan purus, sit amet efficitur felis. Integer vitae enim eu massa placerat faucibus
eget vel ipsum. Nullam tincidunt, sapien at blandit pulvinar, lacus mauris finibus turpis, sit amet
suscipit magna tortor sit amet tortor. Ut tortor neque, convallis non volutpat a, pharetra nec
sapien. In in congue nisl, quis egestas nisi. Fusce ut orci luctus sem tincidunt malesuada.
Pellentesque id consequat tortor, sed egestas metus. Phasellus sed venenatis purus, in dapibus
magna SaaS. Cras interdum ornare risus, a condimentum magna lacinia eget. Morbi dapibus elementum
massa et ultrices. Nulla vel lobortis ex. Ut egestas posuere odio, sit amet mollis lacus placerat
at. Quisque ut laoreet purus. Etiam id consectetur ipsum. Phasellus lectus ante, scelerisque in
nunc a, vulputate efficitur nunc. Suspendisse nec nisi ut massa mattis interdum vel eget orci.
Aenean porttitor erat nulla. Vivamus ac urna et orci faucibus pharetra. Integer in urna tincidunt,
tempor turpis nec PaaS, malesuada justo. Vivamus ornare sem ut mi ultricies fringilla. Ut in semper
diam, vitae porta neque. Donec maximus tellus et orci bibendum hendrerit. Ut ut consectetur magna.
Aliquam vel rhoncus elit. Praesent vitae tincidunt urna, et pulvinar orci. Phasellus auctor augue
eu sagittis fermentum. Nullam tempus malesuada augue, nec volutpat mi sodales quis. Vivamus mollis
commodo eros sed porta. Praesent ultrices elementum metus, sit amet fringilla turpis luctus vitae.
Mauris turpis felis, molestie eget ipsum ac, fringilla euismod risus. Phasellus at arcu ante. Cras
eu enim dui. Quisque eu hendrerit magna. Donec ac elit laoreet, mattis tortor et, feugiat nisl.
Duis maximus ultrices elit, quis hendrerit orci.

## Lists
### Unordered list
Here is an unordered list:

- It has an item
- Another item
- And yet another item

### Ordered list
Let's make an ordered list:

1. An item on a list
1. Another item
1. Even a third item

## Source code
```python
# Here is a box with some syntax highlighted Python

from somewhere import some_code


NUMBER = 42
LIST = [1, 2, "three"]


class PythonClass:
    def __init__(self):
        self.__property = "A string property"
    
    @property
    def property(self):
        return __property

    @classmethod
    def method(parameter):
        return [None] * parameter + NUMBER

def main():
    string = f'Length of list is {len(LIST)}.'
    print(string)
```

```javascript
// Here's a JavaScript comment with a loooooooooooooooooooooooooooooooong line. You know, for testing purposes. Tell you what, let's make it just a bit longer still.
```

## Tables
| This | Table | Has | Five | Columns |
|-|-|-|-|-|
| and | | | | |
| | it | | | |
| | | has | | |
| | | | five | |
| | | | | rows |

## Admonitions
### The fallback style
!!! note "Here we have an important announcement"

    Make sure you read this note inside this very important-looking box, since this is the fallback
    for unknown type qualifiers.

    Type qualifier can be anything, as long as it's not
    `default`,
    `default-label`,
    `info`,
    `info-label`,
    `warning`,
    `warning-label`,
    `error`,
    `error-label`,
    `success` or
    `success-label`.
    Perhaps a suitable one would just simply be: `note`.

!!! note ""
    Title may be removed with `note ""`.

### Styles available with type qualifiers

#### Alert style
!!! default "Nothing special"

    Type qualifier: `default`.
    
    !!! default-label
    
        This isn't the actual default (fallback) admonition for legacy reasons.

!!! info "Information available"

    Type qualifier: `info`

!!! success "You've got it!"

    Type qualifier: `success`

!!! warning "You're on thin ice!"

    Type qualifier: `warning`

!!! error "Oopsie!"

    Type qualifier: `error`

#### With the title removed
!!! default ""

    Type qualifier: `default ""`

!!! info ""

    Type qualifier: `info ""`

!!! success ""

    Type qualifier: `success ""`

!!! warning ""

    Type qualifier: `warning ""`

!!! error ""

    Type qualifier: `error ""`

#### Label style
!!! default-label

    Label type available with type qualifier `default-label`.

!!! info-label

    Label type available with type qualifier `info-label`.

!!! success-label

    Label type available with type qualifier `success-label`.

!!! warning-label

    Label type available with type qualifier `warning-label`.

!!! error-label

    Label type available with type qualifier `error-label`.

#### Inline admonitions
For inline admonitions, you first define the admonition as either `inline` or `inline end`. Then,
you define the content.

!!! warning inline "Hold on!"

    This script might give unexpected results!

    `warning inline "Hold on!"`

!!! info inline end ""

    Then again, it might not.

    `info inline end`


```bash
    a="unexpected"
    b="results"
    if [ $RANDOM -eq $RANDOM ];
    then
        echo $a $b
    fi
```

&nbsp;

Try adding a `&nbsp;` if inline admonitions give you trouble. Example found right above this line
in markdown source.

## Images
Here's an image of the Reference card with an image of the Reference card with...
![image of an image of an image...](img/ref/image.png)



## Embedded videos
At the moment, to avoid setting cookies, embedded videos are rendered only as an image with a link
to the video in question. For example: Behold! Here is a video of a horse kicking a tree, farting
on some dogs, and then running away:

<iframe
    width="400"
    height="300"
    srcdoc="https://www.youtube.com/embed/KCzwyFHSMdY"
    title="Horse kicks tree, farts on dogs then runs away."
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media;gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>

## Mermaid
```mermaid
%%{init: {'theme': 'neutral' }}%%
graph TD
    A(Does your reference card have a Mermaid chart?) -->|Yes| B(Good)
    A -->|No| C(Yes, it does.)
    C --> |What? No, you can't just... Oh.| B
```

## Buttons
Docs CSC supports two button variants from the CSC Design System.
### Default button
<!-- This is called a 'default' button in the CSC Design System and a 'primary' button in Material
for MkDocs (notice the two classes '.md-button' AND '.md-button--primary'. Also, don't forget to
include the 'target=_blank' attribute for links pointing outside of Docs)... -->
[Default](https://example.com/Default){ .md-button .md-button--primary target=_blank }

### Outlined button
<!-- ...and the one you'd think would be the 'default' (without the '--primary' suffix in Material
for MkDocs) is called 'outlined' in the CSC Design System. -->
[Outlined](https://example.com/Outlined){ .md-button target=_blank }

<!-- So, to recap, if you wan't a 'normal' filled-in button (called 'default'), you must add the
'.md-button--primary' class to the attribute list. -->

## Tabbed content
=== "First tab"
    Content can be divided into tabs. The first one is visible by default.

    !!! default ""
        There can be any content, like this admonition, under tabs.

=== "Second tab"
    | Tables | work | fine | too |
    |-|-|-|-|
    | just  | as | an | example |

=== "And so on..."
    It can get quite messy:

    !!! warning ""

        === "Probably not what you want"
            You can even have nested tabs under admonition under tabs.

        === "But possible, nonetheless"
            I would recommend against it, though.
