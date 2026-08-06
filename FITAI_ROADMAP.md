# FitAI Roadmap

Current Status: ~90% Complete

The core architecture of FitAI is complete.

Remaining work focuses on improving AI quality, removing temporary architecture, polishing the UI/UX, and preparing the project for presentation as a portfolio application.

## Checklist

- [X] Ticket 1 – Reliable Workout Tool Calling
- [ ] Ticket 2 – Remove Temporary Frontend Workout Dataset
- [ ] Ticket 3 – Return Structured Workout Objects
- [ ] Ticket 4 – Conversation Response Model Cleanup
- [ ] Ticket 5 – Prompt Engineering Improvements
- [ ] Ticket 6 – Better Intent Detection
- [ ] Ticket 7 – Smarter Follow-up Questions
- [ ] Ticket 8 – Improve Retrieval Quality
- [ ] Ticket 9 – Conversation Memory
- [ ] Ticket 10 – Replace Emojis with Icons
- [X] Ticket 11 – Message Animations
- [X] Ticket 12 – Skeleton Loading
- [X] Ticket 13 – Visual Polish
- [ ] Ticket 14 – Markdown Rendering
- [ ] Ticket 15 – Workout Card Improvements
- [ ] Ticket 16 – Documentation
- [ ] Ticket 17 – Architecture Diagrams
- [ ] Ticket 18 – Automated Testing
- [ ] Ticket 19 – Code Cleanup
- [ ] Ticket 20 – Performance Review

---

# Sprint 1 – Architecture Completion

## Checklist

- [ ] Ticket 1 – Reliable Workout Tool Calling
- [ ] Ticket 2 – Remove Temporary Frontend Workout Dataset
- [ ] Ticket 3 – Return Structured Workout Objects
- [ ] Ticket 4 – Conversation Response Model Cleanup

---

### Ticket 1 – Reliable Workout Tool Calling

**Goal**

Ensure GPT always calls the WorkoutTool whenever it recommends or describes a specific workout from the FitAI knowledge base.

**Why**

Currently GPT sometimes recommends workouts directly from RAG context without calling the tool.

This causes:

- Missing workout cards
- Missing response sources
- Inconsistent behaviour

The tool should become the source of truth for every workout recommendation.

---

### Ticket 2 – Remove Temporary Frontend Workout Dataset

**Goal**

Delete the temporary frontend workout dataset.

Instead, render WorkoutCards directly from backend data.

**Why**

The frontend currently duplicates workout information that already exists in the backend.

Removing duplication:

- simplifies maintenance
- removes synchronization issues
- creates a cleaner architecture

---

### Ticket 3 – Return Structured Workout Objects

**Goal**

Return complete workout objects instead of only workout names.

Current:

```json
{
  "answer": "...",
  "sources": [
    "Beginner Full Body Foundation"
  ]
}
```

Future:

```json
{
  "answer": "...",
  "workouts": [
    {
      "id": "...",
      "name": "...",
      "difficulty": "...",
      "goal": "...",
      "duration": "...",
      "equipment": [...]
    }
  ]
}
```

**Why**

The frontend should never need to reconstruct workout information.

It should simply render structured data.

---

### Ticket 4 – Conversation Response Model Cleanup

**Goal**

Introduce a cleaner ChatResponse model.

Example:

```text
ChatResponse

answer

recommended_workouts

metadata
```

**Why**

Future-proofs the API and makes it easier to extend with citations, conversation IDs, timestamps, and additional metadata.

---

# Sprint 2 – AI Quality

## Checklist

- [ ] Ticket 5 – Prompt Engineering Improvements
- [ ] Ticket 6 – Better Intent Detection
- [ ] Ticket 7 – Smarter Follow-up Questions
- [ ] Ticket 8 – Improve Retrieval Quality
- [ ] Ticket 9 – Conversation Memory

---

### Ticket 5 – Prompt Engineering Improvements

**Goal**

Improve the personality and coaching quality of FitAI.

**Focus**

- More natural coaching
- Less repetitive language
- Better recommendations
- Better explanations

**Why**

AI quality has a greater impact on user perception than additional UI features.

---

### Ticket 6 – Better Intent Detection

**Goal**

Improve GPT's understanding of user intent.

Distinguish between:

- educational questions
- workout recommendations
- workout comparisons
- plan requests

**Why**

Makes responses more reliable and prevents unnecessary tool usage.

---

### Ticket 7 – Smarter Follow-up Questions

**Goal**

Ask clarification questions when information is missing.

Example:

Instead of immediately generating a workout:

Ask:

- available equipment
- workout duration
- experience level

**Why**

Produces much higher quality recommendations.

---

### Ticket 8 – Improve Retrieval Quality

**Goal**

Tune the RAG pipeline.

Potential improvements:

- top_k tuning
- similarity thresholds
- metadata filtering

