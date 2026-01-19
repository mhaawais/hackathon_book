/**
 * Creates a chat API client with the provided base URL
 * @param {string} baseUrl - The base URL for the API
 * @returns {Object} API client with health and query methods
 */
export const createChatApi = (baseUrl) => {
  // Normalize the base URL (remove trailing slash)
  const normalizedBaseUrl = baseUrl.endsWith('/') ? baseUrl.slice(0, -1) : baseUrl;

  return {
    /**
     * Makes a request to the health endpoint
     * @returns {Promise<Object>} The health status response
     */
    health: async () => {
      try {
        const response = await fetch(`${normalizedBaseUrl}/health`, {
          method: 'GET',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
          },
          // Add timeout
          signal: AbortSignal.timeout(10000) // 10 second timeout
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
      } catch (error) {
        if (error.name === 'AbortError') {
          throw new Error('Health check timed out');
        }
        throw error;
      }
    },

    /**
     * Makes a request to the chat API endpoint
     * @param {Object} params - Request parameters
     * @param {string} params.query - The user's query
     * @param {number} [params.top_k=5] - Number of chunks to retrieve
     * @param {string} [params.selected_text] - Selected text for selected-text-only mode
     * @param {string} [params.session_id] - Session identifier
     * @returns {Promise<Object>} The API response
     */
    query: async ({ query, top_k = 5, selected_text, session_id }) => {
      try {
        const response = await fetch(`${normalizedBaseUrl}/api/v1/chat/query`, {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            query,
            top_k,
            selected_text: selected_text || undefined,
            session_id: session_id || undefined
          }),
          // Add timeout
          signal: AbortSignal.timeout(30000) // 30 second timeout
        });

        if (!response.ok) {
          const errorData = await response.text();
          throw new Error(`HTTP error! status: ${response.status}, message: ${errorData}`);
        }

        const data = await response.json();
        return data;
      } catch (error) {
        if (error.name === 'AbortError') {
          throw new Error('Request timed out');
        }
        throw error;
      }
    }
  };
};