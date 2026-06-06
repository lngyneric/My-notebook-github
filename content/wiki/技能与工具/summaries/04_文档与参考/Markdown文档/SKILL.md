---
source: raw/04_文档与参考/Markdown文档/SKILL.md
raw_sha256: 0af2f12742148c3775f13fe4d11862949d2ce765738f77297a18fdf1ccbe28b7
compiled_at: 2026-04-24T06:15:22.410Z
---
<wiki>
# Obsidian Flavored Markdown Skill
## Summary
This skill enables the creation and editing of valid Obsidian Flavored Markdown, the native markup syntax for the Obsidian note-taking application. It combines standard Markdown specifications with Obsidian-specific extensions for internal linking, content embedding, structured metadata, and styled content blocks.

## Key Takeaways
1. Obsidian Flavored Markdown builds on CommonMark, GitHub Flavored Markdown, and LaTeX for math, with additional Obsidian-exclusive syntax.
2. Internal wikilinks support direct linking to notes, headings, and individual content blocks.
3. Embeds allow inline inclusion of other notes, media files, PDFs, and search results.
4. Callouts provide customizable, optionally foldable styled content blocks for note organization.
5. YAML frontmatter (properties) adds structured metadata to notes, including tags, aliases, and custom fields.

---

## Core Syntax Reference
### Overview of Supported Markdown Flavors
Obsidian uses a combined set of Markdown standards:
- [CommonMark](https://commonmark.org/) (core Markdown specification)
- [GitHub Flavored Markdown (GFM)](https://github.github.com/gfm/)
- [LaTeX](https://www.latex-project.org/) for mathematical notation
- Obsidian-specific extensions (wikilinks, callouts, embeds, properties, etc.)

### Basic Formatting
#### Paragraphs & Line Breaks
```markdown
This is a paragraph.

This is another paragraph (separated by a blank line).

For an in-paragraph line break, add two trailing spaces  
or use Shift+Enter.
```

#### Headings
```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

#### Text Formatting
| Style | Syntax | Example | Output |
|-------|--------|---------|--------|
| Bold | `**text**` or `__text__` | `**Bold**` | **Bold** |
| Italic | `*text*` or `_text_` | `*Italic*` | *Italic* |
| Bold + Italic | `***text***` | `***Both***` | ***Both*** |
| Strikethrough | `~~text~~` | `~~Striked~~` | ~~Striked~~ |
| Highlight | `==text==` | `==Highlighted==` | ==Highlighted== |
| Inline Code | `` `code` `` | `` `code` `` | `code` |

#### Escaping Special Characters
Use a backslash to escape formatting characters:
```markdown
\*This will not be italic\*
\#This will not be a heading
1\. This will not be a list item
```
Commonly escaped characters: `\*`, `\_`, `\#`, `` \` ``, `\|`, `\~`

---

### Internal Links (Wikilinks)
Obsidian's native internal link syntax uses double square brackets.
#### Basic Links
```markdown
[[Note Name]]
[[Note Name.md]]
[[Note Name|Custom Display Text]]
```

#### Links to Headings
```markdown
[[Note Name#Target Heading]]
[[Note Name#Target Heading|Custom Text]]
[[#Heading in the same note]]
[[##Search all headings containing this term]]
```

#### Links to Blocks
Add a block ID (format `^custom-id`) to the end of a content block to enable direct linking:
```markdown
This is a paragraph with a block ID. ^my-custom-block
```
For lists/quotes, place the block ID on a separate line after the block:
```markdown
> This is a multi-line quote
> spanning two lines

^my-quote-block
```
Block link syntax:
```markdown
[[Note Name#^my-custom-block]]
[[Note Name#^my-custom-block|Custom Display Text]]
```

#### Search Links
```markdown
[[##heading]]     Search vault for headings containing "heading"
[[^^block]]       Search vault for blocks containing "block"
```

---

### Standard Markdown Links
For URL-formatted links (spaces must be encoded as `%20`):
```markdown
[Display Text](Note%20Name.md)
[Display Text](Note%20Name.md#Heading)
[Display Text](https://example.com)
[Open Note](obsidian://open?vault=VaultName&file=Note.md)
```

---

### Embeds
Add an exclamation mark before a wikilink to embed content directly in the note.
#### Embed Notes
```markdown
![[Note Name]]
![[Note Name#Target Heading]]
![[Note Name#^block-id]]
```

#### Embed Media
```markdown
![[image.png]]
![[image.png|640x480]]    Custom width x height
![[image.png|300]]        Custom width (preserves aspect ratio)
![[audio.mp3]]
![[audio.ogg]]
```

#### External Images
```markdown
![Alt text](https://example.com/image.png)
![Alt text|300](https://example.com/image.png)
```

#### Embed PDFs
```markdown
![[document.pdf]]
![[document.pdf#page=3]]       Open to specific page
![[document.pdf#height=400]]   Set embed height
```

#### Embed Lists
Embed a specific list block by referencing its block ID:
```markdown
![[Note Name#^list-id]]
```
Where the target list has a block ID assigned:
```markdown
- List Item 1
- List Item 2
- List Item 3

^list-id
```

#### Embed Search Results
````markdown
```query
tag:#project status:done
```
````

---

### Callouts
Styled content blocks using modified blockquote syntax.
#### Basic Callouts
```markdown
> [!note]
> This is a default note callout.

> [!info] Custom Callout Title
> This callout has a custom title.

> [!tip] Title Only Callout (no body content)
```

#### Foldable Callouts
```markdown
> [!faq]- Collapsed by default
> Content is hidden until expanded.

> [!faq]+ Expanded by default
> Content is visible but can be collapsed.
```

#### Nested Callouts
```markdown
> [!question] Outer callout
> > [!note] Inner nested callout
> > Nested callout content
```

#### Supported Predefined Callout Types
| Type | Aliases | Description |
|------|---------|-------------|
| `note` | - | Blue, pencil icon |
| `abstract` | `summary`, `tldr` | Teal, clipboard icon |
| `info` | - | Blue, info icon |
| `todo` | - | Blue, checkbox icon |
| `tip` | `hint`, `important` | Cyan, flame icon |
| `success` | `check`, `done` | Green, checkmark icon |
| `question` | `help`, `faq` | Yellow, question mark |
| `warning` | `caution`, `attention` | Orange, warning icon |
| `failure` | `fail`, `missing` | Red, X icon |
| `danger` | `error` | Red, zap icon |
| `bug` | - | Red, bug icon |
| `example` | - | Purple, list icon |
| `quote` | `cite` | Gray, quote icon |

#### Custom Callouts (CSS)
Define custom callout styles with CSS:
```css
.callout[data-callout="custom-type"] {
  --callout-color: 255, 0, 0;
  --callout-icon: lucide-alert-circle;
}
```

---

### Lists
#### Unordered Lists
```markdown
- Item 1
- Item 2
  - Nested item
  - Second nested item
- Item 3

* Works with asterisks
+ Or plus signs
```

#### Ordered Lists
```markdown
1. First item
2. Second item
   1. Nested numbered item
   2. Second nested item
3. Third item

1) Alternative parenthesis syntax
2) With parentheses
```

#### Task Lists
```markdown
- [ ] Incomplete task
- [x] Completed task
- [ ] Task with sub-tasks
  - [ ] Unfinished subtask
  - [x] Completed subtask
```

---

### Blockquotes
```markdown
> This is a blockquote.
> It can span multiple lines.
>
> And include multiple paragraphs.
>
> > Nested blockquotes are supported.
```

---

### Code
#### Inline Code
```markdown
Use `backticks
