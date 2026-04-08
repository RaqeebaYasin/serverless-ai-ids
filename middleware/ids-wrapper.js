// middleware/ids-wrapper.js

const idsMiddleware = async (event, context) => {
    const startTime = Date.now();
    
    // 1. Extract Metadata (as described in your paper)
    const metadata = {
        duration_estimate: 0, // Calculated at the end
        memory_usage: process.memoryUsage().heapUsed / 1024 / 1024, // MB
        request_rate: event.headers['X-Rate-Limit'] || 1, 
        source_ip: event.requestContext.identity.sourceIp
    };

    // 2. Call AI Logic (Hypothetical API call to Part 1)
    const isMalicious = await checkWithAI(metadata);

    if (isMalicious) {
        return {
            statusCode: 403,
            body: JSON.stringify({ message: "Blocked by AI-IDS: Anomalous Behavior Detected" })
        };
    }

    // 3. If normal, continue to function logic
    console.log("Request allowed. Proceeding...");
};
