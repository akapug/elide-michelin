# Agent Handoff: Elide-ification Phase

## Current Status ✅

**The app is now WORKING!** 🎉

- ✅ Both servers running (Convex local on :3210, Remix dev on :5173)
- ✅ App generates full-stack apps successfully (tested with PhotoStream example)
- ✅ Preview works perfectly
- ✅ Authentication works
- ✅ File editing works
- ✅ Terminal works
- ✅ Persistent "Saving..." toasts fixed (BackupStatusIndicator temporarily disabled)

## Known Issues 🐛

1. **Deploy button creates unknown error** - needs investigation
   - Location: `app/components/header/DeployButton.tsx`
   - Flow: Build → Zip → POST to `/api/deploy-simple` → Deploy to Convex hosting
   - Backend: `app/lib/.server/deploy-simple.ts`
   - Likely issue: Missing env vars or Convex hosting API error
   - Check browser console and network tab for error details

2. **BackupStatusIndicator disabled** - was causing persistent "Saving..." toasts due to file sync state mismatch
   - Location: `app/components/workbench/Workbench.client.tsx` (line 197, commented out)
   - Root cause: File update counter doesn't match saved counter
   - Temporary fix: Disabled component
   - Proper fix: Debug chatSyncWorker in `app/lib/stores/startup/history.ts`

## Your Mission 🎯

**Elide-ify the Michelin app step by step with E2E testing cycles**

### Priority 1: Maintain Chef's UX (or better)
- Do NOT worsen the user experience
- Keep all working features working
- Test thoroughly after each change

### Priority 2: Use Elide to simplify operations
- Replace Node.js/TypeScript backend with Elide polyglot where viable
- Separate FastAPI server for LangChain is acceptable if Elide polyglot isn't viable
- Focus on operational simplification without UX degradation

## Architecture Overview

### Current Stack
- **Frontend**: Remix (React) + Vite
- **Backend**: Convex (TypeScript functions)
- **AI**: Anthropic Claude via Convex actions
- **Auth**: WorkOS AuthKit
- **Container**: WebContainer (in-browser Node.js runtime)

### Key Files to Understand

#### Frontend Entry Points
- `app/root.tsx` - Root layout with auth providers
- `app/routes/_index.tsx` - Homepage
- `app/routes/chat.$id.tsx` - Main chat interface
- `app/components/Homepage.client.tsx` - Landing page

#### AI/Chat Logic
- `chef-agent/` - AI agent prompts and logic
- `app/lib/stores/chatId.ts` - Chat state management
- `app/components/chat/` - Chat UI components

#### Convex Backend
- `convex/messages.ts` - Message storage and retrieval
- `convex/sessions.ts` - User session management
- `convex/teams.ts` - Team management
- `convex/snapshot.ts` - File system snapshot storage

#### WebContainer Integration
- `app/lib/.server/llm/stream-text.ts` - AI streaming
- `app/lib/runtime/action-runner.ts` - Executes file operations in WebContainer
- `app/lib/stores/files.ts` - File system state management

## Testing Strategy 🧪

### E2E Testing Workflow
1. **Make a small change**
2. **Test the change** by:
   - Refreshing the browser at http://127.0.0.1:5173
   - Creating a new chat
   - Generating an app (use simple prompts like "create a todo app")
   - Testing the preview
   - Testing file editing
   - Testing the terminal
3. **Verify no regressions**
4. **Commit if successful**
5. **Repeat**

### Test Prompts
- Simple: "create a todo app with local storage"
- Medium: "create a photo sharing app with likes"
- Complex: "create a real-time chat app with presence"

## Elide-ification Steps (Suggested Order)

### Phase 1: Research & Planning
1. Run `elide help` to understand Elide capabilities
2. Review Convex MCP documentation
3. Identify which Convex functions can be replaced with Elide
4. Document the migration plan

### Phase 2: Backend Migration (Incremental)
1. Start with read-only operations (queries)
2. Move to simple mutations
3. Handle complex operations last
4. Keep Convex as fallback during migration

### Phase 3: Polyglot Exploration
1. Identify opportunities for polyglot (Python, Kotlin, etc.)
2. Test Elide's polyglot capabilities
3. Migrate suitable components
4. Document what works and what doesn't

### Phase 4: Optimization
1. Remove unnecessary dependencies
2. Simplify deployment
3. Improve performance
4. Update documentation

## Running the App

### Start Both Servers
```bash
# Terminal 1: Convex local backend
npx convex dev --once --url http://127.0.0.1:3210

# Terminal 2: Remix dev server
pnpm run dev
```

### Or use the background processes (already running)
```bash
# Check if running
lsof -i :3210 -i :5173 | grep LISTEN

# View logs
tail -f convex.log
tail -f dev.log
```

## Important Notes ⚠️

1. **Don't break the working app** - test after every change
2. **Commit frequently** - small, atomic commits
3. **Document decisions** - especially when Elide can't replace something
4. **Ask for help** - if stuck, ask the user
5. **Preserve UX** - Priority 1 is maintaining Chef's UX or better

## Resources 📚

- Elide CLI: `elide help`
- Convex MCP: Check Convex tools available
- Backup branch: `backup-before-cleanup` (has all original docs)
- Git history: `git log --oneline` to see recent changes

## Next Steps for You

1. **Verify the app works** - refresh browser, test basic functionality
2. **Run `elide help`** - understand what Elide can do
3. **Review Convex functions** - identify migration candidates
4. **Create a migration plan** - document in a new file
5. **Start with smallest change** - test thoroughly
6. **Iterate with E2E testing** - make it work, make it right, make it fast

Good luck! 🚀

