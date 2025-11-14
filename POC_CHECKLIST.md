# 🧪 POC Checklist: Mega-Meta Michelin

## Objective

Validate all medium/high-risk technical assumptions before full implementation.

**Timeline**: 1 week
**Success Criteria**: All critical items pass, document workarounds for failures

---

## Phase 1: Elide Server Basics (Day 1)

### 1.1 Simple HTTP Server
- [ ] Create `poc/01-http-server.ts`
- [ ] Implement basic fetch handler
- [ ] Test with `elide serve poc/01-http-server.ts`
- [ ] Verify: Responds to GET/POST requests
- [ ] Verify: CORS headers work
- [ ] Verify: JSON parsing works

**Expected**: ✅ Should work (proven in elideable)

### 1.2 React SSR
- [ ] Create `poc/02-react-ssr.ts`
- [ ] Import React and ReactDOMServer
- [ ] Render simple component to string
- [ ] Serve HTML via fetch handler
- [ ] Test in browser

**Expected**: ✅ Should work (Elide docs show TSX support)

### 1.3 Static Assets
- [ ] Create `poc/03-static-assets.ts`
- [ ] Serve files from `public/` directory
- [ ] Test: CSS, JS, images
- [ ] Verify: Correct MIME types

**Expected**: ✅ Should work (fs.readFile works)

---

## Phase 2: Convex Integration (Day 2)

### 2.1 Convex Client (TypeScript)
- [ ] Create `poc/04-convex-client.ts`
- [ ] Install `convex` package
- [ ] Initialize ConvexClient
- [ ] Test: Query from Convex
- [ ] Test: Mutation to Convex
- [ ] Test: Real-time subscription

**Expected**: ⚠️ Unknown - needs testing
**Fallback**: Use HTTP API if client doesn't work

### 2.2 Convex HTTP API
- [ ] Create `poc/05-convex-http.ts`
- [ ] Make HTTP request to Convex
- [ ] Parse response
- [ ] Test: Query via HTTP
- [ ] Test: Mutation via HTTP

**Expected**: ✅ Should work (HTTP is universal)

---

## Phase 3: Python Integration (Day 3)

### 3.1 Basic Python Execution
- [ ] Create `poc/06-python-basic.py`
- [ ] Write simple Python function
- [ ] Run with `elide poc/06-python-basic.py`
- [ ] Verify: Prints output
- [ ] Verify: Can import standard library

**Expected**: ✅ Should work (Elide supports Python)

### 3.2 Python ↔ TypeScript Interop
- [ ] Create `poc/07-polyglot.ts` and `poc/07-helper.py`
- [ ] Import Python module from TypeScript
- [ ] Call Python function from TypeScript
- [ ] Pass data between languages
- [ ] Test: String, number, object, array

**Expected**: ⚠️ Unknown - critical test
**Fallback**: Use subprocess if direct import fails

### 3.3 Python AI Libraries
- [ ] Create `poc/08-python-ai.py`
- [ ] Install `langchain` and `anthropic`
- [ ] Create simple LangChain agent
- [ ] Test: Agent responds to prompt
- [ ] Measure: Startup time, memory usage

**Expected**: ⚠️ Unknown - performance critical
**Fallback**: Keep TypeScript agent if too slow

---

## Phase 4: Remix on Elide (Day 4)

### 4.1 Simple Remix App
- [ ] Create `poc/09-remix-simple/`
- [ ] Initialize minimal Remix app
- [ ] Configure for Elide (if needed)
- [ ] Run with `elide serve`
- [ ] Test: SSR works
- [ ] Test: Client hydration works
- [ ] Test: Routing works

**Expected**: ⚠️ Unknown - may need Node.js APIs
**Fallback**: Use vanilla React SSR

### 4.2 Remix + Convex
- [ ] Create `poc/10-remix-convex/`
- [ ] Add Convex client to Remix
- [ ] Test: useQuery hook
- [ ] Test: useMutation hook
- [ ] Test: Real-time updates

**Expected**: ⚠️ Depends on 4.1 and 2.1
**Fallback**: Use React + Convex without Remix

---

## Phase 5: Preview System (Day 5)

