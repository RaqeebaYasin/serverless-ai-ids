/**
 * ids-wrapper.js
 * Anomaly Detection Middleware for Serverless Functions
 * Purpose: Capture metadata and block Denial-of-Wallet (DoW) attacks.
 */

const idsMiddleware = (handler) => async (event, context) => {
    const startTime = Date.now();
    
    // 1. Capture Pre-Execution Metadata
    const telemetry = {
        memory_usage: process.memoryUsage().heapUsed / 1024 / 1024, // MB
        request_rate: event.headers['x-request-count'] || 1, 
        source_ip: event.requestContext?.identity?.sourceIp || "unknown",
        timestamp: new Date().toISOString()
    };

    try {
        // 2. Call AI Engine (Simulation of calling the Python Autoencoder)
        // In a real system, this would be a POST request to your Flask/AI API
        const isMalicious = await checkWithAI(telemetry); 

        if (isMalicious) {
            console.error(`[SECURITY ALERT] Blocked request from ${telemetry.sourceIp}`);
            return {
                statusCode: 403,
                body: JSON.stringify({ message: "Request blocked by AI-IDS" })
            };
        }

        // 3. Execute the actual function
        const response = await handler(event, context);

        // 4. Calculate Final Duration (Metadata for future training)
        const duration = Date.now() - startTime;
        console.log(`[IDS Log] Clean Request. Execution Time: ${duration}ms`);

        return response;

    } catch (error) {
        console.error("IDS Middleware Error:", error);
        // Fail-safe: let the request through if the IDS itself crashes
        return await handler(event, context);
    }
};

// Mock function for simulation
async function checkWithAI(data) {
    // Logic: If request rate is impossibly high, mark as malicious
    return data.request_rate > 100; 
}

module.exports = idsMiddleware;
