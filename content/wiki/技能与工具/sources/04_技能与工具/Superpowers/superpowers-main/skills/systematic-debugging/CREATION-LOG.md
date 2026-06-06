---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/CREATION-LOG.md
raw_sha256: b482ef9a918fbfc6c369729e8160633ddfa2332466dd362ee73f1527c239ef8b
compiled_at: 2026-04-14T16:54:52.672Z
---
# Systematic Debugging Skill Creation Log
This document records the full process of extracting, structuring, and bulletproofing the systematic debugging skill, serving as a reference example for critical skill creation.

## Summary
Systematic debugging is a pressure-resistant root-first debugging framework extracted from an existing personal documentation. It follows a standardized skill structure, includes concrete step-by-step phases, explicit anti-pattern guidance, and structural defenses against rationalization under time pressure. It has been validated through 4 different test scenarios and is ready for use.

## Source Material
The core framework was extracted from `/Users/jesse/.claude/CLAUDE.md`:
- 4-phase systematic process: Investigation → Pattern Analysis → Hypothesis → Implementation
- Core mandate: *Always find root cause, never fix symptoms*
- Designed to resist time pressure and rationalization of shortcuts

## Extraction Decisions
### Included Content
- Complete 4-phase framework with all rules
- Anti-shortcut guidance (e.g. "NEVER fix symptom", "STOP and re-analyze")
- Pressure-resistant language (e.g. "even if faster", "even if I seem in a hurry")
- Concrete steps for each phase

### Excluded Content
- Project-specific context
- Repetitive variations of the same rule
- Narrative explanations (condensed to core principles)

## Standard Skill Structure
This skill follows the standardized structure defined in `skill-creation/SKILL.md`:
1. Rich `when_to_use` section covering applicable scenarios and common anti-patterns
2. Categorized as a concrete `technique` type skill with clear step-by-step process
3. Core keywords: `root cause`, `symptom`, `workaround`, `debugging`, `investigation`
4. Decision flowchart for the "fix failed" scenario (re-analyze vs add incremental fixes)
5. Phase-by-phase breakdown in scannable checklist format
6. Dedicated anti-patterns section defining what behaviors to avoid

## Bulletproofing Design
The framework is intentionally designed to resist rationalization of shortcuts under time pressure:
### Language Choices
- Uses absolute terms "ALWAYS" / "NEVER" instead of vague "should" / "try to"
- Explicitly reminds against pressure: "even if faster" / "even if I seem in a hurry"
- Explicit pause instruction: "STOP and re-analyze"
- Guards against common misbehavior: "Don't skip past"

### Structural Defenses
- Phase 1 (Investigation) is required, cannot skip directly to implementation
- Single hypothesis rule to prevent scattered "shotgun" fixes
- Explicit mandatory action for failed fixes
- Dedicated anti-pattern section that clearly describes common shortcuts

### Redundancy Reinforcement
- The core "find root cause" mandate is repeated across overview, `when_to_use`, Phase 1 and implementation rules
- "NEVER fix symptom" is stated 4 times in different contexts
- Each phase includes explicit "don't skip" guidance

## Validation Testing
Four validation tests were conducted following the `skills/meta/testing-skills-with-subagents` standard, and all tests passed with no observed rationalization of shortcuts:
1. **Academic Context (No Pressure):** Perfect compliance with full investigation for a simple bug
2. **Time Pressure + Obvious Quick Fix:** Resisted the shortcut, followed full process and found the real root cause
3. **Complex System + Uncertainty:** Completed systematic investigation through all layers and found the failure source
4. **Failed First Fix:** Stopped, re-analyzed and formed a new hypothesis, did not deploy shotgun fixes

## Iterations
### Initial Version
- Included complete 4-phase framework
- Added dedicated anti-patterns section
- Added flowchart for "fix failed" decision making

### Enhancement 1: TDD Clarification
- Added a link to the `skills/testing/test-driven-development` skill
- Added clarification that TDD's "simplest code" principle is not equivalent to debugging's "root cause first" principle
- Prevents confusion between the two methodologies

## Final Outcome
The final bulletproof skill meets all requirements:
- ✅ Clearly mandates root cause investigation
- ✅ Resists rationalization under time pressure
- ✅ Provides concrete steps for each phase
- ✅ Explicitly defines common anti-patterns
- ✅ Tested across multiple pressure and complexity scenarios
- ✅ Clarifies its relationship to test-driven development
- ✅ Ready for practical use

## Key Insight
The most effective bulletproofing for this skill is the dedicated anti-patterns section that explicitly lists exact shortcuts that feel justified in the moment. When a user is tempted to make a quick symptom fix, recognizing this exact pattern as an anti-pattern creates cognitive friction that prevents the shortcut.

## Usage Example
When encountering a bug:
1. Load the skill: `skills/debugging/systematic-debugging`
2. Read the overview (≈10 seconds) to recall the core mandate
3. Follow the Phase 1 checklist to force full investigation
4. If tempted to skip steps, check the anti-pattern section and stop the shortcut
5. Complete all phases to find the root cause

- **Time investment:** 5-10 minutes
- **Time saved:** Hours of repeated "symptom whack-a-mole" fixes

---
*Created: 2025-10-03*
*Purpose: Reference example for skill extraction and bulletproofing*