**Why**

Better retrieval leads directly to better GPT responses.

---

### Ticket 9 – Conversation Memory

**Goal**

Allow FitAI to remember previous conversation context.

Example:

User:

"I only have dumbbells."

Later:

"Build me another workout."

FitAI should remember available equipment.

**Why**

Transforms FitAI from a chatbot into a coaching assistant.

---

# Sprint 3 – Frontend Polish

## Checklist

- [X] Ticket 10 – Replace Emojis with Icons
- [X] Ticket 11 – Message Animations
- [X] Ticket 12 – Skeleton Loading
- [X] Ticket 13 – Visual Polish
- [ ] Ticket 14 – Markdown Rendering
- [ ] Ticket 15 – Workout Card Improvements

---

### Ticket 10 – Replace Emojis with Icons

**Goal**

Replace emojis with Lucide React icons.

Examples:

- Dumbbell
- Clock
- Target
- Flame
- Home

**Why**

Creates a more professional appearance.

---

### Ticket 11 – Message Animations

**Goal**

Improve transitions.

Examples:

- Fade in
- Slide up
- Loading transitions

**Why**

Makes the interface feel more responsive.

---

### Ticket 12 – Skeleton Loading

**Goal**

Show loading placeholders while waiting for responses.

Examples:

- Workout cards
- Messages

**Why**

Reduces perceived waiting time.

---

### Ticket 13 – Visual Polish

**Goal**

Improve:

- spacing
- typography
- border radius
- shadows
- hover effects

**Why**

Small improvements dramatically increase perceived quality.

---

### Ticket 14 – Markdown Rendering

**Goal**

Render GPT responses using Markdown.

Support:

- headings
- bold text
- bullet lists
- numbered lists

**Why**

Improves readability of longer AI responses.

---

### Ticket 15 – Workout Card Improvements

**Goal**

Enhance WorkoutCards.

Ideas:

- coloured difficulty badges
- equipment chips
- cleaner spacing
- improved layout

**Why**

WorkoutCards become the visual centrepiece of FitAI.

---

# Sprint 4 – Production Ready

## Checklist

- [ ] Ticket 16 – Documentation
- [ ] Ticket 17 – Architecture Diagrams
- [ ] Ticket 18 – Automated Testing
- [ ] Ticket 19 – Code Cleanup
- [ ] Ticket 20 – Performance Review

---

### Ticket 16 – Documentation

**Goal**

Improve the README.

Include:

- architecture
- setup
- screenshots
- technology stack

**Why**

Presentation matters for recruiters and portfolio reviewers.

---

### Ticket 17 – Architecture Diagrams

**Goal**

Create diagrams for:

- frontend
- backend
- RAG
- tool calling

**Why**

Helps demonstrate architectural understanding.

---

### Ticket 18 – Automated Testing

**Goal**

Increase confidence in the application.

Potential areas:

- backend services
- API routes
- React components
- integration flows

**Why**

Shows engineering maturity.

---

### Ticket 19 – Code Cleanup

**Goal**

Final refactoring.

Examples:

- remove dead code
- simplify folders
- remove unused imports
- improve comments

**Why**

Leaves the repository clean and maintainable.

---

### Ticket 20 – Performance Review

**Goal**

Review application performance.

Potential improvements:

- memoization
- lazy loading
- bundle optimisation

**Why**

Good engineering practice before release.

---

# Optional Version 2 Features

These are outside the scope of the current project but could form the basis of a future version.

## User Profiles

- Save preferences
- Equipment
- Goals
- Experience level

---

## Saved Workouts

- Favourites
- History
- Recently viewed

---

## Weekly Planner

Generate a weekly training schedule.

---

## Nutrition

Basic meal recommendations.

---

## Workout Tracking

Track completed workouts and progress.

---

## Authentication

Allow users to save conversations and workout history.

---

## Streaming Responses

Replace waiting for the full response with token-by-token streaming.

---

# Recommended Priority Before Presentation

## High Priority

- Reliable Workout Tool Calling
- Remove Temporary Frontend Workout Dataset
- Structured Workout Objects
- Prompt Engineering Improvements
- Better Intent Detection
- Documentation
- Architecture Diagrams

---

## Medium Priority

- Conversation Memory
- Retrieval Improvements
- Workout Card Improvements
- Markdown Rendering
- Visual Polish

---

## Low Priority

- Skeleton Loading
- Performance Optimisation
- Advanced Animations
- User Accounts
- Nutrition
- Workout Tracking
- Streaming Responses

---

# Current Project Assessment

Backend Architecture:      ★★★★★

Frontend Architecture:     ★★★★★

UI / UX:                   ★★★★☆

AI Quality:                ★★★☆☆

Production Readiness:      ★★★☆☆

Portfolio Readiness:       ★★★★☆

Estimated Completion: ~90%