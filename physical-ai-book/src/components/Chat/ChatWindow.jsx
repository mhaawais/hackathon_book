import React, { useState, useEffect, useRef } from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import MessageList from './MessageList';
import MessageInput from './MessageInput';
import ChatControls from './ChatControls';
import HealthIndicator from './HealthIndicator';
import { createChatApi } from '../../utils/chat-api';

const ChatWindow = () => {
  const context = useDocusaurusContext();
  const { siteConfig = {} } = context;
  const chatApiBaseUrl = siteConfig.customFields?.chatApiBaseUrl || 'http://127.0.0.1:8001';
  const api = createChatApi(chatApiBaseUrl);

  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [healthStatus, setHealthStatus] = useState({ status: 'checking', timestamp: null });
  const [topK, setTopK] = useState(5);
  const [mode, setMode] = useState('retrieval'); // 'retrieval' or 'selected-text-only'
  const [selectedText, setSelectedText] = useState('');
  const messagesEndRef = useRef(null);

  // Check health on component mount
  useEffect(() => {
    const checkInitialHealth = async () => {
      try {
        const health = await api.health();
        setHealthStatus({
          status: health.status || 'unknown',
          timestamp: new Date().toISOString()
        });
      } catch (err) {
        setHealthStatus({
          status: 'unreachable',
          timestamp: new Date().toISOString()
        });
      }
    };

    checkInitialHealth();
  }, [chatApiBaseUrl]);

  // Scroll to bottom when messages change
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSubmit = async (inputText) => {
    if (!inputText.trim()) return;

    // Add user message to chat
    const userMessage = {
      id: Date.now(),
      text: inputText,
      sender: 'user',
      timestamp: new Date().toISOString()
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    setError(null);

    try {
      // Prepare the request based on the mode
      let requestData;
      if (mode === 'selected-text-only' && !selectedText.trim()) {
        throw new Error('Selected text is required in selected-text-only mode');
      }

      if (mode === 'selected-text-only') {
        requestData = {
          query: inputText,
          top_k: topK,
          selected_text: selectedText
        };
      } else {
        requestData = {
          query: inputText,
          top_k: topK
        };
      }

      // Call the API
      const response = await api.query(requestData);

      // Add assistant message to chat
      const assistantMessage = {
        id: Date.now() + 1,
        text: response.answer,
        sender: 'assistant',
        sources: response.sources || [],
        modeUsed: response.mode_used,
        retrievalTimeMs: response.retrieval_time_ms,
        totalTimeMs: response.total_time_ms,
        timestamp: new Date().toISOString()
      };

      setMessages(prev => [...prev, assistantMessage]);

      // Check health after successful response
      try {
        const health = await api.health();
        setHealthStatus({
          status: health.status || 'unknown',
          timestamp: new Date().toISOString()
        });
      } catch (err) {
        setHealthStatus({
          status: 'unreachable',
          timestamp: new Date().toISOString()
        });
      }
    } catch (err) {
      setError(err.message || 'An error occurred while processing your request');

      // Add error message to chat
      const errorMessage = {
        id: Date.now() + 1,
        text: `Error: ${err.message || 'An error occurred while processing your request'}`,
        sender: 'system',
        isError: true,
        timestamp: new Date().toISOString()
      };

      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      height: '100%',
      minHeight: '400px',
      border: 'none',
      borderRadius: '20px',
      backgroundColor: '#ffffff',
      boxShadow: '0 10px 35px -5px rgba(0, 0, 0, 0.15), 0 10px 15px -5px rgba(0, 0, 0, 0.08)',
      overflow: 'hidden',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif',
      maxWidth: '100%',
      border: '1px solid #e2e8f0'
    }}>
      {/* Header with health indicator */}
      <div style={{
        padding: '6px 12px',
        borderBottom: '1px solid #f1f5f9',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        background: 'linear-gradient(135deg, #f0f9ff, #e0f2fe)',
        position: 'sticky',
        top: 0,
        zIndex: 10
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{
            width: '12px',
            height: '12px',
            borderRadius: '50%',
            background: 'linear-gradient(135deg, #10b981, #059669)',
            boxShadow: '0 0 10px rgba(16, 185, 129, 0.4)',
            flexShrink: 0
          }}></div>
          <h3 style={{
            margin: 0,
            fontSize: '16px',
            fontWeight: '600',
            background: 'linear-gradient(135deg, #0f172a, #334155)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            letterSpacing: '-0.025em'
          }}>
            AI Assistant
          </h3>
        </div>
        <HealthIndicator status={healthStatus} />
      </div>

      {/* Controls */}
      <div style={{
        padding: '6px 12px',
        borderBottom: '1px solid #e2e8f0',
        backgroundColor: '#f8fafc',
        position: 'sticky',
        top: '35px',
        zIndex: 9,
        backdropFilter: 'blur(10px)'
      }}>
        <ChatControls
          topK={topK}
          setTopK={setTopK}
          mode={mode}
          setMode={setMode}
          selectedText={selectedText}
          setSelectedText={setSelectedText}
          modeEnabled={mode === 'selected-text-only'}
        />
      </div>

      {/* Messages */}
      <div style={{
        flex: 1,
        overflowY: 'auto',
        padding: '16px',
        backgroundColor: '#f8fafc',
        minHeight: '0',
        WebkitOverflowScrolling: 'touch' // Better scrolling on iOS
      }}>
        <MessageList messages={messages} />
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div style={{
        padding: '8px 12px',
        borderTop: '1px solid #e2e8f0',
        background: 'linear-gradient(135deg, #ffffff, #f8fafc)',
        position: 'sticky',
        bottom: 0,
        zIndex: 10
      }}>
        <MessageInput onSubmit={handleSubmit} isLoading={isLoading} />
      </div>

      {/* Error display */}
      {error && (
        <div style={{
          padding: '6px 12px',
          backgroundColor: '#fef2f2',
          color: '#dc2626',
          borderTop: '1px solid #fecaca',
          fontSize: '12px',
          fontWeight: '500',
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          position: 'sticky',
          bottom: '40px',
          zIndex: 9,
          borderRadius: '0 0 8px 8px',
          boxShadow: '0 -2px 4px rgba(0, 0, 0, 0.05)'
        }}>
          <div style={{
            width: '20px',
            height: '20px',
            borderRadius: '50%',
            backgroundColor: '#dc2626',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '12px',
            color: 'white',
            fontWeight: 'bold',
            flexShrink: 0
          }}>
            !
          </div>
          {error}
        </div>
      )}
    </div>
  );
};

export default ChatWindow;