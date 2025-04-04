---
search:
  boost: 0.1
---

# Reference card

!!! default "Documentation"

    Docs CSC is based on *Material for MkDocs*. Note that not all (by far) features are supported.

    [Reference - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/){ .md-button target=_blank }

!!! info "Source"

    This page is more useful when viewed side-by-side with [the Markdown source at GitHub](https://github.com/CSCfi/csc-user-guide/blob/master/docs/ref.md?plain=1){ target=_blank }.

This page contains some elements that are available in Docs CSC. For example, here we have some
body text [with an external link](https://example.com){ target=_blank }. **Some of it is
boldfaced**, *some italicized*. `Some might be monospaced`. Some acronyms, like HPC, are
defined automatically (see: [Glossary](#glossary)). One small addition: <small>Some small text.</small>

As you can see here:
in some cases [external links](https://example.com){ target=_blank } followed by text _italicized_
using underscores will produce unwanted results. *Italicize* with asterisks instead.

> Now, there's even text in a blockquote. The blockquote has some filler text after an empty line. I
like to imagine it's what a typewriter would dream.
>
> Vel suscipit quia voluptates quis. Rerum sequi voluptatem in non ipsam tempora quod natus. Soluta
perferendis illo saepe sint ipsa vitae provident non. Et qui quaerat et rerum libero officia omnis
enim. Laboriosam autem vel vel aut quod.

Here's a reference to a footnote:[^1]

And there's a reference to a second footnote:[^2]

Then&mdash;as a rule&mdash;a horizontal rule:

---


## Banners

The front page can be fitted with a banner to promote a course for example. The banner is controlled via the `extra.landing_banner` mapping in _mkdocs.yml_. The image file named in `extra.landing_banner.image` should be placed in the _docs-files_ Allas bucket, under _banners/_.

- `path:` _Don't touch!_
- `image:` The image filename in _docs-files/banners/_ Allas bucket.
- `title:` Shown, e.g. as a tooltip when pointing the image with a mouse cursor.
- `link:` The URL for more information, an enrolment page for a course etc.
- `description:` A short description of the banner rendered as alternative text. Provided mainly for accessibility, i.e. screen readers.
- `visible:` Set to `true` or `false` to show or hide the banner.

=== "mkdocs.yml"

    ```yaml
    extra:
      # ...
      landing_banner:
        path: https://a3s.fi/docs-files/banners/ # Put the image file in this bucket; Don't touch this value.
        image: example-banner.png
        title: Example banner now up on landing page
        link: https://example.org/courses/example-course/
        description: |-
          Banner for upcoming example course.
          Second line for example description.
        visible: true
    ```

    <div class="result" markdown>

    ![Screenshot of the landing page with a banner](https://a3s.fi/docs-files/reference-card/screenshot-of-landing-page-with-banner.png)

    </div>

=== "Show/hide"

    To show/hide the banner, just flip `extra.landing_banner.visible` from `false` to `true` (and _vice versa_):

    ```yaml
    extra:
      # ...
      landing_banner:
        # ...
        visible: false
    ```

    <div class="result" markdown>

    ![Screenshot of the landing page without the banner](https://a3s.fi/docs-files/reference-card/screenshot-of-landing-page-without-banner.png)

    </div>

## Glossary

There is a glossary of HPC-related acronyms that get highlighted automatically. For example: CPU,
GPU, QPU, etc. The acronyms are defined in the markdown file
_csc-overrides/assets/snippets/glossaries/hpc.md_. More acronyms (case-sensitive) can be added there or into another
markdown file, like so:

=== "another_glossary.md"

    ```markdown
    *[GNU]: GNU's not Unix!
    *[DFT]: 1. Discrete Fourier Transform, 2. Density Functional Theory
    ```

=== "mkdocs.yml"

    ```yaml
    markdown_extensions:
    - ...
    - pymdownx.snippets:
        base_path: csc-overrides/assets/snippets
        auto_append:
        - glossaries/hpc.md
        - glossaries/another_glossary.md
    - ...
    ```

The glossary is also viewable as a page at [docs.csc.fi/glossary](support/glossary.md).


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

``` py linenums="1" hl_lines="2 3"
# Here is a box with some syntax highlighted Python

from somewhere import some_code


NUMBER = 42
LIST = [1, 2, 'three']


class PythonClass:
    def __init__(self) -> None:
        self.__property = 'A string property'
    
    @property
    def property(self) -> str:
        return self.__property

    @staticmethod
    def method(parameter: int = 1) -> list[None]:
        return [None] * (parameter + NUMBER)

def main():
    string = f'Length of list is {len(LIST)}.'
    print(string)
```

Notice the optional line numbers and the line highlighting (on lines 2 and 3). Additionally, the code boxes can have a title:

```javascript title="looong_comment.js"
// Here's a JavaScript comment with a loooooooooooooooooooooooooooooooong line. You know, for testing purposes. Tell you what, let's make it just a bit longer still.
```

Diff works too:

```diff
-Departing
+Arriving
```

Remember to leave an empty line after the ` ``` ` in a source code box. Failing to do so can leave
any immediately following text as "loose", i.e., outside of an HTML paragraph (`<p>`).


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
    `error-label`,img/ref/image.png)
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
in [the Markdown source](https://github.com/CSCfi/csc-user-guide/blob/master/docs/ref.md?plain=1).


## Images

Here's an image of the Reference card with an image of the Reference card with...

![image of an image of an image...](https://a3s.fi/docs-files/reference-card/screenshot-of-image-of-image-of.png){ width=80% style="margin: 0 10%; border: var(--csc-border);" }


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
    allowfullscreen
></iframe>


### Animations

If you don't need sound (or controls), you can use animations as an alternative for embedded videos. They are
used just like [static images](#images). Both _.gif_ and _.png_ files work.


## Diagrams

### Mermaid

Documented here: <https://mermaid.js.org/intro/>, but for example a fenced block like this:

````markdown
```mermaid
%%{init: {'theme': 'neutral' }}%%
graph TD
    A(Does your reference card have a Mermaid chart?) -->|Yes| B(Good)
    A -->|No| C(Yes, it does.)
    C --> |What? No, you can't just... Oh.| B
```
````

produces a flowchart like that:

```mermaid
%%{init: {'theme': 'neutral' }}%%
graph TD
    A(Does your reference card have a Mermaid chart?) -->|Yes| B(Good)
    A -->|No| C(Yes, it does.)
    C --> |What? No, you can't just... Oh.| B
```


### Draw.io

Diagrams (including a toolbar) from [draw.io](https://draw.io) can be embedded as iframes by selecting _File ->
Embed -> IFrame..._. With line breaks added for illustration, the resulting piece of HTML could
look something like this:

```html
<iframe
  frameborder="0"
  style="width: 100%;
         height: 301px;"
  src="https://viewer.diagrams.net/?tags=blahblahblahblah%blah
       blahblahblah%blahblah%blah%blahblahblahblah%blahblah"
></iframe>
```

**The `src` attribute needs to be renamed to `srcdoc`:**

```html
<iframe
  ...
  srcdoc="..."
  ...
></iframe>
```

The size can be controlled by changing the value of the _style_ attribute. Note the units: _%_ for
width and _px_ for height. Here's an example with a width of 100 percent and a height of 500 pixels:

<iframe frameborder="0" style="width:100%;height:500px;" srcdoc="https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%22ftzXAFIqJNWyvfU7Nhta%22%3E7Zpbc9o4FMc%2FDY%2FxGN9wHgMk6UN2lllmJ7tPHWELW8W2WFmOIZ9%2BJUsy8gUwKWnSaZtkgo4uls7%2Fp%2BMjpSN7lu4eCdjGf%2BAQJiPLDHcjez6yrLFp2uwXt%2ByF5dZxhCEiKJSNDoYleoWqp7QWKIR5oyHFOKFo2zQGOMtgQBs2QAgum83WOGk%2BdQsi2DEsA5B0rc8opLGw%2Bq55sH%2BBKIrVk9mKRU0KVGNpyGMQ4lIz2fcje0YwpuJTupvBhDtP%2BUX0ezhSW0%2BMwIz2dPg7h%2BTP1TfuE8tMwIrpUjUS3RKUbUQ5ppS78o53tB5CHORGkAfGGrFSgNNtQVEW8RqUb6o2doxTeBMiwobGZC%2FGU7Pal%2BvNX8%2Fea%2Fa4%2BM83X2dP4fL5ZuzWy62XkdO9cjHBRRZCPsB4ZE%2FLGFG43IKA15YMKmaLaZrI6hS%2FgFXVk5cIzNGrXsYUUK3MaIR6GYZILyY42FQPNllBEqRVdz0snf4CCYU7zSTX9giZayj3ialqbam%2BxN9R5VKDSZpijaOafyD5jeqhDxKzD9KfqqiJfhKCRRFTxGcBV1y8jEKy5h4%2FyUZZlsaWd6wBOau8dVL4fANpEEv3axqDfCu28hrtuDzTnBK8gTOcYMKsGc4gN6r9xHuvUZKoeoaoPfXnD3worhRiu%2FkuQVHG6ijmPFWeWOAcUYS5NYDcA1rzp1aDFaYUp%2BKhWz77dBfxeGdEwdYyogSv4NcSExZbvh8ZxxqAjGOogXVq%2FHeFZrac8UCOgyJlqwOVa4YHk7Os2CdZ0fA4KxKQYteyVouYgmATVbFGA2Vd%2FTsKigBPBX6rg2II16BIaJvGEORxHVfayCCcTwzEok1uKF8yl023GFUf5iN3yr5NgwXNGdN4Zsofyx65c%2F59lcDktShz3S5lrmtMbruUeVehrPNC64XCk%2BsCSQH199exKIILymhk%2BqhsoAoOOKOa5uzrgU9hyvQIETzUycDSiiVV8%2FmxKNSQ%2BiyZ%2FZR1eNVg53OXWdHYUmW5eLMvVlYcQXL%2FIriqBmkjCMrcMYq8etZVIpZXhyOJk9eD08TvsqRsF7A0DJxJhxMYssROFjGhMY5wBpL7g3V6SEQqlOo2T5jLVHnyG6R0L%2FUABcVNsZgLyf4f3t9w7Yky%2FMtrDctV5flOPkGU9nppAQliDuDKVMaj6uS4IAE8v3MoIBGk517Rlsm9c1JrAhMW8l%2BaafHVZRt7H6rbWNeMh%2BDTkr1dHX%2BgOiJ1%2FjTy%2BBeG46HR6cirU5OoN%2Fi%2BPY8bGIhbrwLTHPv%2BvC%2BgvhYEGuK4xDp%2Bf0itUzn1evZ7Xs895wbHfSflbz86njai6ecMpf4P2qvHj%2FZelYuyM50X8Q%2FL5RdlY0PU5guy9sYVgDwhi8KAjH6sr7%2Bb0nM%2FPYnZN05%2F7U3Y3qspCkPBl3b6NzspdH%2BifAruzvasr5XkQ0b6zU3ftr0xDdN37cbWlfddg0WXgy%2F4Yg6j3DjNHni9zhmMbUjqKV01C1eXEZ9%2F97ND0odtf%2Fva279FgmTMHTdfDd5t6zwmFiR76TeIrYE812kO5LQGEivuDHRHCNhrzeS2Ozphz%2FF7J3zgVow4kOKByFoXpirXzUxaiYNr8q93yFh6z7udCNpOV1jwQAE0QvjCfuVGDEj4tbrf%2FfnuV93WZZljd%2FIkpydPclvh9HoHGPs3d78gd3VQ%2FjDunN%2Fc%2FYrcTVzD%2FWDyJj3ktQ4iC0BAklR%2FGmakwHyfU5geP5pozDK%2F0Av5k6bh54i%2BPzk2s9efjRKnlSL23MZ6PYzYb7rZP%2FwJWyRvh%2F8IYN%2F%2FDw%3D%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E"></iframe>


## Buttons

### Button

[Button](#button){ .md-button }


### Primary button

[Primary](#primary-button){ .md-button .md-button--primary }


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


## Snippets

Files under _csc-overrides/assets/snippets/_ may be added as snippets on the current page.

Suppose we have two Markdown files, _a.md_ and _b.md_ with the content

```markdown title="a.md"
Yes, this is _a.md_.
```

and

```markdown title="b.md"
Hello from _b.md_!
```

The file _ref/a.md_ (relative to the base path above) added as a snippet with

```markdown
;--8<-- "ref/a.md"
```

would look like this:

--8<-- "ref/a.md"

Adding _ref/a.md_ and _ref/b.md_ using

```markdown
;--8<--
ref/a.md
ref/b.md
;--8<--
```

would look like this:

--8<--
ref/a.md
ref/b.md
--8<--

Snippets also work from inside the source code boxes. For example

````markdown
```markdown
;--8<-- "ref/a.md"
```
````

would produce

````markdown
```markdown
--8<-- "ref/a.md"
```
````

More examples (untested in Docs CSC) can be found in [PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/).


## Hiding the sidebars

The sidebars on a particular page can be hidden by adding a `hide` property to the YAML front matter in the page Markdown source.

```yaml
---
hide:
  - toc
  - navigation
---

# Title of the page
```

Here's a preview screenshot for each case:

!!! warning ""

    Make sure that the breadcrumbs navigation at the top of the page is working correctly if hiding the navigation sidebar!

=== "Hide table of contents"
    ![Hide TOC](https://a3s.fi/docs-files/reference-card/screenshot-of-hidden-toc.png){ width=60% style="margin: 0 10%; border: var(--csc-border);" }

=== "Hide navigation"
    ![Hide nav](https://a3s.fi/docs-files/reference-card/screenshot-of-hidden-nav.png){ width=60% style="margin: 0 10%; border: var(--csc-border);" }

=== "Hide TOC and navigation"
    ![Hide both enabled](https://a3s.fi/docs-files/reference-card/screenshot-of-hidden-sidebars.png){ width=60% style="margin: 0 10%; border: var(--csc-border);" }


[^1]: This is the footnote ...and here's a shoenote for the footnote: 👞🎵
[^2]:
    Here's another footnote. Though, this one's a _barefootnote_!  
    Get it? 'Cause it's got no shoenote! Ahuehuehuehue!