### 5.1 Spawn Child Elide Process
- [ ] Create `poc/11-spawn-elide.ts`
- [ ] Spawn `elide serve` for generated app
- [ ] Capture stdout/stderr
- [ ] Test: Process starts successfully
- [ ] Test: Can kill process
- [ ] Test: Multiple processes simultaneously

**Expected**: ✅ Should work (proven in elideable)

### 5.2 Port Management
- [ ] Create `poc/12-port-manager.ts`
- [ ] Allocate dynamic ports (7777+)
- [ ] Track active processes
- [ ] Clean up on exit
- [ ] Test: 10 concurrent apps

**Expected**: ✅ Should work (basic logic)

### 5.3 Log Streaming
- [ ] Create `poc/13-log-stream.ts`
- [ ] Stream logs from child process
- [ ] Send via Server-Sent Events (SSE)
- [ ] Test: Real-time log updates in browser

**Expected**: ✅ Should work (SSE is standard HTTP)

---

## Phase 6: Integration Test (Day 6-7)

### 6.1 Mini Michelin
- [ ] Create `poc/14-mini-michelin/`
- [ ] Combine: Elide server + React SSR + Convex
- [ ] Add: Simple chat interface
- [ ] Add: Python agent (or TypeScript if Python fails)
- [ ] Add: Preview system
- [ ] Test: Generate simple app
- [ ] Test: Preview in iframe
- [ ] Test: Save to Convex

**Expected**: ⚠️ Integration test - will reveal issues

### 6.2 Performance Benchmarks
- [ ] Measure: Server startup time
- [ ] Measure: Request latency
- [ ] Measure: Memory usage (idle)
- [ ] Measure: Memory usage (10 apps)
- [ ] Measure: Python agent response time
- [ ] Compare: vs. Node.js baseline

**Expected**: ⚠️ Unknown - may need optimization

---

## Decision Matrix

After completing POC, use this matrix to decide:

| Scenario | Action |
|----------|--------|
| All tests pass | ✅ Proceed with Mega-Meta Plan |
| Python fails, rest passes | ⚠️ Use TypeScript agent, add Python tools later |
| Remix fails, rest passes | ⚠️ Use vanilla React SSR |
| Convex client fails | ⚠️ Use HTTP API |
| Multiple failures | ❌ Stick with Standard Plan |
| Performance issues | ⚠️ Optimize or use Hybrid Approach |

---

## POC File Structure

```
poc/
├── 01-http-server.ts
├── 02-react-ssr.ts
├── 03-static-assets.ts
├── 04-convex-client.ts
├── 05-convex-http.ts
├── 06-python-basic.py
├── 07-polyglot.ts
├── 07-helper.py
├── 08-python-ai.py
├── 09-remix-simple/
├── 10-remix-convex/
├── 11-spawn-elide.ts
├── 12-port-manager.ts
├── 13-log-stream.ts
└── 14-mini-michelin/
    ├── server.ts
    ├── agent.py (or agent.ts)
    ├── components/
    └── public/
```

---

## Success Metrics

### Must Pass (Critical)
- ✅ Elide server responds to HTTP requests
- ✅ Can spawn child Elide processes
- ✅ Convex integration works (client OR HTTP)
- ✅ React SSR works (Remix OR vanilla)

### Should Pass (Important)
- ⚠️ Python ↔ TypeScript interop
- ⚠️ Python AI libraries work
- ⚠️ Remix on Elide

### Nice to Have (Optional)
- ⚠️ Hot reload
- ⚠️ Performance matches Node.js
- ⚠️ Low memory usage

---

## Timeline

| Day | Focus | Deliverable |
|-----|-------|-------------|
| 1 | Elide basics | HTTP server, React SSR, static assets |
| 2 | Convex | Client integration or HTTP fallback |
| 3 | Python | Polyglot interop, AI libraries |
| 4 | Remix | Remix on Elide or React fallback |
| 5 | Preview | Child processes, port management, logs |
| 6-7 | Integration | Mini Michelin, benchmarks, decision |

---

**Status**: 📋 Ready to Execute | 📅 Created: 2025-11-14
**Next Action**: Create `poc/` directory and start with 01-http-server.ts

