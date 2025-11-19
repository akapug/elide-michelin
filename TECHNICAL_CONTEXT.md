# Technical Context for Elide Migration

## System Architecture

### Current Data Flow

```
User Input → Remix Frontend → Convex Backend → AI (Claude) → Code Generation → WebContainer → Preview
                    ↓                ↓
              Auth (WorkOS)    Storage (Convex DB)
```

### Key Components

#### 1. Frontend (Remix + React)
- **Entry**: `app/root.tsx`
- **Routing**: Remix file-based routing in `app/routes/`
- **State**: Nanostores (`app/lib/stores/`)
- **UI**: Custom components + Radix UI primitives

#### 2. Backend (Convex)
- **Functions**: `convex/*.ts` files
- **Types**: Query, Mutation, Action, HttpAction
- **Auth**: Integrated with WorkOS via `@convex-dev/workos`
- **Storage**: Built-in database + file storage

#### 3. AI Agent (Chef Agent)
- **Prompts**: `chef-agent/prompts/`
- **Streaming**: `app/lib/.server/llm/stream-text.ts`
- **Tools**: File operations, shell commands, etc.

#### 4. WebContainer
- **Runtime**: In-browser Node.js environment
- **File System**: Virtual FS synced with Convex
- **Preview**: Live app preview in iframe

## Convex Functions to Migrate

### High Priority (Simple Queries)
```typescript
// convex/messages.ts
export const list = query(...)           // List messages
export const get = query(...)            // Get single message
export const getChat = query(...)        // Get chat by ID

// convex/sessions.ts
export const get = query(...)            // Get session
export const getOrCreate = mutation(...) // Get or create session

// convex/teams.ts
export const list = query(...)           // List teams
export const get = query(...)            // Get team
```

### Medium Priority (Mutations)
```typescript
// convex/messages.ts
export const send = mutation(...)        // Send message
export const update = mutation(...)      // Update message

// convex/snapshot.ts
export const saveSnapshot = internalMutation(...) // Save file snapshot
```

### Low Priority (Complex Actions)
```typescript
// convex/messages.ts
export const streamResponse = action(...) // AI streaming (uses Anthropic SDK)
```

## Elide Integration Points

### Option 1: Replace Convex Entirely
- Migrate all functions to Elide
- Use Elide's database/storage
- Update frontend to call Elide endpoints

**Pros**: Full Elide integration, simpler stack
**Cons**: Large migration, higher risk

### Option 2: Hybrid Approach (RECOMMENDED)
- Keep Convex for real-time features
- Use Elide for AI/LangChain operations
- Gradual migration of suitable functions

**Pros**: Lower risk, incremental progress
**Cons**: Two backends to maintain

### Option 3: Elide as Middleware
- Convex remains primary backend
- Elide handles polyglot operations
- Minimal changes to existing code

**Pros**: Minimal risk, easy rollback
**Cons**: Limited Elide benefits

## File System Sync Architecture

### Current Implementation
1. **WebContainer** writes files
2. **FilesStore** (`app/lib/stores/files.ts`) watches changes
3. **fileUpdateCounter** increments on changes
4. **chatSyncWorker** (`app/lib/stores/startup/history.ts`) syncs to Convex
5. **BackupStatusIndicator** shows sync status

### Issues
- File sync can lag, causing "Saving..." toasts
- Sync state mismatch between WebContainer and Convex
- Currently disabled BackupStatusIndicator as workaround

### Elide Opportunity
- Could Elide provide better file sync?
- Could Elide replace WebContainer for some operations?
- Could Elide handle snapshot storage more efficiently?

## Authentication Flow

### Current (WorkOS + Convex)
```typescript
// app/root.tsx
<AuthKitProvider>
  <ConvexProviderWithAuthKit>
    {children}
  </ConvexProviderWithAuthKit>
</AuthKitProvider>
```

### Elide Integration
- Can Elide handle auth?
- Should we keep WorkOS?
- How to integrate Elide auth with Convex?

## AI Streaming Architecture

### Current Flow
```
User Message → Convex Action → Anthropic API → Stream Response → Frontend
```

### Key Files
- `app/lib/.server/llm/stream-text.ts` - Streaming logic
- `convex/messages.ts` - `streamResponse` action
- `app/components/chat/Chat.client.tsx` - UI

### Elide Opportunity
- LangChain integration via Elide
- Polyglot AI operations (Python for ML?)
- Better streaming performance?

## Testing Checklist

### After Each Change
- [ ] App loads without errors
- [ ] Can create new chat
- [ ] Can send message
- [ ] AI responds correctly
- [ ] Code generation works
- [ ] Preview displays correctly
- [ ] File editing works
- [ ] Terminal works
- [ ] No console errors
- [ ] No persistent toasts

### Regression Tests
- [ ] Authentication still works
- [ ] Team switching works
- [ ] Chat history persists
- [ ] File changes save
- [ ] Deploy button (when fixed)

## Migration Strategy

### Step 1: Audit
1. List all Convex functions
2. Categorize by complexity
3. Identify Elide equivalents
4. Document dependencies

### Step 2: Prototype
1. Create simple Elide endpoint
2. Test from frontend
3. Verify performance
4. Document learnings

### Step 3: Migrate Incrementally
1. Start with read-only queries
2. Add feature flags for rollback
3. Test thoroughly
4. Monitor for issues
5. Iterate

### Step 4: Optimize
1. Remove unused code
2. Simplify architecture
3. Improve performance
4. Update documentation

## Useful Commands

```bash
# Elide
elide help
elide run <file>
elide repl

# Convex
npx convex dev
npx convex deploy
npx convex dashboard

# Development
pnpm run dev
pnpm run build
pnpm run typecheck

# Testing
curl http://127.0.0.1:5173
curl http://127.0.0.1:3210
```

## Questions to Answer

1. Can Elide replace Convex for real-time features?
2. Can Elide handle WebContainer file sync better?
3. Should we use Elide for AI operations only?
4. What's the best polyglot use case?
5. How to handle authentication with Elide?
6. What's the deployment story with Elide?
7. Can we simplify the tech stack?
8. What are the performance implications?

## Success Metrics

- [ ] App still works perfectly
- [ ] Code is simpler
- [ ] Deployment is easier
- [ ] Performance is same or better
- [ ] Developer experience improved
- [ ] Documentation is clear

