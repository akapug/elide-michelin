"""
Elide Python HTTP Server for Michelin (WSGI format)
Backup server to avoid io_uring bug in TypeScript server
"""

import json
from datetime import datetime


def application(environ, start_response):
    """
    WSGI application callable for Elide server
    This is the standard WSGI interface
    """
    # Get request info from WSGI environ
    path = environ.get('PATH_INFO', '/')
    method = environ.get('REQUEST_METHOD', 'GET')
    
    # Health check endpoint
    if path == "/health":
        body = json.dumps({
            "status": "ok",
            "server": "elide-python-wsgi",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "note": "Using Python WSGI to avoid io_uring bug"
        })
        
        start_response('200 OK', [
            ('Content-Type', 'application/json'),
            ('Content-Length', str(len(body)))
        ])
        return [body.encode('utf-8')]
    
    # Root endpoint - server info
    if path == "/":
        body = json.dumps({
            "name": "Elide Michelin Server",
            "version": "0.1.0",
            "language": "Python",
            "format": "WSGI",
            "reason": "Avoiding TypeScript io_uring bug",
            "endpoints": [
                {"path": "/health", "method": "GET", "description": "Health check"},
                {"path": "/", "method": "GET", "description": "Server info"}
            ]
        })
        
        start_response('200 OK', [
            ('Content-Type', 'application/json'),
            ('Content-Length', str(len(body)))
        ])
        return [body.encode('utf-8')]
    
    # 404 for everything else
    body = json.dumps({
        "error": "Not Found",
        "path": path,
        "method": method
    })
    
    start_response('404 Not Found', [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(body)))
    ])
    return [body.encode('utf-8')]


# Note: Elide's Python server doesn't require explicit @bind for the fetch function
# when using the default export pattern

async def fetch(request):
    """
    Main HTTP handler for Elide server
    This is the Python equivalent of:
    export default { async fetch(request: Request): Promise<Response> { ... } }
    """
    # Get request URL
    url = str(request.url) if hasattr(request, 'url') else str(request)
    method = request.method if hasattr(request, 'method') else 'GET'
    
    # Health check endpoint
    if url.endswith("/health"):
        import json
        from datetime import datetime
        
        body = json.dumps({
            "status": "ok",
            "server": "elide-python",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "note": "Using Python to avoid io_uring bug"
        })
        
        return {
            "status": 200,
            "headers": {"Content-Type": "application/json"},
            "body": body
        }
    
    # Root endpoint - server info
    if url.endswith("/") or url.split(":")[-1].split("/")[-1] == "8080":
        import json
        
        body = json.dumps({
            "name": "Elide Michelin Server",
            "version": "0.1.0",
            "language": "Python",
            "reason": "Avoiding TypeScript io_uring bug",
            "endpoints": [
                {"path": "/health", "method": "GET", "description": "Health check"},
                {"path": "/", "method": "GET", "description": "Server info"}
            ]
        })
        
        return {
            "status": 200,
            "headers": {"Content-Type": "application/json"},
            "body": body
        }
    
    # 404 for everything else
    import json
    
    body = json.dumps({
        "error": "Not Found",
        "path": url,
        "method": method
    })
    
    return {
        "status": 404,
        "headers": {"Content-Type": "application/json"},
        "body": body
    }
