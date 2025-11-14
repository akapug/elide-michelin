# 🎯 ELIDE-MICHELIN: Ultra-Meta AI App Generator

## Project Overview

**Elide-Michelin** is a fork of Convex's "Chef" (which itself is a fork of bolt.diy) that aims to create a production-ready, Elide-powered AI app generator.

### The Meta Layers
1. **Chef** = Convex's AI app builder that generates full-stack apps with Convex backend
2. **Elideable** = Original Elide-based AI app generator
3. **Michelin** = This project - using Chef's professional infrastructure to build a better Elideable with Elide+Convex integration

---

## Current Architecture

### Frontend (Remix + React)
- **Framework**: Remix with Vite
- **UI Components**: Custom design system from `@convex-dev/design-system`
- **Real-time**: Convex React hooks (`useQuery`, `useMutation`)
- **Auth**: WorkOS AuthKit integration
- **Editor**: CodeMirror with multi-language support
- **Preview**: WebContainer API for in-browser execution

### Backend (Convex)
- **Database**: Convex reactive database with real-time subscriptions
- **Schema**: Sessions, chats, messages (with LZ4 compression), API keys
- **Functions**: Queries, mutations, actions for chat/deploy/provisioning
- **Components**: Rate limiter, migrations

### AI Agent (`chef-agent/`)
- **System Prompts**: Extensive Convex guidelines
- **Tools**: view, edit, deploy, npmInstall, lookupDocs
- **Context Management**: ChatContextManager handles file context and streaming
- **Model Support**: Anthropic, OpenAI, Google, xAI, Bedrock

### Template System
- **Base Template**: `template/` directory with Vite + React + Convex
- **Snapshots**: Pre-built templates in `public/template-snapshot-*.bin`
- **Auth**: Convex Auth with Password and Anonymous providers

---

## Elide Capabilities

### Runtime Features
- **Polyglot**: JavaScript, TypeScript, Python, Java, Kotlin (all via GraalVM/Truffle)
- **Zero-config TypeScript/TSX**: Run directly without build steps
- **Cross-language interop**: Import Python from JS, etc.
- **Performance**: ~800K RPS on Linux (TechEmpower benchmarked)

### Server Features
- **Built-in HTTP server**: Netty + Micronaut powered
- **Modern protocols**: HTTP/2, HTTP/3, WebSockets
- **TLS**: OpenSSL/BoringSSL support
- **Non-blocking I/O**: By default

### Project Management
- **Package managers**: Maven, NPM, PyPI, Rubygems, HuggingFace
- **Manifest support**: `package.json`, `pyproject.toml`, `requirements.txt`
- **Scripts**: Run tasks via `elide <script-name>`

---

## Integration Opportunities

### 1. Elide as Runtime for Generated Apps
- **Faster execution**: Native binary vs. browser sandbox
- **Polyglot apps**: Generate Python + TypeScript + Java in one app
- **Better performance**: GraalVM JIT compilation
- **Real deployment**: Not just preview, actual production runtime

### 2. Convex + Elide Synergy
```typescript
// Generated app using Elide server with Convex backend
export default {
  async fetch(request: Request): Promise<Response> {
    const convex = new ConvexClient(process.env.CONVEX_URL);
    const data = await convex.query(api.messages.list);
    return new Response(JSON.stringify(data));
  }
}
```

### 3. Enhanced System Prompts
- **Polyglot patterns**: How to mix languages
- **Elide server setup**: Using `elide serve`
- **Performance optimization**: GraalVM-specific tips
- **Deployment**: Elide native binary generation

---

## Proposed Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    MICHELIN UI (Remix)                      │
│  - Chat interface for app generation                        │
│  - Code editor (CodeMirror)                                 │
│  - Live preview (Elide-powered, not WebContainer)           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              CONVEX BACKEND (Reactive DB)                   │
│  - Store chats, sessions, generated code                    │
│  - Real-time sync to UI                                     │
│  - Deploy automation                                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│           MICHELIN AGENT (Enhanced Chef Agent)              │
│  - Elide-aware system prompts                               │
│  - Polyglot code generation                                 │
│  - Elide + Convex integration patterns                      │
│  - Tools: elideServe, elideProject, etc.                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              GENERATED APP (Elide Runtime)                  │
│  - Polyglot: TS + Python + Java + Kotlin                    │
│  - Elide server (800K RPS capable)                          │
│  - Convex backend (real-time, reactive)                     │
│  - Native binary deployment option                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Implementation Plan

### Phase 1: Foundation (Weeks 1-2)
1. ✅ Understand current Chef architecture
2. Set up Elide integration layer
3. Convex MCP integration
4. Test basic Elide server generation

### Phase 2: Agent Enhancement (Weeks 3-4)
1. Extend system prompts with Elide guidelines
2. New agent tools (elideServe, elideInit, elidePolyglot, elideOptimize)
3. Template updates with Elide server setup

### Phase 3: Runtime Integration (Weeks 5-6)
1. Replace WebContainer with Elide
2. Document Convex + Elide patterns
3. Create example apps

### Phase 4: Production Features (Weeks 7-8)
1. Deployment pipeline with native binaries
2. Advanced features (debugging, profiling, security)

---

## Key Insights

### Competitive Advantages
- Only polyglot AI app generator with production runtime
- Convex's real-time backend superior to traditional REST APIs
- Native performance beats interpreted/JIT-only runtimes
- Type safety across frontend, backend, and database

### Challenges
- Elide maturity (v1.0.0-beta11-rc1)
- Need comprehensive Elide guidelines for AI
- Multi-language debugging complexity
- Learning curve for developers

---

**Status**: ✅ Exploration Complete | 📅 Created: 2025-11-14

