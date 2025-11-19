export default {
    async fetch(request: Request): Promise<Response> {
        const url = new URL(request.url);

        // Health check endpoint
        if (url.pathname === "/health") {
            return new Response(JSON.stringify({
                status: "ok",
                server: "elide-typescript",
                timestamp: new Date().toISOString()
            }), {
                status: 200,
                headers: { "Content-Type": "application/json" }
            });
        }

        // Root endpoint - info about the server
        if (url.pathname === "/") {
            return new Response(JSON.stringify({
                name: "Elide Michelin Server",
                version: "0.1.0",
                language: "TypeScript",
                endpoints: [
                    { path: "/health", method: "GET", description: "Health check" },
                    { path: "/", method: "GET", description: "Server info" }
                ]
            }), {
                status: 200,
                headers: { "Content-Type": "application/json" }
            });
        }

        // 404 for everything else
        return new Response(JSON.stringify({
            error: "Not Found",
            path: url.pathname
        }), {
            status: 404,
            headers: { "Content-Type": "application/json" }
        });
    }
}
