---
📅 created: 12.06.2026 16:59
aliases:
tags:
  - article
  - guidelines
  - rules
author: Martin
---


# [[Article guidelines]]

Principles:
- Fast scanning
- actionable to the reader
- context preserved inside the article
- searchable / future retrieval
- low fluff
- Context preserved for later use

For a senior with too little time and mild sleep deprivation.
#### Tone patterns
Consistenly:
- sound confident
- avoid emotional hedging
- acoid "content createor voice"
- avoid fake neutrality!

GOOD
> “This is how it behaves.”

BAD:
> “It appears that under some circumstances…”

#### Stylistic fingerprints
OPERATIONAL FRAMING:
Consistently ask: What changes in reality because if this?
Not: What's theoretically true?

FAST SCANABILITY:
Articles are easy to skim read and searchable/grep-style information extraction. Very littel prose overhead

CONCRETE VERIFICATION:
Almost always include:
- how to check
- expected results
- command output
- failure behaviour

STRONG NAMING PRECISION
Avoid vauge nouns:
GOOD:
- RUntime check
- Socket Anaylsis
- Test Hardware
- Power density

BAD:
- Details
- Stuff
- More Information


## 1. Structural patterns
###### One problem / topic per article
> "What exact problem does this solve"
- **Tightly scope titles**: 
	- GOOD: "Verify fstab is correctly edited". BAD: "Linux fstab tip"
	- GOOD: "Fix Drone falling out of sky - ESC Motor Desyncs". BAD: "Drone Notes"

###### Titles
- imperative ("Set the cap...")
- diagnostic ("Runtime check")
- conceptual ("Why does this happen")
- procedural ("Test scenario")

GOOD:
- RUntime check
- Power density
- Current Situation
- Push for action
BAD:
- A deep dive into...
- Understanding...
- Exploring...

HEADING TYLE:
- `Verb + Object`: "Verify fstab", "Create UUID", "Set German number format"
- `Category: Detail`: System wide: Modifying the range"

###### Research / analysis articles structure
1. topic
2. current situation
3. historical context
4. implications
5. sources

## 2. Sentence patterns
###### Short declarative statements
Use: 
- active language
- no fluff words

- GOOD: "Chrony listens to the last entry it finds". 
- BAD: "The chrony parser is listening to the last entry it finds in the configured file".

###### Explanation first, nuance later
Rarely start with theory!. Start with:
- effect
- outcome
- operational relevance

Pattern ([[Minto pyramid]]):
```
Direct statement.
Supporting details
```

Example:
```
Motor desyncs cause the death roll.
These adjustments help...
```


## 3. Reader-oriented operational wording
Optimize for:
- What do I do?
- What happens?
- How do I verify it?

Not "abstract concepts" or "exhaustive completeness"

Common words "verify", "check", "result", "apply changes", "runtime", "current range".

## 4. Information Density Pattern
Compress aggressively, avoid transitions or narrative filler or fancy rhetorical padding.

typical pattern:
```
Claim:
- numbers
- implication
```

Example:
```
120.000km²
- 6.000GW
- 225% of demand
```


## 5. Sources usage
- propper source attribution
- numbered references: inline `[1]`

Use the template for sources at the end of the article: 
```
[1] TITLE. AUTHOR. DATE. MEDIUM. LINK. (DATE LAST SEEN)
```

If some are not available leave them out. Otherwise just put the URL after the number.

## 6. Article patterns
QUICK FIX NOTES ("Future me forgot the command" notes):
```
Problem  
Command/config  
Verification  
Source
```

TROUBLESHOTTING PLAYBOOK (SRE runbooks):
```
Symptom
Cause
Fixes
Verification
Hardware isolation/testing
Sources
```

BEHAVIORAL / PRODUCTIVIY RULES (opinionated, but applicable):
```
Strong thesis
Practical rules
Examples
Warnings
```

RESEARCH BRIEF (policy memos, implies good/bad things):
```
Claim  
Background  
Current situation  
Impact  
Historical context  
Implications  
Sources
```

QUALITATIVE ANALYSIS (academic style simpler):
```
Main claim  
Numbers  
Conversion logic  
Assumptions  
Caveats  
Sources
```


## Templates
META TEMPLATE:
```
# Problem / Thesis

One Strong opening statement.

## Why this matters (optional. bullet points)

## Steps / Findings / Analysis

Short sections with:
- commands
- bullets
- examples
- expected behavior

## Verification (optional, but common)

## Implications / Notes (optional)

## Sources

```

```
# Problem / Thesis

One Strong opening statement.

## Why this matters (optional. bullet points)

## Steps / Findings / Analysis

Short sections with:
- commands
- bullets
- examples
- expected behavior
  
## Cause / Background (optional)

## Solution / Findings

### Method 1
Commands/config

### Verification (optional but common)
Expected output

## Implications / Notes (optional)

## Notes (optional)

## Sources
```




 🔮 Origin:: [[17.05.2026]]
