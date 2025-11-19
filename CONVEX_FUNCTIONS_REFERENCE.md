# Convex Functions Reference

## Overview
This document catalogs all Convex functions in the project for migration planning.

## Core Files

### convex/messages.ts
**Purpose**: Message storage, retrieval, and AI streaming

**Queries** (Read-only):
- `list` - List messages for a chat
- `get` - Get single message by ID
- `getChat` - Get chat by ID or URL ID
- `getLatestChatMessageStorageState` - Get latest message storage state

**Mutations** (Write):
- `send` - Send a new message
- `update` - Update existing message
- `deleteChat` - Delete a chat
- `createSubchat` - Create a subchat

**Actions** (External calls):
- `streamResponse` - Stream AI response from Anthropic
- `summarizeChat` - Summarize chat for title

**Migration Priority**: HIGH
**Complexity**: Medium-High (streaming is complex)
**Elide Opportunity**: Could use Elide for AI operations, keep Convex for storage

---

### convex/sessions.ts
**Purpose**: User session management

**Queries**:
- `get` - Get session by ID
- `getByUserId` - Get session by user ID

**Mutations**:
- `getOrCreate` - Get or create session for user

**Migration Priority**: MEDIUM
**Complexity**: Low
**Elide Opportunity**: Simple CRUD, easy to migrate

---

### convex/teams.ts
**Purpose**: Team management and permissions

**Queries**:
- `list` - List teams for user
- `get` - Get team by ID
- `getBySlug` - Get team by slug

**Mutations**:
- `create` - Create new team
- `update` - Update team
- `addMember` - Add member to team
- `removeMember` - Remove member from team

**Migration Priority**: MEDIUM
**Complexity**: Medium (permissions logic)
**Elide Opportunity**: Could benefit from polyglot for complex permissions

---

### convex/snapshot.ts
**Purpose**: File system snapshot storage

**Mutations**:
- `saveSnapshot` - Save file system snapshot to storage

**Queries**:
- `getSnapshotUrl` - Get URL for snapshot download

**Migration Priority**: HIGH
**Complexity**: Medium
**Elide Opportunity**: Could Elide handle file storage better?

---

### convex/apiKeys.ts
**Purpose**: API key management for AI providers

**Queries**:
- `get` - Get API keys for user/team
- `list` - List all API keys

**Mutations**:
- `set` - Set API key
- `delete` - Delete API key

**Migration Priority**: LOW
**Complexity**: Low (sensitive data)
**Elide Opportunity**: Keep in Convex for security

---

### convex/convexProjects.ts
**Purpose**: Convex project connection management

**Queries**:
- `get` - Get connected Convex project
- `list` - List Convex projects

**Mutations**:
- `connect` - Connect to Convex project
- `disconnect` - Disconnect from project

**Migration Priority**: LOW
**Complexity**: Medium
**Elide Opportunity**: Convex-specific, keep as-is

---

### convex/share.ts
**Purpose**: Chat sharing functionality

**Queries**:
- `getSharedChat` - Get shared chat by URL

**Mutations**:
- `shareChat` - Create shareable link
- `unshareChat` - Remove shareable link

**Migration Priority**: LOW
**Complexity**: Low
**Elide Opportunity**: Simple CRUD, could migrate

---

### convex/subchats.ts
**Purpose**: Subchat management (chat branching)

**Queries**:
- `list` - List subchats for chat
- `get` - Get subchat by ID

**Mutations**:
- `create` - Create new subchat
- `delete` - Delete subchat

**Migration Priority**: MEDIUM
**Complexity**: Medium
**Elide Opportunity**: Could migrate, but test branching logic carefully

---

### convex/deploy.ts
**Purpose**: Deployment management

**Actions**:
- `deploy` - Deploy generated app

**Migration Priority**: HIGH
**Complexity**: HIGH
**Elide Opportunity**: This is where deploy button fails - investigate!

---

### convex/openaiProxy.ts
**Purpose**: OpenAI API proxy

**Actions**:
- `proxyRequest` - Proxy request to OpenAI

**Migration Priority**: MEDIUM
**Complexity**: Medium
**Elide Opportunity**: Could use Elide for AI proxy

---

## Migration Recommendations

### Phase 1: Low-Hanging Fruit
1. `sessions.ts` - Simple CRUD
2. `share.ts` - Simple CRUD
3. `apiKeys.ts` queries - Read-only

### Phase 2: Core Features
1. `messages.ts` queries - Read messages
2. `teams.ts` queries - Read teams
3. `snapshot.ts` queries - Read snapshots

### Phase 3: Complex Operations
1. `messages.ts` mutations - Write messages
2. `teams.ts` mutations - Team management
3. `subchats.ts` - Branching logic

### Phase 4: AI Operations
1. `messages.ts` actions - AI streaming
2. `openaiProxy.ts` - API proxy
3. `deploy.ts` - Deployment (FIX FIRST!)

### Phase 5: Polyglot Opportunities
1. AI operations in Python (LangChain)
2. Complex permissions in Kotlin
3. File processing in Python

## Testing Strategy

For each migrated function:
1. Create Elide equivalent
2. Add feature flag to switch between Convex/Elide
3. Test with flag ON
4. Monitor for errors
5. Gradually roll out
6. Remove Convex version when stable

## Notes

- Keep Convex for real-time features (subscriptions)
- Use Elide for AI/LangChain operations
- Consider hybrid approach for gradual migration
- Test thoroughly after each migration
- Document what works and what doesn't

